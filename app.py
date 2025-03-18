import pymysql
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/HeadersInfo', methods=['GET'])

def biography():
    try:
        
        db_connection = pymysql.connect(
            host="94.55.216.168",       # MySQL sunucusunun adresi (localhost veya IP)
            user="starex",            # MySQL kullanıcı adı
            password="1234",      # MySQL kullanıcı şifresi
            database="WhoIsStarex"  # Bağlanmak istediğiniz veritabanı adı
        )

        cursor = db_connection.cursor()

        cursor.execute("SELECT MainName FROM MainTable")
        main_name = cursor.fetchall() 
        main_name = main_name[0][0]

        cursor.execute("SELECT DescriptionFirst FROM MainTable")
        description_first = cursor.fetchall()
        description_first = description_first[0][0]

        cursor.execute("SELECT DescriptionSecond FROM MainTable")
        description_second = cursor.fetchall() 
        description_second = description_second[0][0]

        cursor.execute("SELECT LinkedIn FROM MainTable")
        linkedin = cursor.fetchall() 
        linkedin = linkedin[0][0]

        cursor.execute("SELECT Steam FROM MainTable")
        steam = cursor.fetchall()
        steam= steam[0][0]

        cursor.execute("SELECT Youtube FROM MainTable")
        youtube = cursor.fetchall()
        youtube = youtube[0][0]

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
    app.run(debug=True)