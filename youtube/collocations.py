import xml.etree.ElementTree as ET
import math
import sys

def log_dice(freq_target, freq_collocate, freq_co_occurrences):
	dice_coefficient = (2 * freq_co_occurrences) / (freq_target + freq_collocate)
	return 14 + math.log2(dice_coefficient)


current_ngram = []

if len(sys.argv) != 5:
	exit(1)

input_file = sys.argv[1]

window_left  = int(sys.argv[2])
window_right = int(sys.argv[3])

target_word = sys.argv[4]

n = window_left + window_right + 1
target_idx = window_left

freq = {}
cooccurrence_freq = {}

token_lines = open(input_file, "r").readlines()

for token_line in token_lines:
	token_line = token_line.rstrip()

	if not len(token_line):
		continue

	word = token_line


	if freq.get(word):
		freq[word] += 1
	else:
		freq[word] = 1


	if len(current_ngram) < n:
		current_ngram.append(word)
		continue


	current_ngram.pop(0)
	current_ngram.append(word)

	current_ngram_str = " ".join(current_ngram)

	target_position_word = current_ngram[target_idx]

	if target_position_word.lower() == target_word.lower():
		for word in current_ngram:
			if word != target_word:
				if cooccurrence_freq.get(word):
					cooccurrence_freq[word] += 1
				else:
					cooccurrence_freq[word] = 1

current_ngram = []


results = {}

for cooccurence in cooccurrence_freq.keys():
	ld = log_dice(freq[target_word], freq[cooccurence], cooccurrence_freq[cooccurence])
	results[cooccurence] = ld

sorted_results = sorted(results.items(), key=lambda item : item[1], reverse=True)

output_count = 0

print("collocate\tlog Dice")

for collocate, ld in sorted_results:
	if freq[collocate] < 2:
		continue

	output_count += 1

	# print(f"{collocate}\t{ld}\t{freq[collocate]}")
	print(f"{collocate}\t{ld}")

	if output_count == 70:
		break