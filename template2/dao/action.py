from template2.database.Mongoconnection import Mongoconnection
from bson.objectid import ObjectId
import pymongo
class PolicyDao(Mongoconnection):
    print("insidepolicydao")
    def __init__(self):
        super(PolicyDao, self).__init__()
        print("inside_init")
        self.get_collection("policies")

    def getCountOfTotalEntries(self, customerId):
        return self.collection.count_documents({"customerId": customerId})

    '''def getPolicies(self, filterQuery, sortQuery, skip, limit):
        cursor = self.collection.find(filterQuery).collation({"locale": "en"}).sort(sortQuery).skip(skip).limit(limit)
        policies = list(cursor)
        totalResults = cursor.count()
        return policies, totalResults'''

    '''def isPolicyExist(self, policyId, customerId):
        result = self.collection.find_one({"_id": ObjectId(policyId), 'customerId': customerId})
        if result:
            return True
        return False'''

    def getpolicy(self,custid):
        cursor = self.collection.find({"customer_id" : custid})
        lists = list(cursor)
        #cursor = self.collection.find_one({"cust_id" : customerid} )
        res = {}
        print(lists)
        for i in lists:
            for j, k in i.items():
              if j!="_id":
                res[j]=k
            
        print(res)
        return res

    def create(self, policy,custid):
       
        
        count=0
        list1 = {}
        list2 = {}
        list3 = {}
        list1["customer_id"] = custid
        list2["customer_id"] = custid
        list3["customer_id"] = custid
        for i, j in policy.items():
             
             count=count+1
            
             if count>=1 and count<=4:
                list1[i]=j
             elif count>=5 and count<=7:
                list2[i]=j
             elif count>=8 and count<=10:
                list3[i]=j
                 
        insertOneResult = self.collection.insert_one(list1)
        print("self id",insertOneResult.inserted_id)
        insertOneResult = self.collection.insert_one(list2)
        print("self id",insertOneResult.inserted_id)
        insertOneResult = self.collection.insert_one(list3)
        print("self id",insertOneResult.inserted_id)
      
        
        

    def updatepolicy(self, policy, customerid):
        # Remove the '_id' as it's immutable and results in WriteError
        
        res = self.collection.find_one({"cust_id": customerid})

        print("policy customerid",policy,customerid,res)
        print(res["_id"])
        res1 = {}
        count=0
        for i, j in policy.items():
             print(i, ":", j)
             count=count+1
             res1[i]=j
             if count==4 :
               break
        res1["cust_id"] = customerid
        updateResult = self.collection.update({'_id': ObjectId(res["_id"])}, res1)
        #updateResult = self.collection.update({'cust_id': customerid}, policy)
        #print("update",updateresult)
       

    def getPolicy(self, policyId, customerId):
        return self.collection.find_one({'_id': ObjectId(policyId), 'customerId': customerId})

    def replace(self, policyName, customerId, policy):
        # True flag makes upsert = True i.e. when filter result not found it will create entry
        updateResult = self.collection.replace_one(
            {'name': policyName, "customerId": customerId}, policy, True)
        return updateResult.raw_result['updatedExisting']