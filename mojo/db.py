import rethinkdb as r
from mojo.config import RETHINK_HOST, RETHINK_PORT, DB_NAME
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from functools import partial


LISTENERS = []


@coroutine
def get_db_conn():
    """Yields a RethinkDB connection"""
    r.set_loop_type("tornado")
    try:
        conn = yield r.connect(host=RETHINK_HOST,
                               port=RETHINK_PORT,
                               db=DB_NAME)
    except r.RqlRuntimeError:
        conn = yield r.connect(host=RETHINK_HOST, port=RETHINK_PORT)
    return conn


@coroutine
def make_table(name):
    conn = yield get_db_conn()
    try:
        yield r.table_create(name).run(conn)
        print("Table %s created successfully." % name)
    except r.RqlRuntimeError:
        print("Table %s already exists... skipping." % name)


@coroutine
def make_user_table():
    yield make_table('users')


@coroutine
def make_match_table():
    yield make_table('matches')


@coroutine
def make_teams_table():
    yield make_table('teams')


@coroutine
def setup_tables():
    yield make_user_table()
    yield make_match_table()


@coroutine
def rethink_listener():
    db_conn = yield get_db_conn()
    users = r.table('users')
    io_loop = IOLoop.instance()
    feed = yield users.changes().run(db_conn)
    while (yield feed.fetch_next()):
        change = yield feed.next()
        msg = {}
        user = change['new_val']['id']
        if not change['old_val']:
            msg['funds'] = change['new_val']['funds']
        elif change['new_val']['funds'] != change['old_val']['funds']:
            msg['funds'] = change['new_val']['funds']

        for client in LISTENERS:
            if client.get_current_user() == user:
                io_loop.add_callback(partial(client.on_message, msg))
