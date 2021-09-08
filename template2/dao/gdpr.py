from template2.database.Mongoconnection import Mongoconnection
from bson.objectid import ObjectId
import pymongo
class PolicyDaogdpr(Mongoconnection):
    print("insidepolicydao")
    def __init__(self):
        super(PolicyDaogdpr, self).__init__()
        print("inside_init")
        self.get_collectiongdpr("policies")

    def getCountOfTotalEntries(self, customerId):
        return self.collection.count_documents({"customerId": customerId})

    def getpolicy(self,customerid):
        cursor = self.collection.find_one({"cust_id" : customerid} )
        print(cursor)
        return cursor
    '''def isPolicyExist(self, policyId, customerId):
        result = self.collection.find_one({"_id": ObjectId(policyId), 'customerId': customerId})
        if result:
            return True
        return False'''

    def create(self, policy):
       
        '''print("insidecreatepolicy")
        print(self,policy)
        
        
        print("collection count",self.collection.count())'''
        c = self.collection.count()
        d = c*13 + 1
      
        res = {}
        count=0
        for i, j in policy.items():
             print(i, ":", j)
             count=count+1
            
             if count>=5 and count<=7:
                res[i]=j
               

            
        #print("polic",res)
        res["cust_id"] = c*13 + 1
        insertOneResult = self.collection.insert_one(res)
        print("self id",insertOneResult.inserted_id)
        #print("collection list ",self.db.list_collection_names())
        #print("collection",self.collection)
        
        return d

    def update(self, policy, policyId):
        # Remove the '_id' as it's immutable and results in WriteError
        policy.pop('_id', None)

        #updateResult = self.collection.update({'_id': ObjectId(policyId)}, policy)
        #return updateResult['updatedExisting']

    def getPolicy(self, policyId, customerId):
        return self.collection.find_one({'_id': ObjectId(policyId), 'customerId': customerId})

    def replace(self, policyName, customerId, policy):
        # True flag makes upsert = True i.e. when filter result not found it will create entry
        updateResult = self.collection.replace_one(
            {'name': policyName, "customerId": customerId}, policy, True)
        return updateResult.raw_result['updatedExisting']