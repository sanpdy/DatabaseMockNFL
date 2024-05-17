import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    if len(sys.argv) != 2:
        sys.exit(1)

    team_nickname = sys.argv[1]
    team_nickname = sql_db.sanatize_input(team_nickname)

    # Open database connection
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)

    games_wonlost_query = f'''
SELECT
    Team_Location,
    Team_Nickname,
    Opponent_Location,
    Opponent_Nickname,
    Date,
    Result,
    Team_Score,
    Opponent_Score
FROM (
    SELECT
        CASE
            WHEN t1.Nickname = '{team_nickname}' THEN t1.Location
            ELSE t2.Location
        END AS Team_Location,
        '{team_nickname}' AS Team_Nickname,
        CASE
            WHEN t1.Nickname = '{team_nickname}' THEN t2.Location
            ELSE t1.Location
        END AS Opponent_Location,
        CASE
            WHEN t1.Nickname = '{team_nickname}' THEN t2.Nickname
            ELSE t1.Nickname
        END AS Opponent_Nickname,
        g.Date,
        CASE
            WHEN (t1.Nickname = '{team_nickname}' AND g.Score1 > g.Score2) OR (t2.Nickname = '{team_nickname}' AND g.Score2 > g.Score1) THEN 'Won'
            WHEN (t1.Nickname = '{team_nickname}' AND g.Score1 < g.Score2) OR (t2.Nickname = '{team_nickname}' AND g.Score2 < g.Score1) THEN 'Lost'
            ELSE 'Draw'
        END AS Result,
        CASE
            WHEN t1.Nickname = '{team_nickname}' THEN g.Score1
            ELSE g.Score2
        END AS Team_Score,
        CASE
            WHEN t1.Nickname = '{team_nickname}' THEN g.Score2
            ELSE g.Score1
        END AS Opponent_Score
    FROM 
        Game g
    JOIN 
        Team t1 ON g.TeamId1 = t1.TeamId
    JOIN 
        Team t2 ON g.TeamId2 = t2.TeamId
    WHERE 
        t1.Nickname = '{team_nickname}' OR t2.Nickname = '{team_nickname}'
) AS TeamMatches
ORDER BY 
    Date;
'''

    result = sql_db.execute_select(games_wonlost_query)  # Adjust the function call

    # Print the results if there are any
    if result:
        print("Games for Team: " + team_nickname + "<br/>")
        print("<pre style='color:#FFEBCD;'>")
        print(result)
        print('</pre>')
    else:
        print("No games found for Team: " + team_nickname)

    # Close database connection
    sql_db.close_db()

except Exception as e:
    logging.error(traceback.format_exc())
