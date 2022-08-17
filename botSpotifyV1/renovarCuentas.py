from PQTs.MongoDB.MongoDB import MongoDB

def db_acc_neverinstallestado2_to_0():

    mongoDB = MongoDB()
    mongoDB.iniciarDB()

    result = mongoDB.find("neverinstall",{"acc_estado":1})
    for elem in result: 
        mongoDB.updateOne("neverinstall",elem["_id"], {"acc_estado":0})
        mongoDB.updateOne("tinytask",elem["_id"], {"acc_estado":0})


if __name__ == '__main__':
    db_acc_neverinstallestado2_to_0()