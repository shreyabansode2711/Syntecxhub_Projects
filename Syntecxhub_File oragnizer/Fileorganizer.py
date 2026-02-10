
import os
import shutil
from datetime import datetime

SOURCE_FOLDER = "test_folder"
DRY_RUN = True
LOG_FILE = "organizer_log.txt"


def write_log(message):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {message}\n")


def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Source folder does not exist.")
        return

    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isfile(file_path):
            extension = filename.split(".")[-1]
            target_folder = os.path.join(SOURCE_FOLDER, extension)

            if not os.path.exists(target_folder):
                if not DRY_RUN:
                    os.mkdir(target_folder)

            target_path = os.path.join(target_folder, filename)

            if DRY_RUN:
                print("Would move:", filename, "->", target_folder)
            else:
                shutil.move(file_path, target_path)
                write_log(f"Moved {filename} to {target_folder}")

    print("File organization completed.")


organize_files()