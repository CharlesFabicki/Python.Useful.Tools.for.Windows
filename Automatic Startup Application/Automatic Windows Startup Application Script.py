import subprocess


def run_applications():
    try:
        # Add the full paths to the applications you want to run
        app1_path = r"C:\path\to\application1.exe"
        app2_path = r"C:\path\to\application2.exe"

        # Launch the applications using subprocess
        subprocess.Popen([app1_path], shell=True)
        subprocess.Popen([app2_path], shell=True)

        print("Applications have been launched.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    run_applications()
