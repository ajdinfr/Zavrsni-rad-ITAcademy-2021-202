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

oprema = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a").click()
time.sleep(1)
tip_opreme = driver.find_element(By.ID,"type_id").click()
odabir = driver.find_element(By.CSS_SELECTOR,"#type_id > option:nth-child(28)").click()
proizvodjac_opreme = driver.find_element(By.ID,"producer_id").click()
odabir_prozvodjaca = driver.find_element(By.CSS_SELECTOR,"#producer_id > option:nth-child(24)").click()
inventurni_broj = driver.find_element(By.CSS_SELECTOR,"#wrapper > main > section.section-one > div.section-one-left > form > input[type=text]:nth-child(4)").send_keys("Selenium test")
serijski_broj = driver.find_element(By.CSS_SELECTOR,"#wrapper > main > section.section-one > div.section-one-left > form > input[type=text]:nth-child(5)").send_keys("Selenium test")

sacuvaj = driver.find_element(By.CSS_SELECTOR,"#wrapper > main > section.section-one > div.section-one-left > form > input.button.blue").click()

driver.close()
