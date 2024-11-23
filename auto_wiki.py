#AUTHOR: Martin C. Bildhjerd

##LIBS
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager  
import time
import logging
###

##SETUP
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():     
    options = webdriver.ChromeOptions()  
    options.add_argument("--start-maximized")  
    options.add_argument("--disable-extensions")  
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    logging.info("WebDriver setup done")
    return driver  
###

##NAVIGATE TO WEBSITE
def enterwebb(driver):  
    driver.get("https://www.wikipedia.org/")  
    logging.info("Wiki was found")
###

##SEARCH FUNC
def search(driver, query):  
    search_box = driver.find_element(By.NAME, "search")  #FIND SEARCH BAR
    search_box.send_keys(query)
    search_box.submit()
    logging.info("Search was submitted")
###

##EXTRACT SUM
def get_summary_text(driver):  
    try:
        summary = driver.find_element(By.CSS_SELECTOR, "p")
        summary_text = summary.text
        logging.info("Summary text collected")
        print("\n")
        print(summary_text)
    except Exception as e:
        print(f"Could not find text: {e}")
        return None
###

##EXTRACT PIC
def image_extraction(driver):
    try:
        image = driver.find_element(By.CSS_SELECTOR, ".infobox img").get_attribute("src")
        print("\n")
        print(f"Attached pic: {image}")
    except Exception as e:
         logging.error(f"Could not extract picture: {e}")
         return None
###

##MAIN
def main():
    driver = setup_driver()  
    enterwebb(driver)
    time.sleep(2)
    search(driver, "Linköpings universitet")
    time.sleep(2)
    get_summary_text(driver)
    image_extraction(driver)
    time.sleep(2)
    driver.quit()
###

if __name__ == "__main__":  
    main()
