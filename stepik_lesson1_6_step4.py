from selenium import webdriver
import time
#задание на поиск элементов с помощью Selenium

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск первого поля ввода
    input1 = browser.find_element_by_tag_name("input")
    #передача значения в первое поле
    input1.send_keys("Ivan")
    #поиск второго поля ввода
    input2 = browser.find_element_by_name("last_name")
    #передача значения во второе поле
    input2.send_keys("Petrov")
    #поиск второго поля ввода
    input3 = browser.find_element_by_class_name("city")
    #передача значения в третье поле
    input3.send_keys("Smolensk")
    #поиск четвертого поля ввода
    input4 = browser.find_element_by_id("country")
    #передача значения в четвертое поле
    input4.send_keys("Russia")
    #поиск кнопки
    button = browser.find_element_by_css_selector("button.btn")
    #нажатие на кнопку
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


