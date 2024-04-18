from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class music():
        def __init__(self):
                self.driver = webdriver.Chrome()
        def play(self,querry):
            self.querry = querry
            self.driver.get("https://www.youtube.com/results?search_query=" + querry)
            video = self.driver.find_element(By.XPATH, "//*[@id='video-title']")
            video.click()
            time.sleep(300)
            
            self.driver.quit()
                   
# assist=music()
# assist.play("beliver")
            