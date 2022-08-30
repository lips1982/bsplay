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
from PQTs.Selenium.Acciones.AccionesReproducir import Acciones
from PQTs.Selenium.Acciones.enviaremail import *
from datetime import datetime
def main():


    #--> Descomentar para ver en PC
    #display = Display(visible=True, size=(1200,768))

    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()

    #--> Descomentar para ver en PC
    #pyautogui._pyautogui_x11._display = Xlib.display.Display(":0")

    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    time.sleep (random.randint(1,4))
    hilos=1
    time.sleep (random.randint(1,5))
    start= time.time()

    db=MongoDB(hilos)
    db.iniciarDB()
    email=[]
    id=[]
    passw=[]

    result= db.findby2("accountmanager","acc_estado",5,"pais","US")
    
    for elem in result:
        email= (elem["email"])
        id=(elem["_id"])
        passw =(elem["pass"])
        db.updateOne("accountmanager",id,"acc_estado",7)
        db.updateOne("accountmanager",id,"datelogin",time.time())  
        #for elemid in id:
        #    db.updateOne("accountmanager",elemid,"creacionlistasentrenamiento",2)
        db.cerrarConexion()
    
    valor= random.randint(5,30)
    time.sleep(valor)

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
        i=0
        while i <=3:
            if returnLoginSpotify== False:
                returnLoginSpotify= acciones.loginSpotify(email,password)
                i+=1
            else:
                i=4
        time.sleep(10)    
        ckecloging= acciones.checklogingok()
        if ckecloging == True:
            db.iniciarDB()
            db.updateOne("accountmanager",id,"ckeclog","logfail")
            db.updateOne("accountmanager",id,"acc_estado",9)
            db.cerrarConexion()
            exit()

        if ckecloging == False:
            #print(f"Hilo {email} - SinginSpotify {returnLoginSpotify}")
            #pyautogui.screenshot(os.path.join(pathImg,f"01-{email}-loging.png"))
            #loging= f"01-{email}-loging.png"
            #enviaremailerror(email,loging, password)  
            db.iniciarDB()
            db.updateOne("accountmanager",id,"ckeclog","logingok")
            db.cerrarConexion()
        acciones.sleep(4)
        acciones.refreshweb()
        acciones.sleep(10)
        #pyautogui.screenshot(os.path.join(pathImg,"loging.png"))
        #acciones.sleep(15)
        #mensaje= f"loging.png"
        #enviaremailmensaje(email,mensaje)        
        pyautogui.moveTo(1866, 1223)
        pyautogui.click()
        valor= random.randint(1,2)
        if valor == 1:  #reproducir lista
            with open(os.path.join(pathImg,f"mensaje.txt"), 'w') as f:
                f.write("Reproduciendo la lista ") 
            mensaje= "mensaje.txt"
            #enviaremailmensaje(email,mensaje)
            acciones.abrirlistareproduccion()
            time.sleep(10)
            pyautogui.moveTo(1065, 745)
            pyautogui.moveTo(1065, 745)
            pyautogui.click(1065, 745)            
            time.sleep(2)
            pyautogui.moveTo(100, 700)
            pyautogui.click(100,700)              
            pyautogui.click(100,700)  
            time.sleep(2)            
            #pyautogui.screenshot(os.path.join(pathImg,f"abrirlista.png"))
            #time.sleep(15)
            #imagen= "abrirlista.png"
            #enviaremailreproduccion(email,imagen)            
            acciones.reproducir1(email)
            
        
        elif valor==2: #reproducir directamente del album
            acciones.ir('https://open.spotify.com/artist/79y2edTYTHJtBpwcVuCnhH')
            time.sleep(10)
            pyautogui.moveTo(1065, 745)
            pyautogui.click(1065, 745)    
            time.sleep(2)
            pyautogui.moveTo(100, 700)
            pyautogui.moveTo(100, 700)
            pyautogui.click(100,700)    
            pyautogui.click(100,700)       
            with open(os.path.join(pathImg,f"mensaje.txt"), 'w') as f:
                f.write("Reproduciendo el album") 
            #mensaje= "mensaje.txt"
            #enviaremailmensaje(email,mensaje)
            time.sleep(10)
            acciones.reproducir2(email)
            
        elif valor ==3:
            acciones.reproducir3()

        

    try:
        iniciarSpotify (email,passw)
        MYIP="REEMPLAZARPUBLICIP"
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",10)
        db.insertOne("logreproduccion",{ "date":datetime.today().strftime('%Y-%m-%d %H:%M'),"email": email,"IP":MYIP })
        db.cerrarConexion()

    except Exception as e:
        with open(os.path.join(pathImg,f"error.txt"), 'w') as f:
            f.write(str(e))        
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",9)
        db.cerrarConexion()
        #error= "error.txt"
        #enviaremailerror(email,error)


     
    display.stop()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with open(os.path.join(pathImg,f"logerror.txt"), 'w') as f:
            f.write(str(e))
        error= "logerror.txt"
        #email="mainerror"
        #nviaremailerror(email,error)
#acc 1: registrada ok
#acc 1, pais COL , >>>>  acc 1 pais US
#acc 5: lista reproduccion ok
#acc 3: cuenta con error al crear la lista de reproduccion
#acc 7: inicia reproducir
#acc 10: reproduccion terminada
#acc 9: cuenta con error al reproducir



