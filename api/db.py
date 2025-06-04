import psycopg2
import os
import json

def init_db():
    def q(conn, cursor):
        cursor.execute(open('init-db.sql', 'r').read())
        conn.commit()

    db_query(q)


def get_user(id):
    def q(conn, cursor):
        cursor.execute('SELECT * FROM user_ where id=%s', (id,))
        row = cursor.fetchone()
        return {"name": row[1]}

    return db_query(q)


def add_user(data):
    def q(conn, cursor):
        cursor.execute('INSERT INTO user_(name) VALUES (%(name)s) ON CONFLICT (id) DO UPDATE SET name = %(name)s', data)
        conn.commit()
    
    db_query(q)


def db_query(f, cursor_factory=None):
    conn = psycopg2.connect(os.environ["POSTGRES_URL"])
    res = None
    with conn.cursor(cursor_factory=cursor_factory) as cursor:
        res = f(conn, cursor)
    conn.close()
    return res
