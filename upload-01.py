import serial
import requests

formData = {"device": "Holla", "temperature": "40.44"}
HTTP_Request = requests.post("http://192.168.1.150/iot/", data=formData)

if HTTP_Request:
    HTTP_Response = HTTP_Request.text
    print(HTTP_Response)
