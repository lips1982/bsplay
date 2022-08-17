# -*- coding: utf-8 -*-
import datetime
import os
import time
from PQTs.Selenium.Base import BaseAcciones
from PQTs.Utilizar import urlSpotifysinginUS, namelistareproduccion
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
    
    def nuevalistanombre(self):

        try:                             
            xpathnuevalista = (By.XPATH,"//*[@id='main']/div/div[2]/nav/div[1]/div[2]/div/div[1]/button") 
            xpathmyplaylist01 = (By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[1]/div[5]/span/button/span/h1') 
            self.sleep(10)
            try:
                self.click(xpathnuevalista)
            except:
                self.refreshweb()
                time.sleep(10)
                self.click(xpathnuevalista)
            self.sleep(10)
            try:
                self.click(xpathmyplaylist01)
            except:
                self.refreshweb()
                time.sleep(15)
                self.click(xpathmyplaylist01)
            self.sleep(10)
            
            namelista=random.choice(namelistareproduccion)
            pyautogui.write(namelista, interval=0.25)
            self.sleep(4)
            pyautogui.press('tab')
            self.sleep(3)
            pyautogui.press('tab')
            self.sleep(3)
            pyautogui.press('enter')
            self.sleep(4)
            
            return True
            

        except Exception as e:
            with open(os.path.join(pathImg,f"logerror.txt"), 'w') as f:
                f.write(str(e))


    def buscaryagregarartista(self):
        listartistas=[ 
        "Love Is Gone","You Are The Reason","When We Were Young","I Love You 3000","When I Look At You",
        "Impossible","When You Say Nothing At All","MEMORIES","Thank U, Next","A Thousand Years","Perfect","Shallow","Need You Now","On My Way - Alan Walker",
        "Someone You Loved - Lewis Capaldi ","Blinding Lights - The Weeknd","Dusk Till Dawn - ZAYN","Cheap Thrills - Sia","Im Not Her - Clara Mae","Work From Home - Fifth Harmony",
        "Dont Wanna  Know - Maroon 5","Shape of You - Ed Sheeran","Send My Love - Landon Austin","Too Good At Goodbyes - Sam Smith","Sugar - Maroon 5",
        "Body Like A Back Road - Sam Hunt","One More Night - Maroon 5","Friends - Marshmello","Treat You Better - Shawn Mendes","What Are Words - Chris Medina",
        "Wonder - Shawn Mendes","Everything I Wanted - Billie Eilish","Something Just Like This - The Chainsmokers","Lush Life - Zara Larsson",
        "Before You Go - Lewis Capaldi","Beyoncé - Halo","Avril Lavigne - When Youre Gone","NSYNC - Bye Bye Bye","Baby One More Time - Britney Spears",
        "Backstreet Boys - I Want It That Way","Eminem - Love The Way You Lie ft. Rihanna","Justin Timberlake - Cry Me A River","Rihanna - Diamonds","Rihanna - Take A Bow",
        "Destinys Child - Say My Name","Miley Cyrus - Party In The U.S.A.","Britney Spears - Oops!...I Did It Again","Backstreet Boys - Shape Of My Heart","Britney Spears - Sometimes",
        "Beyoncé - Single Ladies","NSYNC - Its Gonna Be Me","Rihanna - Umbrella","Rihanna - We Found Love","Alicia Keys - If I Aint Got You"]


        miscanciones=[
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[2]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[3]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[4]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[5]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[6]/div/div[3]/button',
        '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[7]/div/div[3]/button'
        ]
        itemsagregar=[
         '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div',
         '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/div[1]/div[2]/div',
         '//button[text()="Add"]'
        ]
          
        try:  
            miscancionesrandom=random.sample(miscanciones, 7)        
            miscanciones1=miscancionesrandom[0:3]
            miscanciones2=miscancionesrandom[3:7]
            cancion1=random.sample(miscanciones1, 3)
            cancion2=random.sample(miscanciones2, 4)

            mylistartistas=random.sample(listartistas, 4)
            mylistartistas.append("SilkLipsMusicX1")
            mylistartistas.append("SilkLipsMusicX2")
            mylistartistaok1=random.sample(mylistartistas, 6)
            print (mylistartistaok1)
        except Exception as e:
            with open(os.path.join(pathImg,f"logerror-{str(datetime.datetime.now().strftime('%H-%M-%S'))}.txt"), 'w') as f:
                f.write(str(e))

        xpathbuscarartista=(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/section/div/div/input')
        
        xpathalbumSilkLipsMusic=(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div/div/div[2]/div[1]/div/div[1]/div/p[1]')
               
        body=(By.XPATH,'/html/body')

        visiblebuscarartista= self.explicitWaitElementoVisibility(1200,xpathbuscarartista)
        if visiblebuscarartista:
            
            for  elem in mylistartistaok1:
                if elem =='SilkLipsMusicX1':
                    try:
                        self.clear(xpathbuscarartista)
                        self.escribir(xpathbuscarartista,"SilkLipsMusicX")
                        time.sleep(10)
                        self.pagedown(body)
                        self.sleep(4)
                        self.click(xpathalbumSilkLipsMusic)
                        time.sleep(4)
                        xpathcancion=(By.XPATH,cancion1[0])
                        self.click(xpathcancion)
                        print("click cancion1_1")
                        time.sleep(4)
                        xpathcancion=(By.XPATH,cancion1[1] )
                        self.click(xpathcancion)
                        print("click cancion1_2")   
                        time.sleep(4)
                        #xpathcancion=(By.XPATH,cancion1[2])
                        #self.click(xpathcancion)   
                        #print("click cancion1_3") 
                    except Exception as e:
                        with open(os.path.join(pathImg,f"logerror-{str(datetime.datetime.now().strftime('%H-%M-%S'))}.txt"), 'w') as f:
                            f.write(f"{e} --- {elem} --- {xpathcancion}")                   
                
                elif elem =='SilkLipsMusicX2':
                    try:
                        self.clear(xpathbuscarartista)
                        time.sleep(1)
                        self.escribir(xpathbuscarartista,'SilkLipsMusicX')
                        time.sleep(10)
                        self.click(xpathalbumSilkLipsMusic)
                        time.sleep(3)
                        xpathcancion=(By.XPATH,cancion2[0] )
                        self.click(xpathcancion)
                        print("click cancion2_1") 
                        time.sleep(3)
                        xpathcancion=(By.XPATH,cancion2[1] )
                        self.click(xpathcancion)     
                        print("click cancion2_2") 
                        time.sleep(3)
                        #xpathcancion=(By.XPATH,cancion2[2] )
                        #self.click(xpathcancion)      
                        #print("click cancion2_3") 
                        #time.sleep(3)
                        #xpathcancion=(By.XPATH,cancion2[3] )
                        #self.click(xpathcancion) 
                        #print("click cancion2_4") 
                    except Exception as e:
                        with open(os.path.join(pathImg,f"logerror-{str(datetime.datetime.now().strftime('%H-%M-%S'))}.txt"), 'w') as f:
                            f.write(f"{e} --- {elem} --- {xpathcancion}")                                                               
                else:
                    self.clear(xpathbuscarartista)
                    time.sleep(1)
                    self.escribir(xpathbuscarartista,elem)
                    time.sleep(10)
                    try:
                        i=2
                        print ("artista ", elem)
                        xpathcancion=(By.XPATH,itemsagregar[i] )
                        self.click(xpathcancion)
                        print("cancion agregada")
                        time.sleep(2)
                        print('Agregando 1 canciones del artista',elem)  
                    except Exception as e:
                        with open(os.path.join(pathImg,f"logerror-{str(datetime.datetime.now().strftime('%H-%M-%S'))}.txt"), 'w') as f:
                            f.write(f"{e} --- {elem} --- {xpathcancion}")
        else:
            print(f"visibleNuevalista {visiblebuscarartista}")            



    def abrirlistareproduccion(self):
        xpathlistadereproduccion= (By.XPATH,'//*[@id="main"]/div/div[2]/nav/div[1]/div[2]/div/div[4]/div[4]/div/div/ul/div/div[2]/div/li') 
        try:
            self.click(xpathlistadereproduccion)
        except:
            self.refreshweb()
            time.sleep(10)
            self.click(xpathlistadereproduccion)
            


    def enviardatos(self,email):
        remitente = 'mayfeljonas1229@gmail.com'
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
        sesion_smtp.login('mayfeljonas1229@gmail.com','dudwvopyazvtxtun')

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexión
        sesion_smtp.quit()





