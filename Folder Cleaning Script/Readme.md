## Folder Cleaning Script Instructions

**Purpose:** This script is designed to clean specified folders by removing files that meet a certain age criterion and optionally deleting empty folders.

### Age Criterion
The script calculates the age of each file in days, measured from the current time to the file's last modification time. If a file's age exceeds the specified maximum age (default: 30 days), the script deletes that file.

### Empty Folder Removal
The script also provides an option to remove empty folders. After deleting files, it checks each folder, and if it's empty, the script deletes the empty folder as well.

### Usage
1. Open the script file using a text editor.
2. Edit the `folders_to_clean` list to include the paths of the folders you want to clean.
3. Optional: Modify the `max_age_days` value to set the maximum age of files in days before they are deleted.
4. Optional: If you want to delete empty folders, keep `delete_empty` as `True`. Change it to `False` if you don't want to delete empty folders.
5. Run the script using a Python interpreter.

### Precautions
- Carefully review and understand the script before using it on real folders.
- Test the script on a safe set of data or create backups of folders you intend to clean.
- Deletion of files and folders is irreversible, so use the script cautiously.

### Execution
- Run the script by executing it with a Python interpreter (e.g., `Folder Cleaning Script.py`).
- The script will traverse through the specified folders, identify files older than the specified age, and delete them.
- If the `delete_empty` option is enabled, the script will also remove empty folders.

Remember that improper use of this script could result in data loss, so always exercise caution and ensure you fully understand its behavior before applying it to your folders.
