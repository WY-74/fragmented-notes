from selenium import webdriver


def instantiate_driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    return driver
