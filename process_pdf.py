from pdfminer.high_level import extract_text
import os

dir = './corpus'
target_dir = './processed_corpus'

for filename in os.listdir(dir):
    text = extract_text(os.path.join(dir, filename))
    
    with open(os.path.join(target_dir, filename.replace("pdf", "txt")), "w") as target_file:
        target_file.write(text)
