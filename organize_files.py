#CodeRunner
import os
import shutil

def organize_files(folder_path):
    # Create the necessary folders if they don't exist
    folders = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt']
    }

    for folder_name in folders:
        folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Organize files based on their extensions
    for filename in os.listdir(folder_path):
        if filename == 'organize_files.py':  # Exclude the script file itself
            continue

        file_extension = os.path.splitext(filename)[1]

        for folder_name, extensions in folders.items():
            if file_extension in extensions:
                source_path = os.path.join(folder_path, filename)
                destination_path = os.path.join(folder_path, folder_name, filename)
                shutil.move(source_path, destination_path)
                break

    print("File organization completed.")

# Provide the folder path you want to organize
folder_path = './'
organize_files(folder_path)
