import json
from nltk.tokenize import sent_tokenize, word_tokenize
import codecs


def print_info(arg):
	print("Length:		{}".format(len(arg)))
	print("Type:		{}".format(type(arg)))
	print("Value:		{}".format(arg))

	return null

def need_to_be_altered(string):
	line_arr = [word for word in word_tokenize(string, "english")]

	if "@" in line_arr or "http" in line_arr or "https" in line_arr:
		return True
	else:
		return False

def remove_at(string):
	line_arr = [word for word in word_tokenize(string, "english")]

	while "@" in line_arr:
		del line_arr[line_arr.index("@") + 1]
		del line_arr[line_arr.index("@")]

	return_string = ""

	for word in line_arr:
		return_string += word + " "

	return return_string

def remove_links(string):
	line_arr = [word for word in word_tokenize(string, "english")]

	while "http" in line_arr:
		del line_arr[line_arr.index("http") + 2]
		del line_arr[line_arr.index("http") + 1]
		del line_arr[line_arr.index("http")]

	while "https" in line_arr:
 		del line_arr[line_arr.index("https") + 2]
 		del line_arr[line_arr.index("https") + 1]
 		del line_arr[line_arr.index("https")]


	return_string = ""
	for word in line_arr:
		return_string += word + " "

	return return_string

def alter(string):
	text = string

	text = remove_at(text)
	text = remove_links(text)

	return text

data_neg = open("twitter_samples/negative_tweets.json", "r")
data_pos = open("twitter_samples/positive_tweets.json", "r")

# Make negative_tweets.txt
negative_tweets = codecs.open("twitter_samples/negative_tweets.txt", "w", "utf-8")

for line in data_neg:
	text = json.loads(line)["text"]

	if need_to_be_altered(text):
		text = alter(text)

	try:
		negative_tweets.write(text + "\n")
	except:
		pass

negative_tweets.close()

# Make positive_tweets.txt
positive_tweets = codecs.open("twitter_samples/positive_tweets.txt", "w", "utf-8")

for line in data_pos:
	text = json.loads(line)["text"]

	if need_to_be_altered(text):
		text = alter(text)

	try:
		positive_tweets.write(text + "\n")
	except:
		pass

positive_tweets.close()


