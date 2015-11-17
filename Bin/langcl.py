import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files as lf
from sklearn.naive_bayes import MultinomialNB
import random

files = lf('/Users/psmehta/Desktop/Languages/Train', load_content = True, random_state = random.randint(0,50), categories = None)
lang_dict = {0:"German", 1:"English", 2:"Spanish",3: "French", 4: "Italian", 5:"Portugese"}

#cv = CountVectorizer(decode_error = 'ignore',lowercase=True, preprocessor=None, tokenizer=None, stop_words=None, token_pattern='(?u)\b\w\w+\b', ngram_range=(1, 3), analyzer='char_wb')
#train_counts = cv.fit_transform(files.data)

tf_vec = TfidfVectorizer(decode_error = 'ignore', lowercase = True, analyzer = 'char_wb', ngram_range = (1,6), strip_accents = 'unicode')
train_tf = tf_vec.fit_transform(files.data)

clf = MultinomialNB().fit(train_tf,files.target)

test = ["This is a sentence to test", "Check this sentence", "Je m'apelle Priyank", "Ich bin ein Berliner", "donde esta la biblioteca"]
test_files = lf('/Users/psmehta/Desktop/Languages/Test', load_content = True, categories = None)

test_vec2 = tf_vec.transform(test)
test_vec = tf_vec.transform(test_files.data)

predicted = clf.predict(test_vec)
predicted2 = clf.predict(test_vec2)

array = ['pt', 'es', 'en', 'fr', 'de', 'it']
array2 = ['en', 'en', 'fr', 'de', 'es']

for a, b in zip(array, predicted):
	print('%r => %s' % (a, files.target_names[b]))
for doc, category in zip(test, predicted2):
	print('%r => %s' % (doc, files.target_names[category]))