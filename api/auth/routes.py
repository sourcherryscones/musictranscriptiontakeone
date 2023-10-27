from api.auth import auth
from api.extensions import db
from api.models.musician import Musician
from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, login_manager, current_user

@auth.route('/users/')
def index():
    allusers = Musician.query.first()
    print(allusers.musician_name)
    return f'<h1>{allusers.musician_name}</h1>'


@auth.route('/login', methods=['POST'])
def loginpost():
    print('MADE IT TO LOGIN FUNCTION')
    req = request.json
    mname = req['username']
    password = req['password']
    usr = Musician.query.filter_by(musician_name=mname).first()
    if not usr:
        return jsonify({'success': False, 'error': 'USER NOT FOUND'})
    print(usr.password)
    if not usr or not check_password_hash(usr.password, password):
        return jsonify({'success': False})

    #do actual checking of pw hash here
    login_user(usr,remember=False)
    return jsonify({'success': True})


@auth.route('/signup', methods=['POST'])
def signup():
    requ = request
    req = request.get_json()
    email = req['email']
    mname = req['username']
    password = req['password']
    grade = req['grade']
    pwconf = req['pwconf']
    usrcheck = Musician.query.filter_by(email=email).first()
    namecheck = Musician.query.filter_by(musician_name=mname).first()

    if usrcheck or namecheck:
        return jsonify({'registered': False, 'error': 'USER ALREADY EXISTS'})

    if password != pwconf:
        return jsonify({'registered': False, 'reguser': None, 'error': 'PASSWORDS DO NOT MATCH'})
    
    newusr = Musician(musician_name=mname, email=email, password=generate_password_hash(password, method='scrypt'))
    db.session.add(newusr)
    db.session.flush()
    db.session.commit()

    return jsonify({'registered': True})

@auth.route("/getsession")
def check_session():
    if current_user.is_authenticated:
        return jsonify({"login": True})

    return jsonify({"login": False})

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'logoutsuccessful': True})