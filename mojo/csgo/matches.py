# -*- coding: utf-8 -*-
from tornado.gen import coroutine
import rethinkdb as r


# Match
# TeamA v.s. TeamB
# Start time
# End time
# score


@coroutine
def add_match(conn, teama, teamb, start):
    insert = yield r.table('matches').insert({
            'teama': teama,
            'teamb': teamb,
            'start': start,
            'end': 0,
            'score': '0-0'
        }).run(conn)
    return insert


@coroutine
def get_match(conn, teama, teamb, start):
    """Returns True if withdrawal goes through, False if not."""
    data = yield r.table('matches').filter(r.row['teama'] == teama and
                                           r.row['teamb'] == teamb and
                                           r.row['start'] == start).run(conn)
    return data


def get_round(score):
    teama_score, teamb_score = score.split('-')
    return int(teama_score) + int(teamb_score)
