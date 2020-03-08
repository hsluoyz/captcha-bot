from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

number_button_xpaths = [
    '//*[@id="root"]/div/div/div/div[4]/div[1]/button',
    '//*[@id="root"]/div/div/div/div[1]/div[1]/button',
    '//*[@id="root"]/div/div/div/div[1]/div[3]/button',
    '//*[@id="root"]/div/div/div/div[1]/div[5]/button',
    '//*[@id="root"]/div/div/div/div[2]/div[1]/button',
    '//*[@id="root"]/div/div/div/div[2]/div[3]/button',
    '//*[@id="root"]/div/div/div/div[2]/div[5]/button',
    '//*[@id="root"]/div/div/div/div[3]/div[1]/button',
    '//*[@id="root"]/div/div/div/div[3]/div[3]/button',
    '//*[@id="root"]/div/div/div/div[3]/div[5]/button',
]


def crawl1(driver):
    driver.get('https://captcha.mouselog.org/virtualkeyboard')

    number = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/p[4]')
    number = number.text
    numbers = [int(x) for x in number]

    for number in numbers:
        driver.find_element_by_xpath(number_button_xpaths[number]).click()

    # submit
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[5]/button').click()


def crawl2(driver):
    driver.get('https://captcha.mouselog.org/formfilling')

    for i in range(1, 7):
        option = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[%d]/div[1]' % i)
        option = int(option.text[7:])

        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[%d]/div[2]/div/label[%d]/span[1]/input' % (i, option)).click()

    # submit
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/button').click()


def crawl3(driver):
    driver.get('https://captcha.mouselog.org/slider')

    for i in range(1, 3):
        value = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/p[%d]' % i)
        target_value = int(value.text[19:])

        slider_handle = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[%d]/div[4]' % i)
        current_value = int(slider_handle.get_attribute('aria-valuenow'))

        slider_all = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[%d]/div[1]' % i)
        x_all = slider_all.rect['width']
        dx = x_all * (target_value - current_value) / 100

        ActionChains(driver).drag_and_drop_by_offset(slider_handle, dx, 0).perform()

    # submit
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/button').click()


if __name__ == '__main__':
    options = Options()
    user_agent = 'ybot'
    options.add_argument('user-agent=%s' % user_agent)
    driver = webdriver.Chrome('driver/chromedriver.exe', options=options)

    crawl1(driver)
    crawl2(driver)
    crawl3(driver)

    driver.close()
