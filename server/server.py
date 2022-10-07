import sys
sys.path.insert(0, 'D:/Yuvaraj/project/Chess/functions')
from database import connect, insert,delete
from genrateDateName import nowEncryption
# global defines
serverName = ''
disconnect = 0
# start server
def startServer():
    global serverName,disconnect
    connect()
    serverName = nowEncryption("chessYt")
    insert("insert into serverState (serverName) values ('" + serverName + "')")
    while disconnect == 0:
        
# stop server
def stopServer():
    connect()
    delete("update serverState set serverActive = 0,serverEndDateTime = GETDATE() where serverName = '"+ serverName +"'")
startServer()