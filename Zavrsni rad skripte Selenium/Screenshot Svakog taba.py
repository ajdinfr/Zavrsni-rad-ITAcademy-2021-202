from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://puppies-closet.com/evidencija/login.php")
driver. get_screenshot_as_file("screenshot1.png")
korisnicko_ime = driver.find_element(By.NAME, "username").send_keys("ajdinfranca")
password = driver.find_element(By.NAME, "password").send_keys("ajdinfranca123")
login_button = driver.find_element(By.NAME, "login").click()
driver. get_screenshot_as_file("screenshot2.png")
driver.implicitly_wait(20)
oprema = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a").click()
driver. get_screenshot_as_file("screenshot3.png")
time.sleep(1)
izvjestaj = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(3) > a").click()
driver. get_screenshot_as_file("screenshot4.png")
time.sleep(1)
tip_opreme = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(4) > a").click()
driver. get_screenshot_as_file("screenshot5.png")
time.sleep(1)
kancelarija = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(5) > a").click()
driver. get_screenshot_as_file("screenshot6.png")
time.sleep(1)
administracija = driver.find_element(By.CSS_SELECTOR,"#wrapper > header > nav > ul:nth-child(1) > li:nth-child(6) > a").click()
driver. get_screenshot_as_file("screenshot7.png")

driver.quit()

