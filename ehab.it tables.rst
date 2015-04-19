Users Table
    Every User has a:
        usernamename
        password
        funds

Wagers Table
    user id
    amount wagered
    match
    team
    match_complete boolean
    timestamp wager made
    timestamp wager resolved

bet on match winner
bet on round winner
bet on clutch or choke moments

Wager that a Team will Win a match Table
    Every Wager has a:
        User
        Amount Wagered
        Match
        Team
        Complete boolean


Matches Table
    Every Match has a:
        Game Time
        2 Teams
        status - pre-game, playing, completed
        victor


Teams Table
    Every Team has a:
        name
        5 players
        score


Players Table
    Every Player has a:
        name
        kills
        deaths
        assists
        score
        mvps