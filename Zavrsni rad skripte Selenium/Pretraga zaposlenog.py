from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
print("Upisite ime ili prezime zaposlenog: ")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://puppies-closet.com/evidencija/login.php")
korisnicko_ime = driver.find_element(By.NAME, "username").send_keys("ajdinfranca")
password = driver.find_element(By.NAME, "password").send_keys("ajdinfranca123")
login_button = driver.find_element(By.NAME, "login").click()
driver.implicitly_wait(20)
zaposleni = driver.find_element(By.NAME,"search").send_keys(input("").lower())
time.sleep(3)
zaposlenii = driver.find_element(By.NAME,"employeesSearch").click()
time.sleep(3)
izmjena_podataka = driver.find_element(By.CSS_SELECTOR,"#results > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > button.button.blue").click()
y = driver.find_element(By.CSS_SELECTOR,"#modalequipment > div > div.table > form > div > input.button.blue")
print("Ako zelite da stampate revers zaduzenja odaberite opremu!")
z = input("Da li zelite štampate revers zaduzenja? y/n ")
if z == "y":
    y.click()
    print("Uspješno ste odstampali revers zaduzenja")
    if z == "n":
        driver.close()

driver.close()


