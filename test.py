import requests
import device_module
import chat_module


# BASE = "http://deviceapp-env.eba-jctvp42w.us-east-1.elasticbeanstalk.com/"
BASE = "http://127.0.0.1:5000/"

test = "test_files/device_test.json"
data = device_module.validate_device_json(test)
print(data)
device_id = str(data["_id"])
print(device_id)

response = requests.put(BASE + "device/" + device_id, data)
print(response.json())
"""
response = requests.get(BASE + "device/" + device_id)
print(response.json())
response = requests.delete(BASE + "device/" + device_id)
print(response)
response = requests.get(BASE + "device/" + device_id)
print(response.json())

msgtest = "test_files/chat_test.json"
msgdata = chat_module.validate_chat_json(msgtest)
msg_id = str(msgdata["_id"])

response = requests.put(BASE + "chat/" + msg_id, msgdata)
print(response.json())

response = requests.get(BASE + "chat/" + msg_id)
print(response.json())

response = requests.delete(BASE + "chat/" + msg_id)
print(response)

response = requests.get(BASE + "chat/" + msg_id)
print(response.json())
"""