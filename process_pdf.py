from pdfminer.high_level import extract_text
import os

dir = './corpus'
target_dir = './processed_corpus'

for filename in os.listdir(dir):
        new_file_name = filename.replace(".pdf", ".txt").replace("'", "_").replace(" ", "_")

        if new_file_name in os.listdir(target_dir):
            print(f"{filename} already found in target directory, skipping.")
            continue

        print(f"Processing {filename}")
        try:
            text = extract_text(os.path.join(dir, filename))                        
            with open(os.path.join(target_dir, new_file_name), "w") as target_file:
                target_file.write(text)
            print("Succes!")

        except:
            print(f"Error in {filename}, skipping")    

    