import json
import logging


# noinspection PyTypeHints
def validate_chat_json(chat_json):
    """Module takes JSON as input from chat program, parses the data and ensures that the data is in a valid format.
    Then returns a python dictionary with the validated values."""
    # log configuration setup
    logging.basicConfig(filename="logs/chat_module.log",
                        format='%(asctime)s - %(levelname)s - %(process)d - %(message)s',
                        level=logging.INFO)
    json_obj = open(chat_json)
    data = json.load(json_obj)

    # Dictionary to compare expected types based on input type
    fields = ("message_id", "conversation_id", "sender_id", "recipient_id", "message_date", "message_txt")
    types = {"message_id": int, "conversation_id": int, "sender_id": int, "recipient_id": int,
             "message_date": str, "message_txt": str}

    for field in fields:
        correctType = types[field]
        if field not in data:
            logging.error(field + " is not present in input")
            return
        if not isinstance(data[field], correctType):
            logging.error(field + " is not the correct type")
            return

    # If data is valid, return the JSON
    logging.info("Successfully validated chat data from coversation_id: " + str(data["conversation_id"]))

    return data


if __name__ == "__main__":
    test = "test_files/chat_test.json"
    print(validate_chat_json(test))
    test = "test_files/device_test.json"
    print(validate_chat_json(test))
