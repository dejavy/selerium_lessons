from selenium import webdriver
import time
import  random
from fake_useragent import UserAgent

# urls
url_1 = "https://www.olx.ua/"
url_2 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# add useragent
useragent = UserAgent()
# optoins
options = webdriver.FirefoxOptions()
# change useragent
# options.set_preference("general.useragent.override", "Hello friend")
options.set_preference("general.useragent.override", useragent.random)
# driwer
driver = webdriver.Firefox(
    executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/geckodriver/geckodriver",
    options=options
)

try:
    driver.get(url=url_2)
    time.sleep(3)
    # driver.get(url="https://www.stackoverflow.com/")
    # time.sleep(5)
    # driver.refresh()

    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://www.stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
