import pymysql
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/HeadersInfo', methods=['GET'])

def biography():
    try:
            
            db_connection = pymysql.connect(
                host="94.55.216.168",       
                user="starex",            
                password="1234",      
                database="WhoIsStarex"  
            )

            cursor = db_connection.cursor()

            cursor.execute("SELECT MainName, DescriptionFirst, DescriptionSecond, LinkedIn, Steam, Youtube FROM MainTable")
            result = cursor.fetchall() 
            main_name = result[0][0]
            description_first = result[0][1]
            description_second = result[0][2]
            linkedin = result[0][3]
            steam = result[0][4]
            youtube = result[0][5]

            cursor.close()
            db_connection.close()
            
            return jsonify({'main_name': main_name, 
                            'description_first': description_first,
                            'description_second': description_second,
                            'linkedin': linkedin,
                            'steam': steam,
                            'youtube': youtube})
        
    except Exception as e:
            
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)