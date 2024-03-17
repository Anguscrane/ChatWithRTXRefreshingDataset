from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import schedule
import time
import os

def scrape_and_save_visible_text(url, file_name):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    chrome_options.add_argument("--log-level=3")  # Reduce logging level
    chrome_options.add_argument("--ignore-ssl-errors=true")  # Ignore SSL errors
    chrome_options.add_argument("--ssl-protocol=TLSv1.2")  # Force TLS 1.2 protocol
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Disable verbose logging

    # Launch Chrome with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the website
    driver.get(url)

    # Wait for the page to fully load (adjust the delay as needed)
    time.sleep(5)

    # Get the visible text on the page
    body = driver.find_element(By.TAG_NAME, "body")
    visible_text = body.text

    # Get username
    username = os.environ.get('USERNAME')

    # Construct the file path and name
    file_path = fr"C:\Users\{username}\AppData\Local\NVIDIA\ChatWithRTX\RAG\trt-llm-rag-windows-main\dataset"
    file_path_and_name = os.path.join(file_path, f"{file_name}.txt")

    # Write the visible text to a file
    with open(file_path_and_name, "w", encoding="utf-8") as file:
        file.write(visible_text)

    print(f"Visible text saved to {file_path_and_name}")

    # Close the browser
    driver.quit()

def main():
    # List of websites
    websites = [
        "https://weather.com/weather/tenday/l/3853b5a1e1f11d964eac6711e835a2b9365b755f45a46490e815cfbcdc5d98b5",
        "https://weather.com/weather/today/l/3853b5a1e1f11d964eac6711e835a2b9365b755f45a46490e815cfbcdc5d98b5",
        "https://weather.com/weather/hourbyhour/l/3853b5a1e1f11d964eac6711e835a2b9365b755f45a46490e815cfbcdc5d98b5",
        "https://www.nytimes.com",
        "https://www.bbc.com",
        "https://www.cnn.com",
        "https://www.theguardian.com/us",
        "https://www.washingtonpost.com",
        "https://www.nasa.gov",
        "https://www.whitehouse.gov",
        "https://www.cdc.gov",
        "https://arstechnica.com",
        "https://www.engadget.com",
        "https://techcrunch.com",
        "https://www.wired.com",
        "https://www.scientificamerican.com",
        "https://www.reuters.com",
        "https://www.npr.org",
        "https://www.foxnews.com",
        "https://www.wsj.com",
        "https://www.latimes.com",
        "https://www.chicagotribune.com",
        "https://www.sciencedaily.com",
        "https://www.nature.com",
        "https://www.space.com",
        "https://www.popsci.com",
        "https://www.popularmechanics.com",
        "https://www.forbes.com",
        "https://www.bloomberg.com",
        "https://www.cnbc.com",
        "https://www.economist.com",
        "https://www.ft.com",
        "https://www.mayoclinic.org",
        "https://www.webmd.com",
        "https://www.health.harvard.edu",
        "https://www.cdc.gov/healthliteracy",
        "https://www.nih.gov",
        "https://apnews.com",
        "https://time.com",
        "https://www.nbcnews.com",
        "https://www.usatoday.com/sports/",
        "https://theathletic.com",
        "https://www.espn.com",
        "https://www.sportingnews.com/us"
    ]

    # List of file names
    file_names = ["Weather_10_Day", "Weather_Today", "Weather_Hourly", "NYT",
                "BBC", "CNN", "TheGuardian_US", "WashingtonPost", "NASA", "WhiteHouse",
                "CDC", "ArsTechnica", "Engadget", "TechCrunch", "Wired", "ScientificAmerican", "Reuters",
                "NPR", "FoxNews", "WSJ", "LATimes", "ChicagoTribune", "ScienceDaily", "Nature", "Space",
                "PopSci", "PopularMechanics", "Forbes", "Bloomberg", "CNBC", "Economist", "FT", "MayoClinic",
                "WebMD", "HarvardHealth", "CDCHealthLiteracy", "NIH", "APNews", "Time", "NBCNews", "USATodaySports",
                "TheAthletic", "ESPN", "SportingNews"]

    # Run the scraping process immediately when the script is launched
    for url, file_name in zip(websites, file_names):
        scrape_and_save_visible_text(url, file_name)

    # Schedule the function to run every hour for each website and file name
    for url, file_name in zip(websites, file_names):
        schedule.every().hour.do(scrape_and_save_visible_text, url, file_name)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()