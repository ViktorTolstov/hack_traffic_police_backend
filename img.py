from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import requests
import json
import os
import database
import docxtpl
#from flask_sslify import SSLify

app = Flask(__name__)
# sslify = SSLify(app)
CORS(app)

@app.route('/api', methods=['POST', 'GET'])
def bot():
    print(request.files.get('attachmentName'))
    file = request.files.get('attachmentName')
    file.save(os.path.join("./img", "test.png"))
    return 'ok'

if __name__ == '__main__': 
	# port = int(os.environ.get("PORT", 5000))
	# app.run(host='0.0.0.0', port=port)
    app.run()
