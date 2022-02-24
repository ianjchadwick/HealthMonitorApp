import json
import logging


# noinspection PyTypeHints
def validate_device_json(device_json):
    """Module takes JSON as input from device, parses the data and ensures that the data is in a valid format. Then
    returns a python dictionary with the validated values."""
    # log configuration setup
    logging.basicConfig(filename="logs/device_module.log",
                        format='%(asctime)s - %(levelname)s - %(process)d - %(message)s',
                        level=logging.INFO)
    json_obj = open(device_json)
    data = json.load(json_obj)
    # Dictionary to compare expected types based on input type
    types = {"temperature": float, "blood_pressure": [int, int], "oximeter": [int, int], "glucometer": int,
             "weight_height": [float, float]}

    # get information required to validate data
    type = data['device_type']
    measurement = data['measurement']

    # Validating data
    if type in types:
        type_check = types[type]
        if isinstance(measurement, list):
            for item in measurement:

                if not isinstance(item, type_check):
                    logging.error("Data measurement does not match datatype")
                    return
    elif not isinstance(measurement, type_check):
        logging.error("Data measurement does not match datatype")
        return

    # If data is valid, get the rest of the metadata/information from the JSON
    device_id = data['device_id']
    patient_assigned = data['patient_assigned']
    MAC = data['MAC']
    purchase_date = data['purchase_date']
    model_number = data['model_number']
    model_name = data['model_name']
    serial_number = data['serial_number']
    logging.info("Successfully validated data for device: " + str(device_id))

    return {"device_id": device_id,
            "patient_assigned": patient_assigned,
            "type": type,
            "measurement": measurement,
            "MAC": MAC,
            "purchase_date": purchase_date,
            "model_number": model_number,
            "model_name": model_name,
            "serial_number": serial_number}


if __name__ == "__main__":
    test = "test_files/device_test.json"
    print(validate_device_json(test))
