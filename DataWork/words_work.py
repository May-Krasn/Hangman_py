import os

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

import Database.Database_Words as db

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Database/words.db")
engine_words = create_engine(f'sqlite:///{db_path}')
db.words_database.metadata.create_all(engine_words)

# ======== Get

def get_word_random():
    Session = sessionmaker(bind=engine_words)
    session = Session()

    result = session.query(db.Word).order_by(func.random()).first()
    result_cat = session.query(db.Category).filter_by(id=result.category).first()
    session.close()

    return result_cat.category, result.word

def get_word(cat, diff_id):
    Session = sessionmaker(bind=engine_words)
    session = Session()

    cat_id = session.query(db.Category).filter_by(category=cat).first().id

    if cat == "random":
        result = session.query(db.Word).filter_by(difficulty=diff_id).order_by(func.random()).first()
    elif diff_id == 0:
        result = session.query(db.Word).filter_by(category=cat_id).order_by(func.random()).first()
    else:
        result = session.query(db.Word).filter_by(category=cat_id, difficulty=diff_id).order_by(func.random()).first()
    session.close()

    return result.word

def get_difficulty(id):
    if id == 0:
        return "random"

    Session = sessionmaker(bind=engine_words)
    session = Session()
    result = session.query(db.Difficulty).filter_by(id=id).first().difficulty
    session.close()
    return result

def get_all_categories():
    Session = sessionmaker(bind=engine_words)
    session = Session()
    cats = session.query(db.Category).all()
    result = []
    for x in cats:
        result.append(x.category)
    session.close()
    return result

# =============== ADDING TO DATABASE =======================

def add_difficulty():
    Session = sessionmaker(bind=engine_words)
    session = Session()

    dif1 = db.Difficulty()
    dif1.difficulty = "easy"
    dif2 = db.Difficulty()
    dif2.difficulty = "medium"
    dif3 = db.Difficulty()
    dif3.difficulty = "hard"

    session.add(dif1)
    session.add(dif2)
    session.add(dif3)
    session.commit()
    session.close()

def add_category():
    Session = sessionmaker(bind=engine_words)
    session = Session()

    msg = ""
    while msg != "stop":
        msg = input("Enter a category: ")
        cat = db.Category()
        if not session.query(db.Category).filter_by(category=msg).first() and msg != "stop":
            cat.category = msg
            session.add(cat)
            session.commit()
    session.close()

def add_word():
    Session = sessionmaker(bind=engine_words)
    session = Session()

    msg = ""
    while msg != "stop":
        msg = input("[category,difficulty,word]: ")
        if msg == "stop": return

        word = db.Word()

        to_add = msg.split(",")
        word.category = to_add[0]
        word.difficulty = to_add[1]
        word.word = to_add[2]

        session.add(word)
        session.commit()
    session.close()

# add_difficulty()
# add_category()
# add_word()
