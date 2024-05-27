from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerialzers
from django.http import JsonResponse
import io
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch') # csrf token is diabled
class StudentAPI(View): # API based view
    def get(self,request,*args,**kwargs): # if request is getting student info
        stu_id = request.GET.get('id', None) # checks for student id , otherwise assigns None
        if stu_id is not None: # if student id is given
            try: # tries to fetch data of that id student.
                stu = Student.objects.get(id = stu_id) # complex data type
                serializer = StudentSerialzers(stu,many=True) # serializers convert complex data type into python dict
                return JsonResponse(serializer.data,safe=False)
            except: # in case that id student is not their
                res = {'msg':f"id = {stu_id} not in the db"} # python data msg
                return JsonResponse(res,safe=True) 
        else:
            stu = Student.objects.all() # complex data type
            serializer = StudentSerialzers(stu,many=True) # serializers convert complex data type into python dict
            return JsonResponse(serializer.data,safe=False) # Json response convert python dict into Json
        
    def post(self,request,*args,**kwargs): # If the request is about inserting new student data.
        json_data = request.body
        stream = io.BytesIO(json_data) # json into stream of bytes
        
        python_data = JSONParser().parse(stream) # stream of bytes into python_data
        serializer = StudentSerialzers(data = python_data) # python_data into table instance
        
        if serializer.is_valid(): # check serializer validation before saving into a table
            serializer.save() # save the data into table
            res = {'msg':'Data Created Wooo !'} # respond for created succesfully
            return JsonResponse(res)
        else:
            return JsonResponse(serializer.errors) # errors
        
    def put(self,request,*args,**kwargs): # for updating the data in database
        json_data  = request.body # fetch json_data from request
        stream = io.BytesIO(json_data) # json_data convert into stream
        python_data = JSONParser().parse(stream) # stream into python_data
        stu_id = python_data.get('id',None) # fetch id of a student from python_data ,otherwise assign None
        try:
            stu = Student.objects.get(id=stu_id) # try to get instance of that student
            serializer = StudentSerialzers(stu,data=python_data,partial=True) # Partial Update
            if serializer.is_valid(): # checks serializer validation
                serializer.save() # saves the updated instance in db
                res = {'msg':'successfully updated'}
                return JsonResponse(res,safe=True)
        except:
            res = {'msg':f'id = {stu_id} not exist in the data '} # if that id student doesn't exist in db
            return JsonResponse(res,safe=True)
        
    def delete(self,request,*args,**kwargs): # if the request is about deletion
        json_data  = request.body # json_data from request 
        stream = io.BytesIO(json_data) # json_data into stream
        python_data = JSONParser().parse(stream) # stream into python data
        try:
            stu_id = python_data.get('id',None)
            if stu_id is not None:
                stu = Student.objects.get(id = stu_id)
                stu.delete()
                res = {
                    'id':stu_id,
                    'msg':'successfully deleted'
                }
                return JsonResponse(res,safe=True)
            else:
                res = {
                    'id':stu_id,
                    'msg':'None id'
                }
                return JsonResponse(res,safe=True)
        except:
            stu_id = python_data.get('id',None)
            res = {"msg":"no id = f{stu_id} student is available for deletion"}
            return JsonResponse(res,safe=True)



# Create your views here.
def student_detail(request,pk):
    try:
        stu = Student.objects.get(id=pk) # complex data type
    except:
        msg = {'error':f'{pk} student is not available at database'}
        return JsonResponse(msg,safe=True)
    serializer = StudentSerialzers(stu) # serializes into python dict
    return JsonResponse(serializer.data,safe=True) # Jsonresponse will response the python dict into json
