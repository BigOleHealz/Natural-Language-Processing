'''
This script pre-processes all the data from the JSON.
 - Parses .json into .txt
 - Removes stop words
 - Stems words
'''

import json
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import codecs

data_neg = open("twitter_samples/negative_tweets.json", "r")
data_pos = open("twitter_samples/positive_tweets.json", "r")

negative_tweets = codecs.open("twitter_samples/negative_tweets.txt", "w", "utf-8")
positive_tweets = codecs.open("twitter_samples/positive_tweets.txt", "w", "utf-8")

stop_words = set(stopwords.words("english"))

ps = PorterStemmer()

def print_info(arg):
	print("Length:		{}".format(len(arg)))
	print("Type:		{}".format(type(arg)))
	print("Value:		{}".format(arg))

def list_to_string(array):
	return_string = ""

	for word in array:
		return_string += word + " "
	return return_string

def need_to_be_altered(array):
	if "@" in array or "http" in array or "https" in array:
		return True
	else:
		return False

def remove_at(array):
	while "@" in array:
		del array[array.index("@") + 1]
		del array[array.index("@")]

	return array

def remove_links(array):

	while "http" in array:
		del array[array.index("http") + 2]
		del array[array.index("http") + 1]
		del array[array.index("http")]

	while "https" in array:
 		del array[array.index("https") + 2]
 		del array[array.index("https") + 1]
 		del array[array.index("https")]

	return array

def remove_stop_words(array):
	filtered_array = [word for word in array if not word in stop_words]

	return filtered_array

def stem_words(array):
	stemmed_text = [ps.stem(word) for word in array]
	
	return stemmed_text

def alter(array):
	array = remove_at(array)
	array = remove_links(array)

	return array

def stop_words_and_stem(string):

	text = string
	text = remove_stop_words(text)
	text = list_to_string(text)
	return text

# Make negative_tweets.txt

def json_to_txt(file_name):
	json_file = open("twitter_samples/" + file_name + ".json", "r")
	tweets = codecs.open("twitter_samples/" + file_name + ".txt", "w", "utf-8")

	for line in json_file:
		text_arr = [word for word in word_tokenize(json.loads(line)["text"])]

		if need_to_be_altered(text_arr):
			text_arr = alter(text_arr)
		text_arr = remove_stop_words(text_arr)
		text_arr = stem_words(text_arr)

		print(list_to_string(text_arr))
		
		try:
			file_name.write(list_to_string(text_arr) + "\n")
		except:
			pass

	tweets.close()

json_to_txt("negative_tweets")
json_to_txt("positive_tweets")