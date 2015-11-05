import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
import numpy as np
import ConfigParser
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

config = ConfigParser.ConfigParser()

config.read('text_config.ini')
filename = config.get('File functions', 'Input File Path')
filetype = config.get('File functions', 'Input File Format')
if_spell = config.get('File functions', 'Stem')

def read_txt_file(file_name):
	read_filename = open(filename, 'r')
	read_filename = read_filename.read().decode('utf-8').encode('ascii','ignore').splitlines()
	return " ".join(read_filename)

def word_tokenizer(sentence):
	return word_tokenize(sentence)

def sent_tokenizer(sentence):
	return sent_tokenize(sentence)

def pos_tag(sentence):
	return nltk.pos_tag(word_tokenizer(sentence))

def stem_words():
	sentence = read_txt_file(filename)
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

print stem_words()
