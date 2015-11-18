import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
import numpy as np
import ConfigParser
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
'''
Stemming is a tool used to perform important tasks like term frequency count and is

critical in optimization of code in the fields of information retrieval and domain analysis.

The algorithm is run from Python's natural language toolkit (NLTK), and uses the Princeton

Wordnet library to search for inflected and root forms. We tag the parts of speech before

running the stemming/lemmatization process in order for the program to figure out which word

has to be stemmed in the case of one word being used in different parts of speech.

For example: "The running man ran a race" would be stemmed to "The running man run a race",

where only the word ran would be stemmed.
'''

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
