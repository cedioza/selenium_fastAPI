from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import json


def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    url = 'stake,betpaly,etoro'
    add_information = []

    urls = url.split(',')

    for url in urls:
            driver.get(f"https://www.google.com/search?q={url}")
            arrivals = driver.find_elements(By.XPATH, '//span[.="Patrocinado"]/following-sibling::div[1]')

            for arrival in arrivals:
                try:
                    url_ad = arrival.find_element(By.XPATH, './a')
                    keyword_ad = url_ad.find_element(By.XPATH, './/span[@class="OSrXXb"]')
                    add_information.append({
                        "keyword": url,
                        "keyword_ad": keyword_ad.text,
                        "url_ad": url_ad.get_attribute("href")
                    })
                except NoSuchElementException as e:
                    print("Elemento não encontrado:", e)

    driver.implicitly_wait(3)

    with open('ads_data.json', 'w') as file:
         json.dump(add_information, file, indent=4)


    # return driver.page_source
    return add_information

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")