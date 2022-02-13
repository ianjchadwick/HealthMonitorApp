import json
import logging

logging.basicConfig(filename="logs/device_module.log", format='%(asctime)s - %(levelname)s - %(process)d - %(message)s',
                    level=logging.INFO)


def device_reading(json):
    """Module takes JSON as input from device, parses the data and uploads it to the correct database location"""
    logging.info("Log Test")
    return


if __name__ == "__main__":
    test = "string"
    device_reading(test)
