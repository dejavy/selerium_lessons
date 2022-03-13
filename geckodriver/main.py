# from selenium import webdriver
# from seleniumwire import webdriver  # for proxy
import time
# import random
from fake_useragent import UserAgent
# from proxy_auth_data import login, pasword

# urls
url_1 = "https://www.olx.ua/"
url_2 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url_3 = "https://2ip.ua/"

# add useragent
useragent = UserAgent()

# optoins
options = webdriver.FirefoxOptions()

# user-agent
# options.set_preference("general.useragent.override", "Hello friend")
options.set_preference("general.useragent.override", useragent.random)

# set proxy
# proxy = "12.3.243.178:8080"
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True
# firefox_capabilities["proxy"] = {
#     "poxyTupe": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }

# proxy_options = {
#     "proxy": {
#         "https": f"http://{login}:{password}@12.3.243.178:8080"
#     }
# }

# driwer
driver = webdriver.Firefox(
    executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/geckodriver/geckodriver",
    options=options
)

# driwer +proxy
# driver = webdriver.Firefox(
#     executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/geckodriver/geckodriver",
#     seleniumwire_options=proxy_options
# )

# driver = webdriver.Firefox(
#     executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/geckodriver/geckodriver",
#     options=options,
#     proxy=proxy
# )


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
