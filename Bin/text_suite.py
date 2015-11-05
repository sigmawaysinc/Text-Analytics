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


def read_txt_table():
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

def read_txt_file(file_name):
	read_filename = open(filename, 'r')
	return read_filename.read()

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

if filetype == 'txt':
	file_name = read_txt_file(filename)
elif filetype == 'json':
	file_name = read_json(filename)
elif filetype == 'xml':
	file_name = read_xml(filename)
elif filetype == 'rss':
	file_name = read_rss(filename)
elif filetype == 'csv':
	file_name = read_csv(filename)

decode = config.get('Cleanser', 'Decode Text')
url = config.get('Cleanser', 'Remove URL')
stop_rem = config.get('Cleanser', 'Remove Stopwords')
sent_tok = config.get('Cleanser', 'Tokenize Sentences')
apos_rem = config.get('Cleanser', 'Remove Apostrophes')
punc = config.get('Cleanser', 'Remove Punctuation')
h_char = config.get('Cleanser', 'Convert Escape Characters')
htag = config.get('Cleanser', 'Remove HTML Tags')

file_name = sent_tokenizer(file_name)
if decode == 'True':
	file_name = decoder(file_name)
if htag == 'True':
	file_name = html_clean(file_name)
if h_char == 'True':
	file_name = html_char(file_name)
if url == 'True':
	file_name = url_rem(file_name)
if punc == 'True':
	file_name = strip_punc(file_name)
if stop_rem == 'True':
	file_name = stopword_rem(file_name)
if apos_rem == 'True':
	file_name == apostrophe_rem(file_name)

print file_name