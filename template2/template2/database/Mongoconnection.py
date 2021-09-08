from pymongo import MongoClient
from django.conf import settings


class Mongoconnection(object):
    def __init__(self):
        DATABASES = settings.DATABASES
        '''self.client = MongoClient(host=[DATABASES['HUERISTICS']['HOST']],
                                  username=DATABASES['HUERISTICS']['USERNAME'],
                                  password=DATABASES['HUERISTICS']['PASSWORD'],
                                  authSource=DATABASES['HUERISTICS']['AUTH_DATABASE'],
                                 connect=False)'''
        self.client = MongoClient(host='localhost:27017',connect=False)
        self.db = self.client['te']

    
    
    def get_collection(self,name):
        self.collection = self.db["BASE"]

    def get_collectiongdpr(self,name):
        self.collection = self.db["GDPR"]
    
    def get_collectionccpa(self,name):
        self.collection = self.db["CCPA"]
      