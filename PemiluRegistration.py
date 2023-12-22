from flask import Flask, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__)

@app.route('/success/<thenik>', methods=['GET'] )
def success(thenik):
    return 'Proses data Pemilu NIK : %s berhasil' % thenik

@app.route("/insertpemiludata", methods=['POST'])  
def insertpemiludata():
    pass
    
@app.route("/updatepemiludata", methods=['POST'])  
def updatepemiludata():
    pass

@app.route("/deletepemiludata", methods=['POST'])  
def deletepemiludata():
    pass
    
@app.route('/pemilulist')
def pemilulist():
    pemilues = getAllPemiluData()
    return render_template('pemilulist.html', title='Daftar Pemilu', listpemilu=pemilues)

def insertPemiludata(nik, nama, tempat_lahir, tanggal_lahir, alamat):
   pass

def updatePemiludata(nik, nama, tempat_lahir, tanggal_lahir, alamat):
    pass
    
def deletePemiludata(nik):
    pass

def getAllPemiluData():
    # Open database connection
    connection = sqlite3.connect("pemilu.db")
    cursor = connection.cursor()
    # Execute the query
    cursor.execute("SELECT nik, nama, tempat_lahir, tanggal_lahir, alamat FROM pemiludata;")    

    # convert it into dictionary
    desc = cursor.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
    # Close the connection
    connection.close()
    return data

if __name__ == '__main__':
    app.run()
