from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class dragndrop():
     def dragdrop(self):

         baseUrl = "https://jqueryui.com/droppable/"
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get(baseUrl)

         driver.switch_to.frame(0)
         dragable_element = driver.find_element(By.ID,'draggable')
         location1 = dragable_element.location
         print("Before drag position",location1)
         x1=location1.get(0)
         print (x1)

         actions = ActionChains(driver)
         actions.drag_and_drop_by_offset(dragable_element,150,50)
         actions.perform()
         time.sleep(5)

         location2 = dragable_element.location
         print("After drag position:", location2)
         x2 = location2.get(1)
         print(x2)


dd = dragndrop()
dd.dragdrop()