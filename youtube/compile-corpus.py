import nltk
import json
import os

RESULTS_DIR = "results/"

for file in os.listdir("results/"):
	if file.endswith(".json"):

		f = open(RESULTS_DIR + file)
		transcript_data = json.load(f)
		transcript_text = " ".join(transcript_data["transcript"])

		tokens = nltk.word_tokenize(transcript_text, language='german')


		for token in tokens:
			print(token)