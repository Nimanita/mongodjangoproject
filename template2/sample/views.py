from django.shortcuts import render

from django.http import HttpResponse
from dao.action import PolicyDao 


from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt

def home(request,customer_id=0):
 if request.method == 'GET':
       print(request,id)
       print("view.home",request)
       print("customerid",customer_id)
       con1 = PolicyDao()
      
      
       y = con1.getpolicy(customer_id)
      
       print(y)
       return JsonResponse("Added successfully  : " + str(y),safe=False)
 elif request.method == 'POST':
       print(request,id)  
       data = JSONParser().parse(request)
       data["cust_id"]=customer_id
       print("customerid",customer_id)
       print("jsondata",data)
       con1 = PolicyDao()
      
       
       y = con1.create(data,customer_id)
      
       print(y)
       return JsonResponse("your policy : " + str(y),safe=False)
'''def create(request) :
       print("view.home",request)
       con1 = PolicyDao()
      
       print("policydao created")
       post = {"name":"sois","Des:":"I am human","ent":"client","loc":"INDIA","add":"plot no 46,sh","con":748499490,
       "rep":"lina","repcon":3384939 ,"dpo":"ksusb","dpo_con":28739736}
       y = con1.create(post)
       y = con2.create(post)
       y = con3.create(post)
       print(y)
       return JsonResponse("Please note your customer_id  : " + str(y),safe=False)
# Create your views here.
def show(request) :
       print("view.show")
       con1 = PolicyDao()
       con2 = PolicyDaogdpr()
       con3 = PolicyDaoccpa()
     
       d1 = con1.getpolicy(105)
       print(d1)
       d2 = con2.getpolicy(105)
       print(d2)
       d3 = con3.getpolicy(105)
       print(d3)
       d1.update(d2)
       d1.update(d3)
       print(d1)
       return JsonResponse("Please note your customer_id  : ",safe=False)

def edit(request) :
       print("view.updatepolicy")
       post = {"name":"sois2","Des:":"I am robot","ent":"client","loc":"INDIA","add":"plot no 46,sh","con":999990,
       "rep":"lina","repcon":3384939 ,"dpo":"ksusb","dpo_con":00000}
       con1 = PolicyDao()
       con2 = PolicyDaogdpr()
       con3 = PolicyDaoccpa()
     
       d1 = con1.updatepolicy(post,66)
       print(d1)
       
       return JsonResponse("Please note your updated customer_id  : ",safe=False)'''