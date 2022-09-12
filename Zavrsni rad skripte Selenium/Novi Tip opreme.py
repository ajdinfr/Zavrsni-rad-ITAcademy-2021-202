import textwrap

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://puppies-closet.com/evidencija/login.php")

korisnicko_ime = driver.find_element(By.NAME, "username").send_keys("ajdinfranca")
password = driver.find_element(By.NAME, "password").send_keys("ajdinfranca123")
login_button = driver.find_element(By.NAME, "login").click()


tip = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(4) > a").click()
time.sleep(1)
pregled_izmjena_zipa_opreme = driver.find_element(By.CSS_SELECTOR,"#wrapper > div:nth-child(2) > div:nth-child(1) > label").click()
time.sleep(1)

unos_tipa_opreme = driver.find_element(By.CSS_SELECTOR,"#wrapper > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > form > input[type=text]:nth-child(2)").send_keys("selenium test")

sacuvaj = driver.find_element(By.NAME,"saveEquipType").click()


driver.quit()






