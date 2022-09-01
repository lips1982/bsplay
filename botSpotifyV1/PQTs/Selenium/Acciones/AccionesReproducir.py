# -*- coding: utf-8 -*-

import datetime
import os
import time

from PQTs.Selenium.Base import BaseAcciones
from PQTs.Utilizar import urlSpotifysinginUS, sendermail

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PQTs.Paths import pathImg
import pyautogui
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from PQTs.Selenium.Acciones.enviaremail import enviaremailreproduccion


class Acciones(BaseAcciones):
    def ingresarSpotify(self):
        try:
            self.maximizar()
            self.ir(urlSpotifysinginUS)
            self.sleep(2)
            return True
        except:
            self.salir()
            return False
    def checklogingok(self):
        xpatherrorpass = (By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/span')
        visibleErrorloging = self.explicitWaitElementoVisibility(10,xpatherrorpass)
        if visibleErrorloging:
            return True
        else:
            return False

    def loginSpotify(self,cuenta,password):
        try:
            xpathInputEmail = (By.ID,"login-username")
            xpathInputPassword = (By.ID,"login-password")        
            xpathBotonLogin= (By.ID,"login-button")
            xpathfailemailorpass= (By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/span') 
            
            visibleInputEmail = self.explicitWaitElementoVisibility(15,xpathInputEmail)
            if visibleInputEmail:
                self.escribir(xpathInputEmail,cuenta)
                
                visibleInputPassword = self.explicitWaitElementoVisibility(15,xpathInputPassword)
                if visibleInputPassword:
                    self.escribir(xpathInputPassword,password)
                    visibleBotonLogin = self.explicitWaitElementoVisibility(15,xpathBotonLogin)
                    if visibleBotonLogin:
                        self.click(xpathBotonLogin)
                        self.explicitWaitElementoInvisibility(11,xpathBotonLogin)
                                                                                             
                    else:
                        print(f"visibleBotonLogin {xpathBotonLogin}")
                        return False
                else:
                    print(f"visibleInputPassword {visibleInputPassword}")
                    return False
            else:
                print(f"visibleInputEmail {visibleInputEmail}")
                return False
        except:
            self.refreshweb()
            time.sleep(4)
            return False
    
    def abrirlistareproduccion(self):
        xpathlistadereproduccion= (By.XPATH,'//*[@id="main"]/div/div[2]/nav/div[1]/div[2]/div/div[4]/div[4]/div/div/ul/div/div[2]/div/li') 
                                             
        try:
            self.click(xpathlistadereproduccion)
        except:
            time.sleep(4)
            self.refreshweb()
            time.sleep(8)
            self.click(xpathlistadereproduccion)

    def reproducir1(self,email):
        xpathbotonplay= (By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button') 
        
        try:                        
            self.click(xpathbotonplay)

        except:
            self.refreshweb()
            time.sleep(10)
            self.click(xpathbotonplay)
            pass
        time.sleep(10)
        pyautogui.screenshot(os.path.join(pathImg,f"reproduciendo.png"))
        time.sleep(15)
        imagen= "reproduciendo.png"
        enviaremailreproduccion(email,imagen)
        time.sleep(1080)
        #pyautogui.screenshot(os.path.join(pathImg,f"18min.png"))
        #time.sleep(10)
        #imagen= "18min.png"
        #enviaremailreproduccion(email,imagen)
        time.sleep(540)
        #pyautogui.screenshot(os.path.join(pathImg,f"27min.png"))    
        #time.sleep(10)
        #imagen= "27min.png"
        #enviaremailreproduccion(email,imagen)

    def reproducir2(self,email):
        xpathseemore= (By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[3]/div[1]/div/div/button/div') 
        
        try:                        
            self.click(xpathseemore)
        except:
            time.sleep(5)
            self.ir('https://open.spotify.com/artist/79y2edTYTHJtBpwcVuCnhH')
            time.sleep(10)
            self.refreshweb()
            time.sleep(8)
            self.click(xpathseemore)

        xpathplay= (By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/div/button')
                              
        self.click(xpathplay)

        time.sleep(10)
        pyautogui.screenshot(os.path.join(pathImg,f"play.png"))
        time.sleep(10)
        imagen= "play.png"
        enviaremailreproduccion(email,imagen)
        time.sleep(240)
        #pyautogui.screenshot(os.path.join(pathImg,f"4min.png"))    
        #time.sleep(10)
        #imagen= "4min.png"
        #enviaremailreproduccion(email,imagen)        
        time.sleep(240)
        #pyautogui.screenshot(os.path.join(pathImg,f"8min.png"))    
        #time.sleep(10)
        #imagen= "8min.png"
        #enviaremailreproduccion(email,imagen)         
        time.sleep(240)
        #pyautogui.screenshot(os.path.join(pathImg,f"12min.png"))    
        #time.sleep(10)
        #imagen= "12min.png"
        #enviaremailreproduccion(email,imagen) 
        time.sleep(240)
        #pyautogui.screenshot(os.path.join(pathImg,f"16min.png"))    
        #time.sleep(10)
        #imagen= "16min.png"
        #enviaremailreproduccion(email,imagen) 
        time.sleep(240)
        #pyautogui.screenshot(os.path.join(pathImg,f"22min.png"))    
        #time.sleep(10)
        #imagen= "22min.png"
        #enviaremailreproduccion(email,imagen) 


    def reproducir3(self):
        xpathbotonplay= (By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[2]/div[4]/div/div/div/div/div/button') 
        try:                        
            self.click(xpathbotonplay)
        except:
            self.refreshweb()
            time.sleep(10)
            self.click(xpathbotonplay)
        pass

        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"3min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"6min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"9min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"12min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"15min.png"))
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"18min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"21min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"24min.png"))    
        time.sleep(180)
        pyautogui.screenshot(os.path.join(pathImg,f"27min.png"))    

    def enviardatos(self,email):
        remitente = 'azuresilk02@gmail.com'
        destinatarios = ['azuresilkmain@gmail.com']
        asunto = f'Lista de reproduccion : {email}'
        cuerpo = f"{str(datetime.datetime.now().strftime('%H-%M-%S'))}"
        ruta_adjunto = (os.path.join(pathImg,f"{email}.png"))
        nombre_adjunto = f'{email}.png'

        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        
        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(ruta_adjunto, 'rb')
        
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        
        # Creamos la conexión con el servidor
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        
        # Ciframos la conexión
        sesion_smtp.starttls()

        # Iniciamos sesión en el servidor
        #sesion_smtp.login('mayfeljonas1229@gmail.com','dudwvopyazvtxtun')
        emailsender=random.choice(sendermail)
        corre, contrase = emailsender
        sesion_smtp.login(corre,contrase)

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexión
        sesion_smtp.quit()





