import pymysql
from flask import Flask, jsonify, request, render_template
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
            db_connection.close()
            
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
      return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)