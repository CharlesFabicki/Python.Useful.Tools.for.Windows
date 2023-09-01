# Automated Browser Cleaner

Automated Browser Cleaner is a Python script designed to automate the process of clearing cache for popular web browsers, emptying the recycle bin, and removing temporary files on Windows systems.

## Features

- Clears cache for Chrome, Firefox, and Edge browsers.
- Empties the system's recycle bin.
- Removes temporary files from the user's temporary directory.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Windows operating system.

### Usage

1. Clone this repository or download the `cleaner.py` script.
2. Open a command prompt and navigate to the directory containing the `cleaner.py` script.
3. Run the script using the following command:

    ```
    python cleaner.py
    ```

4. The script will prompt you to press Enter to exit after completing the cleaning process.

## Customization

- You can modify the browser paths in the `browser_paths` dictionary within the script to match your system's installation paths.
- If you want to exclude certain browsers or add more, update the `browser_paths` accordingly.

## Caution

- Make sure you understand the consequences of running this script, as it will delete cache, recycle bin contents, and temporary files permanently.
- Review and modify the script according to your preferences before executing it.

## License

This project is licensed under the License

## Acknowledgments

This script was inspired by the need for an automated way to keep the system clean and free up disk space.

