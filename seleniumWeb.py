import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import pyttsx3

class info():
        def __init__(self):
                self.driver = webdriver.Chrome()
                self.engine = pyttsx3.init()
                rate = self.engine.getProperty('rate')
                # print(rate)
                self.engine.setProperty('rate', 130)
                voices = self.engine.getProperty('voices')
                # print(voices)
                self.engine.setProperty('voice', voices[2].id)

        def speak(self, text):
                self.engine.say(text)
                self.engine.runAndWait() 
                
        def get_info(self,querry):
                self.querry = querry
                self.driver.get(url="https://www.wikipedia.org/")
                # self.driver.maximize_window()   
                search= self.driver.find_element(By.XPATH, "//*[@id='searchInput']")
                
                search.clear()
                search.send_keys(self.querry)
                
                search_button = self.driver.find_element(By.XPATH, "//*[@id='search-form']/fieldset/button/i")
                ActionChains(self.driver).move_to_element(search_button).click().perform()
                
                search_result = ""
                paragraphs = self.driver.find_elements(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[2]")
                for i, paragraph in enumerate(paragraphs):
                        if i >= 2:
                                break
                        text = paragraph.text
                        # Removing citations
                        text = re.sub(r'\[\d+\]', '', text)
                        # Removing links
                        text = re.sub(r'\[.*?\]', '', text)
                        search_result += text + " "
                        
                result = search_result.strip()
                print(result)
                self.speak(result)
                
# assist = info()
# assist.get_info("star")

       
                


