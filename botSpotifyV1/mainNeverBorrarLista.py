# -*- coding: utf-8 -*-
import datetime
import Xlib.display
from pyvirtualdisplay import Display
import pyautogui
import os
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Paths import pathImg
import time
import random
from PQTs.Selenium.Acciones.AccionesBorrarlista import Acciones
from PQTs.Selenium.Acciones.enviaremail import enviaremailerror
def main():


    #--> Descomentar para ver en PC
    #display = Display(visible=True, size=(1200,768))

    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()

    #--> Descomentar para ver en PC
    #pyautogui._pyautogui_x11._display = Xlib.display.Display(":0")

    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    time.sleep (random.randint(1,30))
    hilos=1
    time.sleep (random.randint(1,5))
    

    db=MongoDB(hilos)
    db.iniciarDB()
    email=[]
    id=[]
    passw=[]

    result= db.findby1("accountmanager","acc_estado",4)

    for elem in result:
        email= (elem["email"])
        id=(elem["_id"])
        passw =(elem["pass"])
        db.updateOne("accountmanager",id,"acc_estado",2)
        db.cerrarConexion()

    print (email, id,db,passw)

    def iniciarSpotify(email,password):
        
        driver = BaseConexion().conexionChrome()
        #driver = BaseConexion().conexionChromeHeadless()

        acciones = Acciones(driver)
        try:
            ingresando=acciones.ingresarSpotify()
        except:
            ingresando=acciones.ingresarSpotify()
        while ingresando==False:
            try:
                ingresando=acciones.ingresarSpotify()
            except:
                ingresando=acciones.ingresarSpotify()
                


        returnLoginSpotify= acciones.loginSpotify(email,password)
        #while returnLoginSpotify== False:
        #    returnLoginSpotify= acciones.loginSpotify(email,password)

        time.sleep(8)
        acciones.refreshweb()
        #while returnLoginSpotify== False:
        #    returnLoginSpotify= acciones.loginSpotify(email,password)
        time.sleep(10)
        pyautogui.moveTo(74, 430)
        time.sleep(1)
        pyautogui.moveTo(74, 430)                
        pyautogui.click(button='right')
        time.sleep(10)
        pyautogui.moveTo(120, 580)
        time.sleep(1)
        pyautogui.moveTo(120, 580)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(600, 700)
        time.sleep(1)
        pyautogui.moveTo(600, 700)        
        pyautogui.click()         
        acciones.sleep(15)
        pyautogui.screenshot(os.path.join(pathImg,f"{email}.png"))
        acciones.sleep(15)
        acciones.enviardatos(email)        


    try:
        iniciarSpotify (email,passw)
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",1)
        db.cerrarConexion()

    except Exception as e:
        with open(os.path.join(pathImg,f"error.txt"), 'w') as f:
            f.write(str(e))        
        error= "error.txt"
        enviaremailerror(email,error)
        db.cerrarConexion()
        exit()

    
    display.stop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open(os.path.join(pathImg,f"errormain.txt"), 'w') as f:
            f.write(str(e))



#acc 1: registrada ok
#acc 1, pais COL , >>>>  acc 1 pais US
#acc 5: lista reproduccion ok
#acc 3: cuenta con error de loging
#acc 7: inicia reproducir
#acc 10: reproduccion terminada
#acc 9: cuenta con error al reproducir
