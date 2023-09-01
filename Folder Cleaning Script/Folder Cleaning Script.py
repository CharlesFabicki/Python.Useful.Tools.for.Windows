import os
import time


def clean_folder(folder_path, max_age_days=30, delete_empty=True):
    now = time.time()

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_age_days = (now - os.path.getmtime(file_path)) / (24 * 3600)

            if file_age_days > max_age_days:
                os.remove(file_path)
                print(f"Deleted: {file_path}")

        if delete_empty and not os.listdir(root):
            os.rmdir(root)
            print(f"Deleted empty folder: {root}")


if __name__ == "__main__":
    folders_to_clean = [
        "/path/to/folder/1",
        "/path/to/folder/2",
        # Add more folders to clean
    ]

    for folder in folders_to_clean:
        clean_folder(folder)
