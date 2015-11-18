#textblob spell check
import enchant
import ConfigParser
import csv

'''
The spellchecker runs on a classic model of inserts, deletions and replaces.

This code runs with a combination of Peter Norvig's 21-line application and

the python Pattern library, with a customized dictionary.

The code is able to correct words from a file or sentence to its closest counterpart

using the Levenshtein edit distance. Further functionality will include suggestions of

the next five closest words, from which the user will be able to pick which works.
'''


config = ConfigParser.ConfigParser()

config.read('text_config.ini')
filename = config.get('File functions', 'Input File Path')
filetype = config.get('File functions', 'Input File Format')
if_spell = config.get('File functions', 'Check Spelling')
output_file = config.get('File functions','Output File')
def read_txt_file(file_name):
	read_filename = open(filename, 'r')
	read_filename = read_filename.read()
	return read_filename

def read_txt_table(file_name):
	inp = []
	with open(file_name, 'rU') as g:
		reader = csv.reader(g,delimiter = '\t')
		sent = list(reader)
	for x,y in sent:
		inp.append(x)
	return inp

def read_csv(file_name):
	inp = []
	with open(file_name, 'rU') as g:
		reader = csv.reader(g,delimiter = ',')
		sent = list(reader)
	for x in sent:
		inp.append(x)
	return inp

def correction(file_name):
	d = enchant.Dict("en_US.dic")
	corr = []
	if filetype == 'txt':
		file_name = read_txt_file(file_name).split()
	elif filetype == 'tab':
		file_name = read_txt_table(file_name)
	elif filetype == 'csv':
		file_name = read_csv(file_name)
	output = []
	ctr = 0
	for item in file_name:
		if d.check(item):
			output.append(item)
		else:
			a = d.suggest(item)
			if len(a) > 0:
				output.append(a[0])
				ctr += 1  #Number of corrected words
			else:
				output.append(item)
	return output

file_name = " ".join(correction(filename))

output_file = open(output_file, 'w')

print >> output_file, file_name
output_file.close()
