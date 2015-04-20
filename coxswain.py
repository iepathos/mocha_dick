#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mojo.db import get_db_conn
from mojo.auth.user import make_admin, add_user


if __name__ == '__main__':
    db = get_db_conn()
    # parser = argparse.ArgumentParser(description='Demo')
    # parser.add_argument('--add_user',
    #     help='Add a new user to Seadog.  add_user username password',
    #     nargs=2)
    # parser.add_argument('--make_admin',
    #     help='Add a user an admin on Seadog.  --make_admin username')

    # args = parser.parse_args()

    # if args.add_user != None:
    #     username, password = args.add_user
    #     add_user(username, password)

    # if args.make_admin != None:
    #     print(args.make_admin)
    #     make_admin(args.make_admin)
