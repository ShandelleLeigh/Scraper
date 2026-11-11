import re
import sys
from pathlib import Path
import os
import shutil
import fileinput


original_path = Path("scribed.html").resolve();

output_name = "parsed.html"
output_path = original_path.parent / output_name

def get_files_in_directory(directory: Path):

	files_array = []
	for f in directory.iterdir():

		if f.is_file()\
		and f.suffix.lower() in ['.html', '.htm']\
			and not f.match('*.txt*'):
			files_array.append(f)

	return files_array


pattern_1 = r'<div class="page-number">(\d+)</div>'
replacement_1 = r'<div class="page-number" id="page-\1">\1</div>'

def modify_html(file_content: str) -> str:
	modified_line: str = re.sub(pattern_1, replacement_1, file_content)
	return modified_line


def process_html():


	with open(original_path, 'r', encoding='utf-8') as f:
		file_content = f.read()

	modified_content = modify_html(file_content)
		# modified_line: str = re.sub(pattern_1, replacement_1, file_content)
	# sys.stdout.write(modified_line)

	with open(output_path, 'w', encoding='utf-8') as f:
		f.write(modified_content)


def files_function():
	files = get_files_in_directory(original_path.parent)
	for file in files:
		print(f"Found file: {file.name}")
		process_html()

if __name__ == "__main__":
	files_function()
