from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Bot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome("storage/chromedriver")
        self.wait_driver = WebDriverWait(self.driver, timeout=10)

    def search_on_youtube(self, query):
        self.driver.get("https://youtube.com")

        self.wait_driver.until(EC.presence_of_all_elements_located(By.ID, "search"))

    def close(self):
        self.driver.close()


# def hello_world():
#     driver = webdriver.Chrome("storage/chromedriver")
#     wait_driver = WebDriverWait(driver, timeout=10)
#     driver.get("https://youtube.com")

#     search_box = driver.find_element(By.ID, "search")
#     search_box.send_keys("Messi chiquito")
#     search_box.send_keys(Keys.RETURN)

#     time.sleep(10)
#     driver.close()
