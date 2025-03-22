import pymysql
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
import json


app = Flask(__name__)

CORS(app)

def db_connection():
      
    load_dotenv()

    DATABASE_IP = os.getenv("DATABASE_IP")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE = os.getenv("DATABASE")

    db_connection = pymysql.connect(
        host=DATABASE_IP,       
        user=DATABASE_USER,            
        password=DATABASE_PASSWORD,      
        database=DATABASE 
    )

    return db_connection

@app.route('/HeadersInfo', methods=['GET'])

def biography():
    try:

            connection = db_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT Language, MainName, DescriptionFirst, DescriptionSecond FROM MainTable")
            result = cursor.fetchall() 

            english_data = next(item for item in result if item[0] == 'ENG')

            main_name_eng = english_data[1]
            description_first_eng = english_data[2]
            description_second_eng = english_data[3]

            turkish_data = next(item for item in result if item[0] == 'TR')

            main_name_tr = turkish_data[1]
            description_first_tr = turkish_data[2]
            description_second_tr = turkish_data[3]

            cursor.execute("SELECT Youtube, Steam, LinkedIn FROM LinkTable")
            result = cursor.fetchall() 
            youtube = result[0][0]
            steam = result[0][1]
            linkedin = result[0][2]

            cursor.close()
            connection.close()
            
            return jsonify({'main_name_eng': main_name_eng, 
                            'description_first_eng': description_first_eng,
                            'description_second_eng': description_second_eng,
                            'main_name_tr': main_name_tr, 
                            'description_first_tr': description_first_tr,
                            'description_second_tr': description_second_tr,
                            'linkedin': linkedin,
                            'steam': steam,
                            'youtube': youtube})
        
    except Exception as e:
            
            return jsonify({'error': str(e)}), 400
    
@app.route('/index')
def index():

    load_dotenv()
      
    if not os.path.exists('static/config.json'):

        data = {
        "API_IP" : os.getenv("API_IP")
        }

        with open('static/config.json','w') as file:
            json.dump(data, file, indent= 4)

    else:
        with open('static/config.json', 'r') as file:
            json_data = json.load(file)

        if os.getenv("API_IP") != json_data:
                 
            data = {
            "API_IP" : os.getenv("API_IP")
            }

            with open('static/config.json','w') as file:
                json.dump(data, file, indent= 4)
            
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)