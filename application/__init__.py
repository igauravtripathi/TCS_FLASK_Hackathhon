from flask import Flask,render_template,request,jsonify
import json
from config import Config
app= Flask(__name__,
            static_folder='static',
            template_folder='templates')
app.config.from_object(Config)


from application import routes