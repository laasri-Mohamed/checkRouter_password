import sqlite3 as sq
from selenium import webdriver
import os
import time
 
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

db = 'secure.db'
 
 
def connect():
   
    
    conn = sq.connect(db)
     
    
    c = conn.cursor()
    c.execute("""
                 CREATE TABLE IF NOT EXISTS data (
                     PASs ,
                     username ,
                     url text,
                     date text,
                     password text primary key
                     
                 )             
    """)
    items = c.fetchall()
    for item in items:
        print(item)
     
    # to commit the sql command, it will commit the
    # current transaction or
    conn.commit()
    conn.close()
 
 
def enter(username,PASs,url, date, pas):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES(?,?,?,?,?)", (username,PASs, url, date, pas))
    conn.commit()
    conn.close()
 
 
def show():
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
     
    # ça va stocker toutes les données de la table à
    # la variable i sous forme de liste 2d
    i = c.fetchall()
    conn.commit()
    conn.close()
    return i
 
def Del(password):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("DELETE FROM data WHERE password=(?)", (password,))
    conn.commit()
    conn.close()
 
 
def edit(date, password):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("UPDATE data SET date=? WHERE password=(?)  ",
              (date, password))
    conn.commit()
    conn.close()


def USERNAME(username):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES(?)", (username))
    conn.commit()
    conn.close()

def PASSWORD(PASs):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES(?)", (PASs))
    conn.commit()
    conn.close()
    
    


def last():
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
     
    i = c.fetchall()
    conn.commit()
    conn.close()
    lastpawd = i[-2][4]
    print("Le dernier password est: "+lastpawd)
    return lastpawd

def NEW():
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
     
    i = c.fetchall()
    conn.commit()
    conn.close()
    new = i[-1][4]
    return new
    

def URL(user,Pas, url):
    conn = sq.connect(db)
    c = conn.cursor()
     

    i = c.fetchall()
    conn.commit()
    conn.close()
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #os.environ['PATH'] += r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\SelniumDrivers"
    driver = webdriver.Chrome(executable_path=r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\chromedriver.exe",chrome_options=options)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("http://"+url+"/")

    ###################################################################### TELECOM ROUTER ################################################################################################################################## 
    """#login
    username = driver.find_element(by=By.XPATH,value='//*[@id="user"]')
    username.send_keys(user)

    PasswordForLogin = driver.find_element(by=By.XPATH,value='//*[@id="password"]')
    PasswordForLogin.send_keys(Pas)

    button1 = driver.find_element(by=By.XPATH,value='//*[@id="authform"]/table/tbody/tr/td[2]/table/tbody/tr[7]/td/input[1]')
    button1.click()

    time.sleep(2)


    button2 = driver.find_element(by=By.XPATH,value='//*[@id="Menu1Txt0"]')
    button2.click()

    button3 = driver.find_element(by=By.XPATH,value='/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/a')
    button3.click()

    button4 = driver.find_element(by=By.XPATH,value='/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a[2]')
    button4.click()
    
    NewPassword = driver.find_element(by=By.XPATH,value='/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table[2]/tbody/tr/td[2]/table/tbody/tr[11]/td[2]/input')
    NewPassword.clear()
    NewPassword.send_keys(NEW())

    button5 = driver.find_element(by=By.XPATH,value='/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table[2]/tbody/tr/td[2]/table/tbody/tr[13]/td/input[1]')
    button5.click()
    
    time.sleep(100)"""
    ###################################################################### ORANGE ROUTER ##################################################################################################################################
    #login
    username = driver.find_element(by=By.ID,value='Frm_Username')
    username.send_keys(user)
    
    LastPassword = driver.find_element(by=By.ID,value='Frm_Password')
    LastPassword.send_keys(Pas)
    
    time.sleep(2)
    button1 = driver.find_element(by=By.XPATH,value='//*[@id="LoginId"]')
    button1.click()
    #processus de changement du password1
    button2 = driver.find_element(by=By.XPATH,value='//*[@id="localnet"]')
    button2.click()

    button3 = driver.find_element(by=By.XPATH,value='//*[@id="wlanConfig"]')
    button3.click()

    button4 = driver.find_element(by=By.XPATH,value='//*[@id="WLANSSIDConfBar"]')
    button4.click()
    #For 5G
    NewPassword1 = driver.find_element(by=By.XPATH,value='//*[@id="KeyPassphrase:0"]')
    NewPassword1.clear()
    NewPassword1.send_keys(last())

    button6 = driver.find_element(by=By.XPATH,value='//*[@id="Btn_apply_WLANSSIDConf:0"]')
    button6.click()

    time.sleep(2)

    button5 = driver.find_element(by=By.XPATH,value='//*[@id="instName_WLANSSIDConf:4"]')
    button5.click()
    #For 4G
    NewPassword2 = driver.find_element(by=By.XPATH,value='//*[@id="KeyPassphrase:4"]')
    NewPassword2.clear()
    NewPassword2.send_keys(NEW())

    button6 = driver.find_element(by=By.XPATH,value='//*[@id="Btn_apply_WLANSSIDConf:4"]')
    button6.click()

    #logout

    time.sleep(2)
    button7 = driver.find_element(by=By.XPATH,value='//*[@id="LogOffLnk"]')
    button7.click()
    
    time.sleep(100)

   


    

 
def check():
    # cette fonction vérifiera si la base de données
    # est vide ou non
    if len(show()) == 0:
        return False
    else:
        return True

connect()