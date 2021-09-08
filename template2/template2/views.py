from django.shortcuts import render
from template2.utils import get_db_handle, get_collection_handle

def Mongoconnectionpu() :
        print("Mongoconnection")
        db_handle,client1 = get_db_handle('testmam', 'localhost', 8000, 'mamata_2507', 'Vrindavan@25')


        post = {"id" : 0,"name" : "tim","score":5}
        client1.insert_one(post)