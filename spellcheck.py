# Spell checker
# Written by Peter Norvig
import re, collections
import ConfigParser
import string
import csv
from nltk import *

config = ConfigParser.ConfigParser()

config.read('text_config.ini')
filename = config.get('File functions', 'Input File Path')
filetype = config.get('File functions', 'Input File Format')
if_spell = config.get('File functions', 'Check Spelling')

def read_file(file_name):
	read_filename = open(filename, 'r')
	read_filename = read_filename.read()
	return read_filename
def read_txt(file_name):
	inp = []
	with open(file_name, 'rU') as g:
		reader = csv.reader(g,delimiter = '\t')
		sent = list(reader)
	for x,y in sent:
		inp.append(x)
	return inp

def read_json():
	inp = []
	with open(filename, 'r') as f:
		reader = json.load(f)
	key = reader[1].keys()
	length = len(reader)
	for x in xrange(0,length):
		inp.append(reader[x][key[1]])
	return inp

def read_xml():
	pass

def read_rss():
	pass

def read_csv():
	inp = []
	with open(file_name, 'rU') as g:
		reader = csv.reader(g,delimiter = ',')
		sent = list(reader)
	for x,y in sent:
		inp.append(x)
	return inp

def word_tokenizer(sentence):		# Example:
	tokens = word_tokenize(sentence)	# "This is a sentence"
	return tokens

def words(text):
	return re.findall('[a-z]+', text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/enchant/share/enchant/myspell/en_US.dic').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word)or [word]
    return max(candidates, key=NWORDS.get)

def strip_punc(sentence):
	return(sentence.translate(string.maketrans("",""), string.punctuation))

def hyphen_rem(sentence):
	return(sentence.replace("-"," "))

tokenized = read_file(filename)
#tokenized = hyphen_rem(tokenized)
#tokenized = strip_punc(tokenized)
tokenized = tokenized.split()
print len(tokenized)
for x in xrange(0,len(tokenized)):
	print correct(tokenized[x])


