from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


# Create a new client and connect to the server
load_dotenv()
mongo_connection = os.getenv('MONGO_CONNECTION')
client = MongoClient(mongo_connection, server_api=ServerApi('1'))
database = client['IoTRaspberry']
collection = database.devices

app = Flask(__name__)

@app.route("/includedevice/<device_name>", methods=['POST'])
def set_new_devices(device_name):
    new_device = { "device_name": device_name, "status": False }
    result = collection.insert_one(new_device)
    device_id = str(result.inserted_id)
    return device_id

@app.route("/getdevices", methods=['GET'])
def get_devices():
    result = collection.find_all()
    return result

@app.route("/deletedevices/<device_name>", methods=['DELETE'])
def delete_devices(device_name):
    try:
        collection.delete_one({"device_name": device_name})
        return 'Success'
    except Exception as e:
        return 'Failed'

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')