import rethinkdb as r
from mojo.config import RETHINK_HOST, RETHINK_PORT
from tornado.gen import coroutine


@coroutine
def get_db_conn():
    """Yields a RethinkDB connection"""
    r.set_loop_type("tornado")
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
def make_wallet_table():
    yield make_table('wallet')


@coroutine
def setup_tables():
    yield make_user_table()
    yield make_wallet_table()


@coroutine
def drop_tables():
    pass
