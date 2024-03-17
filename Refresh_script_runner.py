import subprocess
import threading

def run_site_scrape_script():
    subprocess.call(["python", "Scrape.py"])

def run_refresh_script():
    run_site_scrape_script()

refresh_thread = threading.Thread(target=run_refresh_script)
refresh_thread.start()