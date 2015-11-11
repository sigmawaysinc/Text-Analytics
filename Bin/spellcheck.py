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
	return sent

def read_txt_file(file_name):
	read_filename = open(filename, 'r')
	return read_filename.read().splitlines()

def strip_punc(sentence):
	return(sentence.translate(string.maketrans("",""), string.punctuation))

from HTMLParser import HTMLParser
def apostrophe_rem(sentence):
	return(sentence.replace(string.punctuation[6],""))

def url_rem(sentence):
	sentence = re.sub(r"(?:\@|https?\://|www)\S+", "", sentence)
	return(sentence)

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
	pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
	sent = pattern.sub('', sentence)
	return sent

if filetype == 'txt':
	file_name = read_txt_file(filename)
	file_name = " ".join(file_name)
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
apos_rem = config.get('Cleanser', 'Remove Apostrophes')
punc = config.get('Cleanser', 'Remove Punctuation')
h_char = config.get('Cleanser', 'Convert Escape Characters')
htag = config.get('Cleanser', 'Remove HTML Tags')

func_list = [decode, htag, h_char, url, stop_rem, punc, apos_rem]
clean_list = [decoder, html_clean, html_char, url_rem, stopword_rem, strip_punc, apostrophe_rem]
for x in xrange(0,len(func_list)):
	if func_list[x] == 'True':
		file_name = clean_list[x](file_name)
apos = string.punctuation[6]
print apos
output_file = open(output_file, 'w')
print >> output_file, file_name
output_file.close()