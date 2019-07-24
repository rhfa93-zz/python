# -*- coding: UTF-8 -*-

import sys, os, json, re
#import sys
import MysqlEngineClass
import pymysql
from flask import Flask,jsonify, render_template, Markup

user = os.environ["SQL_DB_USER"]
pw = os.environ["SQL_DB_PS"]

conn = MysqlEngineClass.MysqlEngineClass(host='localhost', user=user, passwd=pw, db='fina_db')
json_data = conn.execute("SELECT * FROM test")

data = json_data[0:10]
new_data = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '))
br_data = new_data.replace('\n', '<br>')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False#日本語文字分け

@app.route('/')
def hello_json():
    http_json = Markup(br_data)
    
    #return jsonify(http_json)
    return http_json
if __name__ == '__main__':
    app.run()

