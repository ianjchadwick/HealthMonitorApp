# HealthMonitorApp
A platform to allow healthcare providers to monitor patients' vitals remotely via smart devices. The idea would be 
to send patients home with the devices to recover at home instead of in hospitals.

## Users
* Patients
* Medical Professionals (Nurses and Doctors)
* Administrators
* Developers
>* Application Developers
>* Device Integrators
>* Machine Learning Scientists

## Branching Strategy
Branches will be assigned an issue which will define the new features or functions that are being added to the 
platform. Branches will be merged with the main branch once they have been adequately tested.

## Database Design

The database schema can be found at [this link](https://dbdiagram.io/d/620561ee85022f4ee573a861)

## Modules

### RESTful API
The RESTful API is deployed to AWS Elastic Beanstalk. How to use and specific calls to the API are detailed under each sub-module's section.

### Device Module
The device module is an API designed to allow different devices to upload the data to the platform. It will receive a JSON file with the device information, verify the data parse it and return a format that is ready to be uploaded into the database.

#### Device Module Expected JSON format
{ "device_id": 1,
  "patient_assigned": 12,
  "device_type": "temperature",
  "measurement": 98.6,
  "MAC": "30-65-EC-6F-C4-58",
  "purchase_date": "01-01-2001",
  "model_number": 1234,
  "model_name": "temp-o-matic",
  "serial_number": 56789
}

#### Calling the Device Module API
The calls to the API are made using the requests library with the general format: "BaseURL" + "device/<device_id>" + data (in the format of a python dictionary using:
- PUT: i.e. response = requests.put(BASE + "device/0", data) 
- GET: i.e. response = requests.get(BASE + "device/0")
- DELETE i.e. response = requests.put(BASE + "device/0", data)

### Chat Message Module
The chat message module will allow users to chat with other users of the app which in this case, will include Healthcare Providers, Patients and Administrators. 

#### User Stories
- Send text messages to Users
- Recieve text messages from Users
- Send files to/get from other users 
- Retrieve chat/message history

#### Database Design
The database schema for the chat can be found at [this link](https://dbdiagram.io/d/6220252454f9ad109a4d6528)

#### Chat Module Expected JSON Format
{ "message_id": 1,
  "conversation_id": 1,
  "sender_id": 1234,
  "recipient_id": 5678,
  "message_date": "2001-01-24 12:30:55",
  "message_txt": "This is a message!"
}

#### Calling the Chat Module API
The calls to the API are made using the requests library with the general format: "BaseURL" + "chat/<msg_id>" + data (in the format of a python dictionary using:
- PUT: i.e. response = requests.put(BASE + "chat/0", data) 
- GET: i.e. response = requests.get(BASE + "chat/0")
- DELETE i.e. response = requests.put(BASE + "chat/0", data)
