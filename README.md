# RTX Chat WebUI Data Refresher

This project is designed to continuously refresh the dataset used by the NVIDIA RTX Chat WebUI application. It automatically scrapes visible text from a predefined list of websites and updates the dataset with the new information.

## Installation

### Prerequisites

- Python 3.6 or later
- Google Chrome browser installed

### Setup

1. Clone this repository or download the source code.
2. Install the required Python packages by running:

```
pip install selenium schedule
```

3. Download the appropriate ChromeDriver for your system from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory.

## Usage

1. Open the `Scrape.py` file and modify the `websites` and `file_names` lists to include the URLs and file names you want to scrape and save, respectively.

2. Run the `app_launch.bat` file. This will set up the required environment, verify the installation, and start the scraping and refreshing processes.

The script will initially scrape the visible text from the specified websites and save it to individual text files in the `AppData\Local\NVIDIA\ChatWithRTX\RAG\trt-llm-rag-windows-main\dataset` directory. After the initial scrape, the script will continue to refresh the dataset every hour by scraping the websites again and updating the corresponding text files.

## File Structure

- `Scrape.py`: This file contains the main scraping functionality. It uses Selenium to scrape visible text from a list of websites and saves it to individual text files.
- `run.py`: This file runs two separate processes: the main application (`app.py`) and the refresh script (`refresh_script_runner.py`).
- `refresh_script_runner.py`: This file runs the `Scrape.py` script periodically (every hour) to refresh the dataset.
- `app_launch.bat`: This batch file sets up the required environment, verifies the installation, and runs the `run.py` script.
