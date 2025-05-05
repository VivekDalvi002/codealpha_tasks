import os
import shutil

# Define source directory and destination folders
source_dir = "C:/Users/YourUsername/Downloads"  # Change to your desired path
destination_dirs = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Others": []  # Catch-all folder for files without a defined type
}

# Create destination directories if they don’t exist
for folder in destination_dirs.keys():
    os.makedirs(os.path.join(source_dir, folder), exist_ok=True)

# Move files based on their extensions
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in destination_dirs.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(source_dir, folder, filename))
                moved = True
                break
        if not moved:  # Move files that don’t fit into existing categories
            shutil.move(file_path, os.path.join(source_dir, "Others", filename))

print("Files have been organized successfully!")
