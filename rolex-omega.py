from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
#select = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/section/div/div/div[1]/div[2]/select').click()

ruta = os.getcwd()
driver_path = '{}chromedriver.exe'.format(ruta)
service = Service(executable_path = driver_path)
#initialize web driver

reloj = {}
relojes = list()
columnas = ['url','titulo','sold','Make','Model','Year','Papers','Box','Condition','Reference Number','Case Material','Bezel Material','Case Diameter','Crystal','Dial','Dial Numbers','Bracelet Material','Movement','Power Reserve','Water Resistance']

with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('https://grailzee.com/pages/completed-auctions')
    #find element by xpath
    for k in ["omega","rolex"]:
        driver.find_element(By.XPATH, '//*[@id="shopify-section-template--15476476706948__main"]/div/div/div[1]/div[2]/select/option[@value="'+k+'"]').click()
        time.sleep(5)
        for j in range (1,17):
            print(j)
            flag = 0
            reloj['url'] = driver.find_element(By.XPATH,'//*[@id="shopify-section-template--15476476706948__main"]/div/div/div[2]/div['+str(j)+']/div/a').get_attribute('href')
            flag += 1
            driver.find_element(By.XPATH, '//*[@id="shopify-section-template--15476476706948__main"]/div/div/div[2]/div['+str(j)+']/div/div[1]/a').click()
            time.sleep(10)
            reloj['titulo'] = driver.find_element(By.XPATH, '//*[@id="standard-pdp"]/div/div[2]/div/h1').text
            print(reloj['titulo'])
            flag += 1
            reloj['sold'] = driver.find_element(By.XPATH, '//*[@id="standard-pdp"]/div/div[2]/div/div/div/div/span[1]').text
            flag += 1
            
            for i in range(1,6):
                try:
                    key = driver.find_element(By.XPATH, '//*[@id="standard-pdp"]/div/div[3]/div[4]/span['+str(i)+']').text.split(":", 1)[0]
                    value = driver.find_element(By.XPATH, '//*[@id="standard-pdp"]/div/div[3]/div[4]/span['+str(i)+']').text.split(":", 1)[1]
                    reloj[key] = value
                except:
                    reloj[columnas[flag]] = 'Nan'
                flag += 1
        

            key = driver.find_element(By.XPATH,'//*[@id="standard-pdp"]/div/div[3]/div[5]/div[2]/div[2]/div[3]').text.split(":", 1)[0]
            value = driver.find_element(By.XPATH,'//*[@id="standard-pdp"]/div/div[3]/div[5]/div[2]/div[2]/div[3]').text.split(":", 1)[1]
            reloj[key] = value
            flag += 1 
            
            time.sleep(10)
            for i in range(1,12):
                try:
                    key = driver.find_element(By.XPATH, '//*[@id="standard-pdp"]/div/div[3]/div[5]/div[2]/div[2]/div[4]/ul/li['+str(i)+']').text.split(":", 1)[0]
                    value = driver.find_element(By.XPATH, '//*[@id="standard-pdp"]/div/div[3]/div[5]/div[2]/div[2]/div[4]/ul/li['+str(i)+']').text.split(":", 1)[1]
                    reloj[key] = value
                except:
                    reloj[columnas[flag]] = 'Nan'
                        
                flag += 1
    

            relojes.append(reloj)
            try: 
                driver.back()
                time.sleep(10)
            except: 
                driver.get('https://grailzee.com/pages/completed-auctions')
                driver.find_element(By.XPATH, '/html/body/div[2]/div/main/section/div/div/div[1]/div[2]/select/option['+str(k)+']').click()
                time.sleep(10)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print(relojes)