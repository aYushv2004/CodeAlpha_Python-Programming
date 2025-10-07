import os
import shutil

source_folder = r"source_folder_path"
destination_folder = r"destination_folder_path"

# Make sure destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("✅ Done All .jpg files moved successfully!")