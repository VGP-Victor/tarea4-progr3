import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
#inicio de pagina
browser.get('https://testpages.eviltester.com/styled/index.html')


#1- proceso de llenar un formulario con los datos personales 
titulopagina = browser.title
def historia1(browser):
    browser.find_element(By.ID, "inputvalidation").click()
    browser.find_element(By.ID, "firstname").click()
    browser.find_element(By.ID, "firstname").send_keys("adfsada")
    browser.find_element(By.ID, "surname").click()
    browser.find_element(By.ID, "surname").send_keys("sadasdasdasdasd")
    browser.find_element(By.ID, "age").click()
    browser.find_element(By.ID, "age").send_keys("18")
    browser.find_element(By.NAME, "userdata").click()
    browser.find_element(By.CSS_SELECTOR, "input:nth-child(31)").click()
    browser.save_screenshot("captura_de_pantalla1.png")
    browser.find_element(By.ID, "backtoform").click()
    time.sleep(3)
    browser.find_element(By.LINK_TEXT, "Index").click()
    assert titulopagina in browser.title
    
historia1(browser)



#2-Hacer que la cumpla con los requisito de suma, resta, etc que se le pongan 

def historia2(browser):
    browser.find_element(By.ID, "buttoncalculator").click()
    browser.find_element(By.ID, "button04").click()
    browser.find_element(By.ID, "button08").click()
    browser.find_element(By.ID, "buttonplus").click()
    browser.find_element(By.ID, "button02").click()
    browser.find_element(By.ID, "button04").click()
    browser.find_element(By.ID, "buttonequals").click()
    browser.find_element(By.ID, "buttonallclear").click()
    browser.find_element(By.ID, "button08").click()
    browser.find_element(By.ID, "button05").click()
    browser.find_element(By.ID, "buttonmultiply").click()
    browser.find_element(By.ID, "button07").click()
    browser.find_element(By.ID, "button04").click()
    browser.find_element(By.ID, "buttonequals").click()
    browser.find_element(By.ID, "buttonallclear").click()
    browser.find_element(By.ID, "button03").click()
    browser.find_element(By.ID, "button06").click()
    browser.find_element(By.ID, "buttonminus").click()
    browser.find_element(By.ID, "button05").click()
    browser.find_element(By.ID, "button08").click()
    browser.find_element(By.ID, "buttonequals").click()
    browser.save_screenshot("captura_de_pantalla2.png")
    time.sleep(3)
    browser.find_element(By.LINK_TEXT, "Index").click()
    assert titulopagina in browser.title
    
historia2(browser)



#3-hacer que me calcule la longitud o el ancho, etc de un triangulo, etc.

def historia3(browser):
    browser.find_element(By.ID, "triangleapp").click()
    browser.find_element(By.ID, "side1").click()
    browser.find_element(By.ID, "side1").send_keys("4")
    browser.find_element(By.ID, "side2").click()
    browser.find_element(By.ID, "side2").send_keys("3")
    browser.find_element(By.ID, "side3").click()
    browser.find_element(By.ID, "side3").send_keys("5")
    browser.find_element(By.ID, "identify-triangle-action").click() 
    browser.find_element(By.ID, "side3").click()
    browser.find_element(By.ID, "side3").send_keys("1")
    browser.find_element(By.ID, "identify-triangle-action").click()
    browser.find_element(By.ID, "side2").click()
    browser.find_element(By.ID, "side2").send_keys("2")
    browser.find_element(By.ID, "identify-triangle-action").click()
    browser.save_screenshot("captura_de_pantalla3.png")
    time.sleep(3)
    browser.find_element(By.LINK_TEXT, "Index").click()
    assert titulopagina in browser.title
    
historia3(browser)


#4-Hacer que el cronometro cumpla con las funciones de iniciar, parar y reiniciarlo en caso de accionar lo.

def historia4(browser):
    browser.find_element(By.ID, "countdowntest").click()
    browser.find_element(By.ID, "timer-seconds").click()
    browser.find_element(By.ID, "timer-seconds").send_keys("100")
    browser.find_element(By.CSS_SELECTOR, ".timer-reset").click()
    browser.find_element(By.ID, "start-timer").click()
    browser.find_element(By.ID, "reset-timer").click()
    browser.find_element(By.ID, "start-timer").click()
    browser.find_element(By.ID, "stop-timer").click()
    browser.find_element(By.ID, "reset-timer").click()
    browser.find_element(By.ID, "clear-timer").click()
    browser.find_element(By.ID, "start-timer").click()
    browser.save_screenshot("captura_de_pantalla4.png")
    time.sleep(3)
    browser.find_element(By.LINK_TEXT, "Index").click()
    assert titulopagina in browser.title
    
historia4(browser)


#5-Hacer que cumpla con los parametro que se le exigen de 7 digitos validos.

def historia5(browser):
    browser.find_element(By.ID, "7charval").click()
    browser.find_element(By.NAME, "characters").click()
    browser.find_element(By.NAME, "characters").send_keys("1234567")
    browser.find_element(By.NAME, "validate").click()
    browser.find_element(By.NAME, "characters").click()
    browser.find_element(By.NAME, "characters").send_keys("1234567867")
    browser.find_element(By.NAME, "validate").click()
    browser.save_screenshot("captura_de_pantalla5.png")
    time.sleep(3)
    browser.find_element(By.LINK_TEXT, "Index").click()
    browser.quit()
    assert titulopagina in browser.title
    
historia5(browser)

