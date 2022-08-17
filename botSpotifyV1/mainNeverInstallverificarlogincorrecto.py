# -*- coding: utf-8 -*-
#TESTTTTT

from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesCheckaccount import Acciones
from threading import Thread, Barrier
import time

hilos=1
start= time.time()

def accountsSpotify():
    id=[]
    email =[]
    passw =[]
      
    db=MongoDB(hilos)
    db.iniciarDB()
       
    for elem in (db.findby2("accountmanager","acc_estado",0,"pais","COL")):
            email.append(elem["email"])
            id.append(elem["_id"])
            passw.append(elem["pass"])
    for elemid in id:
            db.updateOne("accountmanager",elemid,"acc_estado",3)
    db.cerrarConexion()
    return email, id, db, passw

users, id,db, passw= accountsSpotify()
print (len(users))
print (users," ", id," ",db," ", passw)


    
def iniciarSpotify(barrier,email,password,i,id,db):

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

    
    if returnLoginSpotify == True:
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",5)
        db.cerrarConexion()
        print("NO REGISTRADA(true)")
        barrier.wait()
     
    if returnLoginSpotify == False:
        db.iniciarDB()
        db.updateOne("accountmanager",id,"acc_estado",1)
        db.cerrarConexion()
        print("REGISTRADA(false)")
        barrier.wait()
    

barrier = Barrier(len(users))
hiloscerrados = 0
threads = []
   
for i in range(len(users)):
    i = Thread(target=iniciarSpotify, args=(barrier,users[i],passw[i],i,id[i],db))
    i.start()
    threads.append(i)
for i in threads:
    i.join()

