# This is the full text analytics suite, including the cleanser, stemmer, language classifier, spell checker, grammar checker, entity recognizer and content summarizer
import string
import re
import csv
import json
import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import numpy as np
import nltk
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('text_config.ini')
filename = config.get('File functions', 'Input File Path')
filetype = config.get('File functions', 'Input File Format')
output_file = config.get('File functions', 'Output File')
task_type = config.get('File functions', 'Type of Task')
if_cleanse = config.get('File functions', 'Cleanse')
if_stem = config.get('File functions', 'Stem')
if_spell = config.get('File functions', 'Check Spelling')
if_grammar = config.get('File functions', 'Check Grammar')
if_lang = config.get('File functions', 'Detect Language')
if_ner = config.get('File functions', 'Detect Named Entities')
if_summarize = config.get('File functions', 'Summarize File')
decode = config.get('Cleanser', 'Decode Text')
url_rem = config.get('Cleanser', 'Remove URL')
stop_rem = config.get('Cleanser', 'Remove Stopwords')
word_tok = config.get('Cleanser', 'Tokenize Words')
sent_tok = config.get('Cleanser', 'Tokenize Sentences')
apos_rem = config.get('Cleanser', 'Remove Apostrophes')
strip_punc = config.get('Cleanser', 'Remove Punctuation')
html_char = config.get('Cleanser', 'Convert Escape Characters')
html_tag = config.get('Cleanser', 'Remove HTML Tags')
word_count = config.get('Stemmer', 'Word Count')
postag_show = config.get('Stemmer', 'Show POS Tags')
spell_words = config.get('Spell Checker', 'Show Closest Word')
sep_entities = config.get('Named Entity Recognizer', 'Separate Entities')
entity_freq = config.get('Named Entity Recognizer', 'Entity Frequency')

def read_txt():
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

def sent_tokenizer(sentence):
	tokens = sent_tokenize(sentence)
	return tokens

def strip_punc(sentence):
	return(sentence.translate(string.maketrans("",""), string.punctuation))

def apostrophe_rem(sentence):
	return(sentence.replace("'",""))

def url_rem(sentence):
	sentence = re.sub(r"(?:\@|https?\://|www)\S+", "", sentence)
	return(sentence)

from HTMLParser import HTMLParser
def html_char(sentence):
	html_parse = HTMLParser()
	return(html_parse.unescape(sentence))

def html_clean(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext

def decoder(sentence):
	return(sentence.decode('utf8').encode('ascii','ignore'))

def stopword_rem(sentence):
	inbuilt_stopwords = stopwords.words("english")
	sent = [word for word in sentence.split() if word not in inbuilt_stopwords]
	return(sent)

def word_tokenizer(sentence):		# Example:
	tokens = word_tokenize(sent)	# "This is a sentence"
	return tokens					# ["This", "is", "a", "sentence"]

def pos_tag(sentence):				# Example:
	yolo = word_tokenizer(sent)		# "I am walking the dog"
	return nltk.pos_tag(yolo)		# [["I", NNP], ["am", NNP], ["walking", VBD]]

# Example:
# walking walks communities
# walk walk community
# run ran
# run ran
def stem_words(sentence):
	stemmed_wnl = []
	wnl = WordNetLemmatizer()
	tokens = word_tokenizer(sentence)
	pos_list = np.array(pos_tag(sentence))
	length = len(tokens)
	pos_array = []
	adj_array = ["JJ", "JJR", "JJS"]
	noun_array = ["NN", "NNP", "NNS", "NNPS"]
	verb_array = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
	adv_array = ["RB", "RBR", "RBS", "RP"]
	for x in xrange(0,length):
		pos_array.append(pos_list[x][1])
	for x in xrange(0,length):
		if pos_array[x] in adj_array:
			stemmed_wnl.append(wnl.lemmatize(tokens[x], wn.ADJ))
		elif pos_array[x] in noun_array:
			stemmed_wnl.append(wnl.lemmatize(tokens[x], wn.NOUN))
		elif pos_array[x] in verb_array:
			stemmed_wnl.append(wnl.lemmatize(tokens[x], wn.VERB))
		elif pos_array[x] in adv_array:
			stemmed_wnl.append(wnl.lemmatize(tokens[x], wn.ADV))
	return stemmed_wnl

if filetype == 'txt':
	read_txt(filename)
elif filetype == 'json':
	read_json(filename)
elif filetype == 'xml':
	read_xml(filename)
elif filetype == 'rss':
	read_rss(filename)
elif filetype == 'csv':
	read_csv(filename)
