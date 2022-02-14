import json
import logging

logging.basicConfig(filename="logs/device_module.log", format='%(asctime)s - %(levelname)s - %(process)d - %(message)s',
                    level=logging.INFO)


def device_reading(device_json):
    """Module takes JSON as input from device, parses the data and uploads it to the correct database location"""
    json_obj = open(device_json)
    data = json.load(json_obj)
    types = {"temperature": float, "blood_pressure": [int, int], "oximeter": [int, int], "glucometer": int,
             "weight_height": [float, float]}

    type = data['device']['device_type']
    measurement = data['device']['measurement']
    # noinspection PyTypeHints
    if type in types:
        type_check = types[type]
        if isinstance(measurement, list):
            for item in measurement:
                # noinspection PyTypeHints
                if not isinstance(item, type_check):
                    logging.error("Data measurement does not match datatype")
                    return
    elif not isinstance(measurement, types[type]):
        logging.error("Data measurement does not match datatype")
        return

    device_id = data['device']['device_id']
    patient_assigned = data['device']['patient_assigned']
    MAC = data['device']['MAC']
    purchase_date = data['device']['purchase_date']
    model_number = data['device']['model_name']
    model_name = data['device']['model_name']
    serial_number = data['device']['serial_number']
    logging.info("Successfully, inputting info for device: " + str(device_id))

    return [device_id, patient_assigned, type, measurement, MAC, purchase_date, model_number, model_name, serial_number]


if __name__ == "__main__":
    test = "test_files/device_test.json"
    print(device_reading(test))
