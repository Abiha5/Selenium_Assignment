from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
from selenium.common.exceptions import*
import time


class BasicAutomation():
     def test(self):

         baseUrl = "https://www.google.com/"
         driver = webdriver.Chrome()
         driver.get(baseUrl)
         driver.implicitly_wait(5)

         search = driver.find_element(By.NAME,("q"))
         search.send_keys('tintash.com')
         search.submit()
         WebDriverWait(driver, 5).until(EC.title_contains("tintash.com"))

         Click = driver.find_element(By.CSS_SELECTOR ,"a[href='https://tintash.com/']")
         Click.click()

         ClickPortfolio = driver.find_element(By.XPATH,"//*[@id='navbarToggler']/ul/li[4]/a").click()

         driver.execute_script("window.scrollBy(0,400)")

         dropdown = driver.find_element(By.XPATH, "/html//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[1]/div/div[2]/div/div[1]/div[.='Select Solution']")
         dropdown.click()
         value = driver.find_element(By.XPATH, "//*[@id='react-select-2-option-1']/label")
         value.click()

         dropdown = driver.find_element(By.XPATH,"/html//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[2]/div/div[2]/div/div[1]/div[.='Select Technology']")
         dropdown.click()
         value = driver.find_element(By.XPATH, "//*[@id='react-select-3-option-1-3']/label")
         value.click()

         dropdown = driver.find_element(By.XPATH,"/html//div[@id='gatsby-focus-wrapper']/section[@class='py-5']/div[2]/div[@class='container']/div/div[3]/div/div[2]/div/div[1]/div[.='Select Industry']")
         dropdown.click()
         driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH,"//*[@id='react-select-4-option-13']/label"))

         try:
             driver.find_element(By.XPATH,"//*[@id='gatsby-focus-wrapper']/section[2]/div[3]/div/div/span[4]/div/article/div/section/div")
             print("Element found")
         except:
             NoSuchElementException
             print("No such element")

         time.sleep(5)

ss = BasicAutomation()
ss.test()



