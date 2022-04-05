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

    # If data is valid, return the JSON as a dictionary
    logging.info("Successfully validated data for device: " + str(data["_id"]))

    return data


if __name__ == "__main__":
    test = "test_files/device_test.json"
    print(validate_device_json(test))
