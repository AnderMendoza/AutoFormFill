# Importamos las librerias necesarias
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el webdriver de chrome
driver = webdriver.Chrome(executable_path="./chromedriver-win64/chromedriver.exe")

# Bucle infinito en el caso quieras dejar el programa corriendo
# Si no, puedes eliminar el bucle y dejar solo el código de abajo para que se ejecute una sola vez
while True:
    # Abre el formulario
    driver.get("https://docs.google.com/forms/") # Coloca el link de tu formulario

    # Encuentra las opciones de tu pregunta
    options = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="TEXTO"]') # Coloca el TEXTO de tu pregunta, si tienes mas de una pregunta, copia y pega ese fragmento de codigo y separalos con una "," y cambia el TEXTO

    # Itera y selecciona una respuesta aleatoria
    random.choice(options).click()
    time.sleep(1)

    # Aqui podrias copiar y pegar el codigo de arriba para responder mas preguntas
    # Solo cambia el TEXTO de la pregunta y el nombre de la variable "options
    # ...

    # Envía el formulario
    submit_button = driver.find_element(By.CSS_SELECTOR, 'ID > div.ID.ID > div > div.ID > div > div.ID > div > span > span') # Este es solo un ejemplo todo formulario tiene un selector diferente, para encontrarlo, inspecciona el boton de enviar y busca el selector de ese boton para luego reemplazarlo por el "ID"
    submit_button.click()

    # Refresca la página
    driver.refresh()

# Cierra el navegador en el caso de que no hayas usado el bucle
driver.quit()