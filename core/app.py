from flask import Flask, g, session
from sqlalchemy.orm import sessionmaker
from config import runtime_config, Config
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object(Config)

engine = create_engine('postgresql://postgres:1@127.0.0.1/contracts')


@app.before_request
def open_session():
    session = sessionmaker()
    g.conn = engine
    session.configure(bind=g.conn)
    g.session = session()


@app.after_request
def close_session(e):
    if e is None:
        g.session.commit()
    else:
        g.session.rollback()

    g.session.close()
    g.session = None
