#textcleanser.py

import string
import re
from nltk.corpus import stopwords
import numpy as np
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('text_config.ini')
filename = config.get('File functions', 'Input File Path')
filetype = config.get('File functions', 'Input File Format')
output_file = config.get('File functions', 'Output File')
task_type = config.get('File functions', 'Type of Task')
if_cleanse = config.get('File functions', 'Cleanse')

def read_txt_file(file_name):
	read_filename = open(filename, 'r')
	return read_filename.read().splitlines()

def read_txt_file(file_name):
	read_filename = open(filename, 'r')
	return read_filename.read().splitlines()

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

def cleanse_txt():
	decode = config.get('Cleanser', 'Decode Text')
	url = config.get('Cleanser', 'Remove URL')
	stop_rem = config.get('Cleanser', 'Remove Stopwords')
	apos_rem = config.get('Cleanser', 'Remove Apostrophes')
	punc = config.get('Cleanser', 'Remove Punctuation')
	h_char = config.get('Cleanser', 'Convert Escape Characters')
	htag = config.get('Cleanser', 'Remove HTML Tags')
	file_name = read_txt_file(filename)
	if decode == 'True':
		for item in xrange(len(file_name)):
			file_name[item] = decoder(file_name[item])
	if htag == 'True':
		for item in xrange(len(file_name)):
			file_name[item] = html_clean(file_name[item])
	if h_char == 'True':
		for item in xrange(len(file_name)):
			file_name[item] = html_char(file_name[item])
	if url == 'True':
		for item in xrange(len(file_name)):
			file_name[item] = url_rem(file_name[item])
	if punc == 'True':
		for item in xrange(len(file_name)):
			file_name[item] = strip_punc(file_name[item])
	if stop_rem == 'True':
		for item in xrange(len(file_name)):
			file_name[item] = stopword_rem(file_name[item])
	if apos_rem == 'True':
		for item in xrange(len(file_name)):
			file_name[item] = apostrophe_rem(file_name[item])
	return file_name
print "\n".join(cleanse_txt())