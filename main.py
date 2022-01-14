import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.chrome.options import Options

s = Service("C:/bin/chromedriver.exe")
driver = webdriver.Chrome()
executable_path = "/webdrivers"
chrome_options = Options()
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options.add_extension('chropath.crx')

driver = webdriver.Chrome(chrome_options=chrome_options)

def main():
    for f in range(215):
        for i in range(20):
            if i == 0:
                continue
            driver.get(f"https://rus-massage.com/?page={f}")
            time.sleep(3)
            try:
                link1 = driver.find_element(By.XPATH, "//button[@id='age-limit-success-btn']")
                link1.click()
            except:
                pass
            time.sleep(3)
            try:
                link2 = driver.find_element(By.XPATH, f"//body/div[@id='main-content']/div[1]/div[1]/div[3]/div[2]/div[{i}]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]")
                link2.click()
                time.sleep(6)
                driver.window_handles
                driver.switch_to.window(driver.window_handles[-1])
                link3 = driver.find_element(By.XPATH, "//button[@id='show-phone']")
                link3.click()
                time.sleep(1)
                link4 = driver.find_element(By.XPATH, "//a[@id='profile-phone']")
                text = link4.get_attribute("href")
                print(text)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
            except:
                pass

main()