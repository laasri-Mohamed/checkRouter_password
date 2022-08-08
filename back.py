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
 
 
def enter(date, pas):
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES(?,?)", (date, pas))
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
    
def last():
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
     
    i = c.fetchall()
    conn.commit()
    conn.close()
    lastpawd = i[-1][1]
    print("Le dernier password est: "+lastpawd)
    return lastpawd #to get the last password out of this function

def URL(url):
    conn = sq.connect(db)
    c = conn.cursor()
    
     
    i = c.fetchall()
    conn.commit()
    conn.close()
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #os.environ['PATH'] += r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\SelniumDrivers"
    driver = webdriver.Chrome(executable_path=r"C:\Users\LAASRI MOHAMED\OneDrive\Bureau\chromedriver.exe",chrome_options=options)
   
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(url)
    time.sleep(100)

 
def check():
    # cette fonction vérifiera si la base de données
    # est vide ou non
    if len(show()) == 0:
        return False
    else:
        return True

def precedentId():
    data=c.execute(SELECT * FROM)
 

