from selenium import webdriver
import time
url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="/Users/dejavy/PycharmProjects/selerium_lessons/chromedriver/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)
    # driver.get(url="https://www.stackoverflow.com/")
    # time.sleep(5)
    # driver.refresh()

    driver.get_screenshot_as_file("1.png")
    driver.get(url="https://www.stackoverflow.com/")
    time.sleep(5)
    driver.save_screenshot("2.png")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
