# -*- coding: utf-8 -*-
from tornado.gen import coroutine
import rethinkdb as r


""" Match Manipulation Functions """


@coroutine
def add_match(conn, name, teama, teamb, start):
    insert = yield r.table('matches').insert({
            'id': name,
            'teama': teama,
            'teamb': teamb,
            'start': start,  # datetime
            'end': 0,  # datetime
            'score': '0-0',
            'live': False
        }).run(conn)
    return insert


@coroutine
def get_match(conn, name):
    """Returns True if withdrawal goes through, False if not."""
    data = yield r.table('matches').get(name).run(conn)
    return data


@coroutine
def get_all_matches(conn):
    data = yield r.table('matches').run(conn)
    return data


@coroutine
def toggle_match_live(conn, name):
    match = yield get_match(conn, name)
    yield r.table('matches').get(name).update({
        'live': not match['live']
    }).run(conn)


""" Score Manipulation Functions """


@coroutine
def update_score(conn, name, score):
    yield r.table('matches').get(name).update({
        'score': score
    }).run(conn)


def get_score_ints(score):
    return [int(x) for x in score.split('-')]


def get_rounds_completed(score):
    teama_score, teamb_score = get_score_ints(score)
    return teama_score + teamb_score


def get_current_round(score):
    return get_rounds_completed(score) + 1


def is_teama_winning(score):
    teama_score, teamb_score = get_score_ints(score)
    return teama_score > teamb_score


def is_teamb_winning(score):
    teama_score, teamb_score = get_score_ints(score)
    return teama_score < teamb_score


def is_a_tie(score):
    teama_score, teamb_score = get_score_ints(score)
    return teama_score == teamb_score
