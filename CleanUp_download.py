import os
import shutil
import time

# Set path to Downloads folder
downloads_folder = "~/Downloads"

# Expand ~ to full path
downloads_folder = os.path.expanduser(downloads_folder)

# Set path to To_delete folder
to_delete_folder = "~/To_delete"

# Expand ~ to full path
to_delete_folder = os.path.expanduser(to_delete_folder)

# Set threshold for file age (in seconds)
age_threshold = 30 * 24 * 60 * 60  # 30 days

# Check if To_delete folder exists, and create it if it doesn't
if not os.path.exists(to_delete_folder):
    os.makedirs(to_delete_folder)

# Iterate over all files in Downloads foldercd ...
for filename in os.listdir(downloads_folder):
    filepath = os.path.join(downloads_folder, filename)
    # Check if file is older than age_threshold
    if time.time() - os.path.getmtime(filepath) > age_threshold:
        # Move file to To_delete folder
        shutil.move(filepath, os.path.join(to_delete_folder, filename))
        print(f"Moved {filename} to To_delete folder.")
