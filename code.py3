from PIL import Image
import pytesseract
import os

test_images_dir = "test_images/"

for file in sorted(os.listdir(test_images_dir)):
	path = test_images_dir + file 
	print(path)
	text = pytesseract.image_to_string(Image.open(path), lang="deu")

	lines = text.splitlines()

	for line in lines:
		if line.strip():
			print("    " + line)		

	# text = text.replace("\n\n", "")
	# print("    " + text.replace("\n", "/"))
	print("")

