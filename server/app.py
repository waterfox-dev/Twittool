from flask import Flask
from flask import render_template, request
from server.router import router
from server.module.twittool.account import Account, UserNotFound

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

@app.route('/user_result', methods = ['GET', 'POST'])
def user_result():
    result = dict(request.form) 
    try :
        return render_template(router['user_result'], user = Account(result['userQuery']).serialize())
    except UserNotFound :
        return render_template(router['user_not_found'], arobase = result['userQuery'])