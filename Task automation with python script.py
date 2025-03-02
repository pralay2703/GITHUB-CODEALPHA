import os
import shutil

def organize_files(directory):
    # Define the file type categories and their corresponding folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
    }

    # Create folders for each file type if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Check the file extension and move the file
        moved = False
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(directory, folder, filename))
                moved = True
                print(f'Moved: {filename} to {folder}')
                break
        
        if not moved:
            print(f'No category found for: {filename}')

if __name__ == "__main__":
    # Specify the directory you want to organize
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files(target_directory)