import requests
import device_module
import chat_module

# Test to use on localhost IP
BASE = "http://127.0.0.1:5000/"

# Loads a test JSON file from test_files directory and runs basic tests for device API
test = "test_files/device_test.json"
data = device_module.validate_device_json(test)
print(data)
device_id = str(data["_id"])

response = requests.put(BASE + "device/" + device_id, data)
print(response.json())

response = requests.get(BASE + "device/" + device_id)
print(response.json())

response = requests.delete(BASE + "device/" + device_id)
print(response)

response = requests.get(BASE + "device/" + device_id)
print(response.json())

# Loads a test JSON file from test_files directory and runs basic tests for chat message database API
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
