from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_one = browser.find_element_by_css_selector('div.first_block input.first')
    input_one.send_keys('Ivan')

    input_two = browser.find_element_by_css_selector('div.first_block input.second')
    input_two.send_keys('Petrov')

    input_thee = browser.find_element_by_css_selector('div.first_block input.third')
    input_thee.send_keys('Email@gmail.com')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(3)

    text = browser.find_element_by_tag_name("h1").text

    assert text == "Congratulations! You have successfully registered!"

finally:

    time.sleep(5)
    browser.quit()
