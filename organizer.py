import os
import shutil

watch_folder = r"E:\automation_suite\input_files"
organized_folder = r"E:\automation_suite\organized_files"

file_types = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx"],
    "Videos": [".mp4"],
}

if not os.path.exists(organized_folder):
    os.makedirs(organized_folder)

for file in os.listdir(watch_folder):

    file_path = os.path.join(watch_folder, file)

    if os.path.isfile(file_path):

        ext = os.path.splitext(file)[1]

        for category in file_types:

            if ext in file_types[category]:

                dest_folder = os.path.join(
                    organized_folder,
                    category
                )

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                shutil.move(file_path,
                            dest_folder)