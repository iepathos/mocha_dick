from tornado.gen import coroutine
import rethinkdb as r
from mojo.db import get_db_conn
from mojo.util import encrypt, verify


@coroutine
def add_user(conn, username, password):
    # encrypt password
    hash = encrypt(password)
    insert = yield r.table('users').insert({
            'id': username,
            'password': hash,
            'funds': 0,
            'is_admin': False
        }).run(conn)
    return insert


@coroutine
def delete_user(conn, username):
    yield r.table('users').get(username).delete().run(conn)


@coroutine
def verify_user(conn, username, password):
    data = yield r.table('users').get(username).run(conn)
    if data is not None:
        return verify(password, data['password'])
    return False


@coroutine
def make_admin(conn, username):
    yield r.table('users').get(username).update({
            'is_admin': True
        }).run(conn)


@coroutine
def is_admin(conn, username):
    user = yield r.table('users').get(username).run(conn)
    return user.get('is_admin', False)
