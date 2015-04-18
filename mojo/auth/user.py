from tornado.gen import coroutine
import rethinkdb as r
from mojo.db import get_db_conn
from mojo.util import encrypt, verify


@coroutine
def add_user(username, password):
    conn = yield get_db_conn()
    # encrypt password
    hash = encrypt(password)
    insert = yield r.table('users').insert({
            'id': username,
            'password': hash
        }).run(conn)
    return insert


@coroutine
def delete_user(username):
    conn = yield get_db_conn()
    yield r.table('users').filter(r.row['username'] == username).delete().run(conn)


@coroutine
def verify_user(username, password):
    conn = yield get_db_conn()
    data = yield r.table('users').get(username).run(conn)
    if data is not None:
        return verify(password, data['password'])
    else:
        return False
