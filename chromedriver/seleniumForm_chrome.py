from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import olx_login, olx_password
import time
# import random

# urls
url_1 = "https://www.olx.com/"
url_2 = "https://www.olx.ua/myaccount/pro/"

# options
# https://deviceatlas.com/blog/list-of-user-agent-strings
# https://deviceatlas.com/blog/mobile-browser-user-agent-strings

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# driver
driver = webdriver.Chrome(
    executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/chromedriver/chromedriver",
    options=options
)


try:
    driver.get(url=url_2)
    time.sleep(3)

    #  login
    # email_input = driver.find_element(id, "userEmail") # Before
    email_input = driver.find_element(By.ID, "userEmail")  # After
    email_input.clear()
    email_input.send_keys(olx_login)
    time.sleep(1)

    # passwopd
    password_input = driver.find_element(By.ID, "userPass")
    password_input.clear()
    password_input.send_keys(olx_password)
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)

    #  button press
    # button_press = driver.find_element(By.ID, "se_userLogin").click()
    time.sleep(7)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
