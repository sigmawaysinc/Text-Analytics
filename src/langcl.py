import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files as lf
from sklearn.naive_bayes import MultinomialNB
import random
import statistics
'''
This language classifier supports the following languages:
German
English
French
Italian
Portugese

The classifier used is a Multinomial Naive Bayes classifier
'''
files = lf('/Users/Prakruti/desktop/Languages/Train', load_content = True, random_state = random.randint(0,50), categories = None)
lang_dict = {0:"German", 1:"English", 2:"Spanish",3: "French", 4: "Italian", 5:"Portugese"}

#cv = CountVectorizer(decode_error = 'ignore',lowercase=True, preprocessor=None, tokenizer=None, stop_words=None, token_pattern='(?u)\b\w\w+\b', ngram_range=(1, 3), analyzer='char_wb')
#train_counts = cv.fit_transform(files.data)

tf_vec = TfidfVectorizer(decode_error = 'ignore', lowercase = True, analyzer = 'char_wb', ngram_range = (1,3), strip_accents = 'unicode')
train_tf = tf_vec.fit_transform(files.data)

clf = MultinomialNB().fit(train_tf,files.target)

filename = "/Users/Prakruti/desktop/Languages/Test/de/de.txt"

test = ["This is a sentence to test", "Check this sentence", "Je m'apelle Prakruti", "Ich bin ein Berliner", "donde esta la biblioteca"]
def read_txt_file(file_name):
	read_filename = open(filename, 'r')
	return read_filename.read().splitlines()
test_file = read_txt_file(filename)
test_vec = tf_vec.transform(test_file)

array = clf.predict(test_vec).tolist()

print statistics.mode(array)
