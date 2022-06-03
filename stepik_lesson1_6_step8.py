from selenium import webdriver
import time 
#задание поиск элемента(кнопки сабмит) по XPath

link = "http://suninjuly.github.io/find_xpath_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #поиск первого поля ввода
    input1 = browser.find_element_by_tag_name("input")
    #ввод значения в первое поле
    input1.send_keys("Ivan")
    #поиск второго поля ввода
    input2 = browser.find_element_by_name("last_name")
    #ввод значения во второе поле
    input2.send_keys("Petrov")
    #поиск третьего поля ввода
    input3 = browser.find_element_by_class_name("city")
    #ввод значения в третье поле
    input3.send_keys("Smolensk")
    #поиск четвертого поля ввода
    input4 = browser.find_element_by_id("country")
    #ввод значения в четвертое поле
    input4.send_keys("Russia")

    #поиск кнопки сабмит с помощью xpath
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    #клик по кнопке
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


