import requests
import json
URL = "http://127.0.0.1:8000/studentmodelapi/"



def get_student_info(id):
    URL2 = f"http://127.0.0.1:8000/studentapi/{id}"
    r = requests.get(url=URL2)
    print(r.json())

def get_all_data():
    r = requests.get(url=URL)
    print(r)
    print(r.json())
def put_data():
    data = {
        'id':4,
        'name':'jyotsan',
        'city':'kathmandu'
    }
    json_data = json.dumps(data)
    r = requests.put(data=json_data,url=URL)
    print(r)
    print(r.json())
    
def post_data():
    data = {
        'name':'jyotsan',
        'city':'bhaktapur',
        'roll':56,
    }
    json_data = json.dumps(data)
    r = requests.post(data=json_data,url=URL)
    print(r)
    print(r.json())
    
post_data()