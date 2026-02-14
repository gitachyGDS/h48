#map : collection of data items (data structure) that have key-value pair,mutable,order(after 3.7 version ),donot allow duplicate 

a={
    "name":"sujan",
    "age":99
}

# print(a["nam"])
print(a.get("name","data is not found"))

# var=dict(name="sujan",age=99)
# print(type(a))
# print(a)

# print(len(a))

# print(a['name']) #sujan
# print(a.get("name","data is not found"))
# print(a.keys())
# print(a.values())
# print(a.items())

# a={
#     "name":"sujan",
#     "age":99,
#     "address":"pokhara"
    
# }

# a.setdefault("address","ktm")
# print(a)

# a.pop("age")
# a.popitem()
# print(a)

# a["name"]="sujan thadarai"
# print(a)

# b={
#     "email":"sujan@gmail.com",
#     "age":100
# }
# a.update(b)

# print(a)


# a=["sujan","hari","manoj"]

# b=dict.fromkeys(a,"present")
# b['manoj']="absent"
# print(b)


#nested dictionary :one dictionary inside another dictionary

# a={
#     "name":"sujan",
#     "age":88,
#     "marks":["sujan","ram"]
# }

# var=a["marks"]
# print(var[0])

# marks={
#     "roll no 1":{
#         "name":"sujan",
#         "age":99
#     },
#     "roll no 2":{
#         "name":"manoj",
#         "age":78
#     }
# }

#  #{'name': 'sujan', 'age': 99}
# print(marks["roll no 1"]["age"])



# data={

#    "weather": [
#       {
#          "id": 501,
#          "main": "Rain",
#          "description": "moderate rain",
#          "icon": "10d"
#       }
#    ],
#    "main": {
#       "temp": 284.2,
#       "feels_like": 282.93,
#       "temp_min": 283.06,
#       "temp_max": 286.82,
#       "pressure": 1021,
#       "humidity": 60,
#       "sea_level": 1021,
#       "grnd_level": 910
#    }, 
# }



# v=data['weather'] # [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}]
# v1=(v[0]) #{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}
# print(v1["description"])
# # print(data["main"]['temp'])

# print(data["weather"][0]['description'])