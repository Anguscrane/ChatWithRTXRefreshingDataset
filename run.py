import subprocess
import threading

def run_app():
    subprocess.Popen(["python", "app.py"])

def run_refresh_script():
    subprocess.Popen(["python", "refresh_script_runner.py"])

if __name__ == "__main__":
    app_thread = threading.Thread(target=run_app)
    refresh_thread = threading.Thread(target=run_refresh_script)

    app_thread.start()
    refresh_thread.start()

    app_thread.join()
    refresh_thread.join()