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


ime = driver.find_element(By.NAME,"firstname").send_keys("Selenium")
prezime = driver.find_element(By.NAME,"lastname").send_keys("User")
email = driver.find_element(By.NAME,"email").send_keys("selenium.user2022@gmail.com")
broj_telefona = driver.find_element(By.NAME,"phone").send_keys("111 222 333")
kancelarija = driver.find_element(By.NAME,"office_id").click()
br = driver.find_element(By.CSS_SELECTOR,"#office_id > option:nth-child(8)").click()
time.sleep(1)
organizaciona_jedinica = driver.find_element(By.NAME,"organization_id").click()
time.sleep(1)
brojorg = driver.find_element(By.CSS_SELECTOR,"#organization_id > option:nth-child(6)").click()

sacuvaj_button = driver.find_element(By.NAME,"save").click()


driver.close()