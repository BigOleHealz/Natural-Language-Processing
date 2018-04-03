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

stop_words = set(stopwords.words("english"))	# import most-used words that convey little intent

ps = PorterStemmer()	# So that we can stem words later (if we want)

def list_to_string(array):	# Converts array (list) of words to a string
	return_string = ""

	for word in array:
		return_string += word + " "
	return return_string	

def need_to_be_altered(array):	# Returns true only if the tweet contains a "@blahblah" or a link
	if "@" in array or "http" in array or "https" in array:
		return True
	else:
		return False

def remove_at(array):	# Removes "@blahblah"
	while "@" in array:
		del array[array.index("@") + 1]	# Removes "blahblah"
		del array[array.index("@")]	# Removes "@"

	return array

def remove_links(array):	# Removes any link starting with "http" or "https"

	while "http" in array:
		del array[array.index("http") + 2]	# Removes "//blahblah.com"
		del array[array.index("http") + 1]	# Removes ":"
		del array[array.index("http")]	# Removes "http"

	while "https" in array:
 		del array[array.index("https") + 2]	# Removes "//blahblah.com"
 		del array[array.index("https") + 1]	# Removes ":"
 		del array[array.index("https")]	# Removes "https"

	return array

def remove_stop_words(array):	# Removes most-used words that don't express much opinion like "and", "the", or "in"
	filtered_array = [word for word in array if not word in stop_words]

	return filtered_array

def stem_words(array):	# Finds root word of each word in array
	stemmed_text = [ps.stem(word) for word in array]
	
	return stemmed_text

def alter(array):	# Removes "@blahblah" and links
	array = remove_at(array)
	array = remove_links(array)

	return array

# Convert .json to .txt file
def json_to_txt(file_name):
	json_file = open("twitter_samples/" + file_name + ".json", "r")
	tweets = codecs.open("twitter_samples/" + file_name + ".txt", "w", "utf-8")

	for line in json_file:
		text_arr = [word for word in word_tokenize(json.loads(line)["text"])]	# Tokenize each string of words in the "text" field of the json and put the into an array (list)

		if need_to_be_altered(text_arr):	# Removes "@blahblah" and links if need-be
			text_arr = alter(text_arr)
		text_arr = remove_stop_words(text_arr)	# Removes stop words
		# text_arr = stem_words(text_arr)	# Stems all words in the array

		print(list_to_string(text_arr))
		
		try:
			tweets.write(list_to_string(text_arr) + "\n")	# Cast the list to a string and print it in the "write to" file
		except:
			pass

	tweets.close()

json_to_txt("negative_tweets")	# Make negative_tweets.txt
json_to_txt("positive_tweets")	# Make positive_tweets.txt