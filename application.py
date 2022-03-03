from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

header_text = '''
    <html>\n<head> <title>Device Module Flask Test</title> </head>\n<body>'''
instructions = '''
    <p>This is a RESTful web service!\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


application = Flask(__name__)
api = Api(application)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text + instructions + footer_text))

# Rules for put arguments for Device Module
device_put_args = reqparse.RequestParser()
device_put_args.add_argument("device_id", type=int, help="Must have a device_id", required=True)
device_put_args.add_argument("patient_assigned", type=int, help="Must have a patient_id assigned", required=True)
device_put_args.add_argument("device_type", type=str, help="Must have a device_type", required=True)
device_put_args.add_argument("measurement", help="Must have a measurement", required=True)
device_put_args.add_argument("MAC", type=str, help="Must have a MAC address", required=True)
device_put_args.add_argument("purchase_date", type=str, help="Must have a device_type", required=True)
device_put_args.add_argument("model_number", type=int, help="Must have a model_number", required=True)
device_put_args.add_argument("model_name", type=str, help="Must have a model_name", required=True)
device_put_args.add_argument("serial_number", type=int, help="Must have a serial_number", required=True)

# Rules for put arguments for Chat Module
msg_put_args = reqparse.RequestParser()
msg_put_args.add_argument("message_id", type=int, help="Must have a message_id", required=True)
msg_put_args.add_argument("conversation_id", type=int, help="Must have a conversation_id", required=True)
msg_put_args.add_argument("sender_id", type=int, help="Must have a sender_id", required=True)
msg_put_args.add_argument("recipient_id", type=int, help="Must have a recipient_id", required=True)
msg_put_args.add_argument("message_date", type=str, help="Must have a message_date", required=True)
msg_put_args.add_argument("message_txt", type=str, help="Must have a message_txt", required=True)


devices = {}
chat = {}


def msg_id_dne(msg_id):
    """Abort if message_id does not exist (DNE)"""
    if msg_id not in chat:
        abort(404, message="message_id does not exist")


def device_id_dne(device_id):
    """Abort if the device_id does not exist (DNE)"""
    if device_id not in devices:
        abort(404, message="device_id does not exist")


def msg_id_already_exists(msg_id):
    """Abort if the msg_id already exists"""
    if msg_id in chat:
        abort(409, message="msg_id already exists")


def device_id_already_exits(device_id):
    """Abort if the device_id already exists"""
    if device_id in devices:
        abort(409, message="device_id already exists")


class Message(Resource):
    def get(self, msg_id):
        """Retrieve information about a message with a given message_id"""
        # Abort if message_id does not exist
        msg_id_dne(msg_id)
        return chat[msg_id]

    def put(self,msg_id):
        """"Create a new message entry with input msg_id and insert the information into database"""
        # Abort if the device id already exists
        msg_id_already_exists(msg_id)
        args = msg_put_args.parse_args()
        chat[msg_id] = args
        return chat[msg_id], 201

    def delete(self, msg_id):
        """Delete a message with input message_id"""
        # Abort if the message_id does not exist
        msg_id_dne(msg_id)
        del chat[msg_id]
        return '', 204


class Device(Resource):
    def get(self, device_id):
        """Retrieve information about a device with a given device_id"""
        # Abort if device_id does not exist
        device_id_dne(device_id)
        return devices[device_id]

    def put(self, device_id):
        """"Create a new device with input device_id and insert the information into database"""
        # Abort if the device id already exists
        device_id_already_exits(device_id)
        args = device_put_args.parse_args()
        devices[device_id] = args
        return devices[device_id], 201

    def delete(self, device_id):
        """Delete a device with input device_id"""
        # Abort if the device_id does not exist
        device_id_dne(device_id)
        del devices[device_id]
        return '', 204


api.add_resource(Message, "/chat/<string:msg_id>")
api.add_resource(Device, "/device/<string:device_id>")

if __name__ == "__main__":
    application.run(debug=True)
