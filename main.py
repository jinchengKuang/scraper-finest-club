import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pynput import keyboard
from pynput.keyboard import Key, Controller


def finest_scraper():
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts, service=ChromeService(executable_path=ChromeDriverManager().install()))

    url = 'https://booking.finestresorts.com/en/bookcore/availability/rooms/finestplaya/'
    driver.get(url)

    driver.implicitly_wait(10)

    #  input destination
    driver.execute_script('document.getElementById("id_destino").removeAttribute("readonly")')
    driver.find_element(by=By.ID, value='id_destino').send_keys('Finest Playa Mujeres')

    # input check in date
    driver.execute_script('document.getElementById("id_entrada").removeAttribute("readonly")')
    driver.find_element(by=By.CLASS_NAME, value='engine__date-group').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//a[@data-handler="next"]').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//a[@data-handler="next"]').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//a[@data-handler="next"]').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//td[@data-month="11"]/a[text()="1"]').click()
    time.sleep(2)

    # input check out date
    driver.execute_script('document.getElementById("id_salida").removeAttribute("readonly")')
    driver.find_element(by=By.XPATH, value='//td[@data-month="11"]/a[text()="2"]').click()
    time.sleep(2)

    # click check availability button
    driver.find_element(by=By.XPATH, value='//button[@class="engine__action-button"]').click()
    time.sleep(5)

    # get all headers
    rooms = driver.find_elements(by=By.CSS_SELECTOR, value='.habitacion')
    for room in rooms:
        room_name = room.find_element(by=By.CSS_SELECTOR, value='.hab_titulo').text
        # EXCELLENCE CLUB TWO-STORY ROOFTOP TERRACE SUITE W/ PLUNGE POOL
        if room_name == "EXCELLENCE CLUB TWO-STORY ROOFTOP TERRACE SUITE W/ PLUNGE POOL":
            # send iMessage
            os.system('open -a Messages')
            for i in range(10):
                time.sleep(3)
                keyboard = Controller()
                keyboard.type("GOT IT")
                time.sleep(2)
                keyboard.press(Key.enter)

    driver.quit()


if __name__ == '__main__':
    while True:
        finest_scraper()
        time.sleep(1800)
