import sys
import os
import random

folder_hash = random.getrandbits(16)

pdf_file = sys.argv[1]
concat = len(sys.argv)>=3

command_0 = f'mkdir {folder_hash}'
success = 0 == os.system(command_0)
if not success:
	sys.exit('Failed to create a directory')

command_1 = f'convert {pdf_file} -quality 80 ./{folder_hash}/out.png'
success = 0 == os.system(command_1)
if not success:
	sys.exit('Failed to run convert')

print("Scanned the pdf")

if(concat):
	print("Concatenating the images")
	pic_count = len([name for name in os.listdir(f'./{folder_hash}/')])

	filenames = ''
	for index in range(pic_count):
		filenames += f'./{folder_hash}/out-{index}.png '

	command = f'convert -append {filenames} ./{folder_hash}/pdfimage.png'
	success = 0 == (os.system(command)) 
	success = 0 == (os.system(f'rm ./{folder_hash}/out*')) 

print(f"Your output is in {folder_hash} folder")