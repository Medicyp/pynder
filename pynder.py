from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class Autoswiper:
    def __init__ (self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users\Djinn\OneDrive\Documents\PycharmProjects\pinder\chromeprofile")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.wait = WebDriverWait(self.driver, 6)

    # Open Chrome Browser and go to tinder.com
    def open_browser(self, url):
        self.driver.get(url)

    # Swipe_right
    def swipe_like(self):
        sleep(2)
        selector = '#c-690079234 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-like-green\) > button'
        swipe_like = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        swipe_like.click()

    # Swipe_left
    def swipe_dislike(self):
        sleep(2)
        selector = '#c-690079234 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-pink\) > button'
        swipe_dislike = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        swipe_dislike.click()

    # Swiping left or right with random function
    def random_finger(self):
        from random import random
        counter = 0
        while True:
            rand = random()
            sleeping_time = rand * 3
            sleep(sleeping_time)

            dice = random()
            if dice < .81:
                self.swipe_like()
            else:
                self.swipe_dislike()

            counter += 1
            print('Swiped profiles: ', counter)

if __name__ == '__main__':
    run = Autoswiper()
    run.open_browser('https://tinder.com/')
    run.random_finger()
