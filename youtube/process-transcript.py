import nltk
import json
import sys

transcript_input_file = sys.argv[1]
f = open(transcript_input_file)
transcript_data = json.load(f)
transcript_text = " ".join(transcript_data["transcript"])

tokens = nltk.word_tokenize(transcript_text, language='german')


for token in tokens:
	print(token)