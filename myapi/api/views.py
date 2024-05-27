from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerialzers
from django.http import JsonResponse
import io
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        stu_id = request.GET.get('id', None)
        if stu_id is not None:
            try:
                stu = Student.objects.get(id = stu_id) # complex data type
                serializer = StudentSerialzers(stu,many=True) # serializers convert complex data type into python dict
                return JsonResponse(serializer.data,safe=False)
            except:
                res = {'msg':f"id = {stu_id} not in the db"}
                return JsonResponse(res,safe=True)
        else:
            stu = Student.objects.all() # complex data type
            serializer = StudentSerialzers(stu,many=True) # serializers convert complex data type into python dict
            return JsonResponse(serializer.data,safe=False) # Json response convert python dict into Json
        
    def post(self,request,*args,**kwargs):
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
    def put(self,request,*args,**kwargs):
        json_data  = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        stu_id = python_data.get('id',None)
        try:
            stu = Student.objects.get(id=stu_id)
            serializer = StudentSerialzers(stu,data=python_data,partial=True) # Partial Update
            if serializer.is_valid():
                serializer.save()
                res = {'msg':'successfully updated'}
                return JsonResponse(res,safe=True)
        except:
            res = {'msg':f'id = {stu_id} not exist in the data '}
            return JsonResponse(res,safe=True)
    def delete(self,request,*args,**kwargs):
        json_data  = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
            stu_id = python_data.get('id',None)
            stu = Student.objects.get(id = stu_id)
            stu.delete()
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

def all_student_details(request):
    stu = Student.objects.all() # complex data type
    serializer = StudentSerialzers(stu,many=True) # serializers convert complex data type into python dict
    return JsonResponse(serializer.data,safe=False) # Json response convert python dict into Json

@csrf_exempt
def insert_student(request):
    if request.method == 'POST':
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
        
@csrf_exempt
def update_Student(request):
    if request.method == 'PUT':
        json_data  = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        stu_id = python_data.get('id',None)
        try:
            stu = Student.objects.get(id=stu_id)
            serializer = StudentSerialzers(stu,data=python_data,partial=True) # Partial Update
            if serializer.is_valid():
                serializer.save()
                res = {'msg':'successfully updated'}
                return JsonResponse(res,safe=True)
        except:
            res = {'msg':f'id = {stu_id} not exist in the data '}
            return JsonResponse(res,safe=True)
    else:
        res = {'msg':'wrong method only put method is allowed!!'}
        return JsonResponse(res,safe=True)


def delete(request):
    if request=='DELETE':
        json_data  = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
            stu_id = python_data.get('id',None)
            stu = Student.objects.get(id = stu_id)
            stu.delete()
            return JsonResponse(res,safe=True)
        except:
            stu_id = python_data.get('id',None)
            res = {"msg":"no id = f{stu_id} student is available for deletion"}
            return JsonResponse(res,safe=True)