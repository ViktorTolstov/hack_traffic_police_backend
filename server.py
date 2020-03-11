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
    r = request.get_json()
    print(r)
    if r["type"] == 'new_violation':
        # database.add_violation(42,42,1500,"a777aaa","Неправильная парковка")
        # print(database.get_db("violation"))
        from docxtpl import DocxTemplate
        doc = DocxTemplate("test.docx")
        context = { 'director' : "И.И.Иванов"}
        doc.render(context)
        doc.save("test-final.docx")
    return 'ok'

if __name__ == '__main__': 
	# port = int(os.environ.get("PORT", 5000))
	# app.run(host='0.0.0.0', port=port)
    app.run()
