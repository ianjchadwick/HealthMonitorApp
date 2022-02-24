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

### Device Module
The device module is an API designed to allow different devices to upload the data to the platform. It will receive 
a JSON file with the device information, parse it and put the information into the database API in the correct 
locations.

### Chat Message Module
The chat message module will allow users to chat with other users of the app which in this case, will include Healthcare Providers, Patients and Administrators. 

#### User Stories
- Send text messages to Users
- Recieve text messages from Users
- Send files to/get from other users 
- Retrieve chat/message history

#### Database Design
The message module will be built around a document based database because the format of the document based database is a lot less restrictive than the relational SQL database and allows for more dynamic input of data as requirements change and enhancements are added.
