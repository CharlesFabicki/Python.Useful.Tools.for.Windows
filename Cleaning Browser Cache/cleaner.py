import os
import shutil


def clear_browser_cache(browser_paths):
    for browser, path in browser_paths.items():
        print(f"Clearing cache for {browser}...")
        os.system(f'start "" "{path}" --incognito --clear-cache')
        print(f"Cache for {browser} cleared.")


def clear_recycle_bin():
    recycle_bin_path = "C:\\$Recycle.Bin"
    try:
        shutil.rmtree(recycle_bin_path)
        os.mkdir(recycle_bin_path)
        print("Recycle bin cleared.")
    except Exception as e:
        print("Error clearing recycle bin:", e)


def clear_temp_files():
    temp_path = os.environ.get("TEMP")
    try:
        for root, dirs, files in os.walk(temp_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        print("Temporary files cleared.")
    except Exception as e:
        print("Error clearing temporary files:", e)


if __name__ == "__main__":
    browser_paths = {
        "Chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "Firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
        "Edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    }

    clear_browser_cache(browser_paths)
    clear_recycle_bin()
    clear_temp_files()

    print("Task completed.")
    input("Press Enter to exit.")
