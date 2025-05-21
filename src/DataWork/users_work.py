import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet

import src.Database.Database_Users as db

# ====== ENGINE

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Database/users.db")
engine_users = create_engine(f'sqlite:///{db_path}')
db.users_database.metadata.create_all(engine_users)



def add_user(login, name, password):
    """
    Adds user to database (From Register window)
    Encrypts password and name
    :param login: str
    :param name: str
    :param password: str
    :return: user is created or user already exists
    """
    with open("DataWork/key.txt", 'r') as f:
        cipher = Fernet(f.read())
    name = cipher.encrypt(name.encode())
    password = cipher.encrypt(password.encode())

    Session = sessionmaker(bind=engine_users)
    session = Session()

    if session.query(db.User).filter_by(login=login).first():
        session.close()
        return "user already exists"

    new_user = db.User()
    new_user.login = login
    new_user.name = name
    new_user.password = password

    session.add(new_user)
    session.flush()
    session.commit()

    new_stats = db.Stats()
    new_stats.user_id = session.query(db.User).filter_by(login=login).first().id

    new_stats.games_played = cipher.encrypt("0".encode())
    new_stats.games_won = cipher.encrypt("0".encode())
    new_stats.total_time = cipher.encrypt("00:00".encode())

    session.add(new_stats)
    session.flush()
    session.commit()
    session.close()

    return "success"

def login_user(login, password):
    """
    Logging user in, validating information given
    :param login:
    :param password:
    """
    with open("DataWork/key.txt", 'r') as f:
        cipher = Fernet(f.read())

    Session = sessionmaker(bind=engine_users)
    session = Session()
    if session.query(db.User).filter_by(login=login).first():
        info = session.query(db.User).filter_by(login=login).first()
        db_password = cipher.decrypt(info.password).decode()
        session.close()

        if db_password == password:
            db_name = cipher.decrypt(info.name).decode()
            return db_name
        else:
            return "wrong password"
    else:
        session.close()
        return "wrong login"

def get_stats(login):
    """
    Getting statistics by login of user
    :param login:
    :return:
    """
    with open("DataWork/key.txt", 'r') as f:
        cipher = Fernet(f.read())

    Session = sessionmaker(bind=engine_users)
    session = Session()

    if session.query(db.User).filter_by(login=login).first():
        id = session.query(db.User).filter_by(login=login).first().id
        info = session.query(db.Stats).filter_by(id=id).first()

        g_won = cipher.decrypt(info.games_won).decode()
        g_total = cipher.decrypt(info.games_played).decode()
        time_total = cipher.decrypt(info.total_time).decode()
        return g_total, g_won, time_total

def update_stats(login, g_total1, g_won1, mins, secs):
    """
    Updating stats after the game is finished
    :param login:
    :param g_total1:
    :param g_won1:
    :param mins:
    :param secs:
    :return:
    """
    with open("DataWork/key.txt", 'r') as f:
        cipher = Fernet(f.read())

    g_total0, g_won0, time0 = get_stats(login)

    g_total1 = int(g_total0) + g_total1
    g_won1 = int(g_won0) + g_won1

    mins = mins + int(time0.split(":")[0])
    secs = secs + int(time0.split(":")[1])
    mins += secs // 60
    secs = secs % 60

    time1 = ""
    if mins < 10: time1 = "0" + str(mins)
    else: time1 = str(mins)
    time1 += ":"
    if secs < 10: time1 += "0" + str(secs)
    else: time1 += str(secs)

    Session = sessionmaker(bind=engine_users)
    session = Session()

    if session.query(db.User).filter_by(login=login).first():
        id = session.query(db.User).filter_by(login=login).first().id

        session.query(db.Stats).filter_by(id=id).update({
            "games_played": cipher.encrypt(str(g_total1).encode()),
            "games_won": cipher.encrypt(str(g_won1).encode()),
            "total_time": cipher.encrypt(time1.encode()),
        })
        session.flush()
        session.commit()
    session.close()