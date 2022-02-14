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
