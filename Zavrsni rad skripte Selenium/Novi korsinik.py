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

time.sleep(1)
ime_korisnika = driver.find_element(By.CSS_SELECTOR,"#wrapper > div.section-one-left > form > input[type=text]:nth-child(2)").send_keys("Selenium user")
przime_korisnika = driver.find_element(By.CSS_SELECTOR,"#wrapper > div.section-one-left > form > input[type=text]:nth-child(3)").send_keys("Selenium user-prezime")
korisnicko_ime = driver.find_element(By.CSS_SELECTOR,"#wrapper > div.section-one-left > form > input[type=text]:nth-child(4)").send_keys("selenium korisnik")
korisnicka_lozinka = driver.find_element(By.CSS_SELECTOR,"#wrapper > div.section-one-left > form > input[type=password]:nth-child(5)").send_keys("selenium")
korisnik_admin = driver.find_element(By.ID,"role").click()
time.sleep(1)
korisnikk = driver.find_element(By.CSS_SELECTOR,"#role > option:nth-child(3)").click()
time.sleep(1)
sacuvaj = driver.find_element(By.CSS_SELECTOR,"#wrapper > div.section-one-left > form > input.button.blue").click()


driver.quit()


