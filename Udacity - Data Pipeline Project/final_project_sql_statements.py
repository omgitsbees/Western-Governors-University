class SqlQueries:
    game_session_table_insert = ("""
        SELECT
                md5(events.sessionid || events.start_time) session_id,
                events.start_time, 
                events.playerid, 
                events.duration, 
                events.location, 
                events.device
        FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, *
            FROM staging_game_sessions) events
    """)

    player_table_insert = ("""
        SELECT distinct playerid, username, email, level, experience
        FROM staging_players
    """)

    item_table_insert = ("""
        SELECT distinct itemid, name, type, rarity, value
        FROM staging_items
    """)

    inventory_table_insert = ("""
        SELECT distinct playerid, itemid, quantity
        FROM staging_inventory
    """)

    time_table_insert = ("""
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time), 
               extract(month from start_time), extract(year from start_time), extract(dayofweek from start_time)
        FROM game_sessions
    """)