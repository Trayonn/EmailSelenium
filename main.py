from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

options = Options()


profile_path = r"CAMINHO DO SEU PERFIL DO NAVEGADOR"


options.profile = profile_path

gecko_driver_path = r"CAMINHO DO GECKODRIVER, OU DO CHROMEDRIVER E ETC"  # Substitua pelo caminho correto

service = Service(gecko_driver_path)
driver = webdriver.Firefox(options=options, service=service)

driver.get("https://mail.google.com/mail/u/0/#inbox")

time.sleep(3)


search_box1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Compose']"))
)
search_box1.click()


assunto_email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "subjectbox"))
)
assunto_email.click()

assunto_email.send_keys("Teste de Automatização Via Selenium")


mensagem_email = driver.find_element(By.XPATH, "//div[@aria-label='Message Body']")

mensagem_email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message Body']"))
)

mensagem_email.click()

mensagem_email.send_keys("Este e-mail foi escrito via automatização, utilizando Selenium.")

destinatario_email = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Recipients']"))
)

destinatario_email.click()

destinatario_email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@aria-label='To recipients']"))
)

destinatario_email_input.click()
destinatario_email_input.send_keys("TESte@gmail.com") #Insira o e-mail do destinatario
destinatario_email_input.send_keys(Keys.TAB)
destinatario_email_input.send_keys(Keys.LEFT_CONTROL, Keys.ENTER)

driver.quit()
