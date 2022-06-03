from selenium import webdriver
import time
#задание на использование метода find_elements_by

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    #сохранение в список всех полепй ввода с тегом инпут
    elements = browser.find_elements_by_tag_name("input")
    
    #прохождение по списку и ввод значения в каждое из полей
    for element in elements:
        element.send_keys("Мой ответ")
    
    #поиск кнопки сабмит
    button = browser.find_element_by_css_selector("button.btn")
    #клик по кнопке
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

