from flask import Flask
from flask import render_template
from server.router import router

app       = Flask(__name__)
debug     = True
admin     = True
devmod    = True
publicmod = False

@app.route('/')
def index():
    return render_template(router['index'])

@app.route('/infos')
def infos():
    if debug :
        return render_template(router['infos'])