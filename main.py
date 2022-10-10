import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
from time import strftime
import csv


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
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//a[@data-handler="next"]').click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//a[@data-handler="next"]').click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//td[@data-month="11"]/a[text()="1"]').click()
    driver.implicitly_wait(10)

    # input check out date
    driver.execute_script('document.getElementById("id_salida").removeAttribute("readonly")')
    driver.find_element(by=By.XPATH, value='//td[@data-month="11"]/a[text()="2"]').click()
    driver.implicitly_wait(10)

    # click check availability button
    driver.find_element(by=By.XPATH, value='//button[@class="engine__action-button"]').click()
    driver.implicitly_wait(10)

    # get all headers
    rooms = driver.find_elements(by=By.CSS_SELECTOR, value='.habitacion')
    print("Number of Room types found: ", len(rooms))
    for room in rooms:
        room_name = room.find_element(by=By.CSS_SELECTOR, value='.hab_titulo').text
        room_price = room.find_element(by=By.CSS_SELECTOR, value='.precio-total').text
        print(room_name, room_price)

        # save into csv
        with open('record.csv', 'a', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow([strftime("%Y-%m-%d %H:%M:%S"), room_name, room_price])

        # EXCELLENCE CLUB TWO-STORY ROOFTOP TERRACE SUITE W/ PLUNGE POOL
        if room_name == "EXCELLENCE CLUB TWO-STORY ROOFTOP TERRACE SUITE W/ PLUNGE POOL":
            print("FOUND")
            # send iMessage
            print("Sending iMessage...")
            os.system('open -a Messages')
            for i in range(10):
                time.sleep(3)
                keyboard = Controller()
                keyboard.type("GOT IT")
                time.sleep(3)
                keyboard.press(Key.enter)

    driver.quit()


if __name__ == '__main__':
    run_count = 1
    while True:
        current_time = strftime("%Y-%m-%d %H:%M:%S")
        print(run_count, current_time)
        run_count += 1
        finest_scraper()
        time.sleep(1800)
