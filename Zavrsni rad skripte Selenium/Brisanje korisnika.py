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

administracija = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(6) > a").click()

pronalazak_usera = driver.find_element(By.CSS_SELECTOR,"#wrapper > div.section-two > div > table > tbody > tr:nth-child(26) > td:nth-child(6) > button.button.red").click()

brisanje_korsinika = driver.find_element(By.ID,"del").click()

driver.quit()
