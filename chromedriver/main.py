from selenium import webdriver
# from seleniumwire import webdriver  # for proxy
import time
# import random
from fake_useragent import UserAgent
# from proxy_auth_data import login, pasword

# urls
url_1 = "https://www.instagram.com/"
url_2 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url_3 = "https://2ip.ua/"

user_agents_list = [
    "HelloWorld",
    "best_of_the_best",
    "python_today"
]

useragent = UserAgent()

# options
# https://deviceatlas.com/blog/list-of-user-agent-strings
# https://deviceatlas.com/blog/mobile-browser-user-agent-strings
options = webdriver.ChromeOptions()

# user-agent
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
# options.add_argument("--proxy-server=12.3.243.178:8080")
# proxy_options = {
#     "proxy": {
#         "https": f"http://{login}:{password}@12.3.243.178:8080"
#     }
# }

# driver
driver = webdriver.Chrome(
    executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/chromedriver/chromedriver",
    options=options
)

# +proxy
# driver = webdriver.Chrome(
#     executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/chromedriver/chromedriver",
#     seleniumwire_options=proxy_options
# )

try:
    driver.get(url=url_3)
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
