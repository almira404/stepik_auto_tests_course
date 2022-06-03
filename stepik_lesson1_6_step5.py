from selenium import webdriver
import math
#задание на поиск элемента по тексту в ссылке

link1 = "http://suninjuly.github.io/find_link_text.html"
try:
    browser = webdriver.Chrome()
    browser.get(link1)

    #тут идет поиск ссылки по совпадению части текста ссылки с формулой
    #str(math.ceil(math.pow(math.pi, math.e)*10000))
    link2 = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link2.click()
    #поиск первого поля ввода
    input1 = browser.find_element_by_tag_name("input")
    #передача значения в первое поле
    input1.send_keys("Ivan")
    #поиск второго поля ввода
    input2 = browser.find_element_by_name("last_name")
    #передача значения во второе поле
    input2.send_keys("Petrov")
    #поиск третьего поля ввода
    input3 = browser.find_element_by_class_name("city")
    #передача значения в третье поле
    input3.send_keys("Smolensk")
    #поиск четвертого поля ввода
    input4 = browser.find_element_by_id("country")
    #передача значения в четвертое поле
    input4.send_keys("Russia")
    #поиск кнопки сабмит
    button = browser.find_element_by_css_selector("button.btn")
    #нажатие на кнопку сабмит
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()