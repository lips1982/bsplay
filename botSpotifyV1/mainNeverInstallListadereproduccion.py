# -*- coding: utf-8 -*-
import Xlib.display
from pyvirtualdisplay import Display
import pyautogui
import os
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Paths import pathImg
import time
import random
from PQTs.Selenium.Acciones.Accioneslagregarlistanueva import Acciones
from PQTs.Selenium.Acciones.enviaremail import enviaremailerror

def main():


    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()


    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    
    time.sleep (random.randint(1,4))
    hilos=1
    time.sleep (random.randint(1,5))

    db=MongoDB(hilos)
    db.iniciarDB()
    email=[]
    id=[]
    passw=[]

    result= db.findby2("accountmanager","acc_estado",1,"pais","US")

    for elem in result:
        email= (elem["email"])
        id=(elem["_id"])
        passw =(elem["pass"])
        db.updateOne("accountmanager",id,"acc_estado",3)
        db.updateOne("accountmanager",id,"datelogin",time.time())  
        #for elemid in id:
        #    db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
        db.cerrarConexion()

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
        while returnLoginSpotify== False:
            returnLoginSpotify= acciones.loginSpotify(email,password)
    
        pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-loging.png"))
    
        if returnLoginSpotify == True:
            print(f"Hilo {email} - SinginSpotify {returnLoginSpotify}")

        acciones.sleep(10)    
        acciones.refreshweb()

        acciones.sleep(10)
        
        acciones.nuevalistanombre()
        #pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-nombbrelistacreada.png"))
        acciones.buscaryagregarartista()
        acciones.sleep(3)

        acciones.abrirlistareproduccion()
        
        acciones.sleep(15)
        pyautogui.screenshot(os.path.join(pathImg,f"{email}.png"))
        
        acciones.sleep(15)
        acciones.enviardatos(email)
        return True
    try:
        iniciarSpotify (email,passw)
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",5)
        db.cerrarConexion()

    except Exception as e:
        with open(os.path.join(pathImg,f"error.txt"), 'w') as f:
            f.write(str(e))        
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",1)
        db.cerrarConexion()
        error= "error.txt"
        enviaremailerror(email,error)

    display.stop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open(os.path.join(pathImg,f"error.txt"), 'w') as f:
            f.write(str(e))  