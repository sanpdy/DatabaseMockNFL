import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    # get date
    date = sys.argv[1]
    date = sql_db.sanatize_input(date)
    date ='{}-{}-{}'.format(date[:4], date[4:6], date[6:8])
    #display all players
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)
    query = f"""SELECT t.Nickname AS "Team 1", t.Location AS "Team 1 Home Location", g.Score1 AS "Team 1 Score",
	CASE WHEN g.Score1 > g.Score2 THEN t.Nickname ELSE t2.Nickname END AS "Game Winner",
	g.Score2 AS "Team 2 Score", t2.Nickname AS "Team 2", t2.Location AS "Team 2 Home Location"
    FROM Team AS t
    LEFT JOIN Game AS g ON g.TeamId1 = t.TeamId
    LEFT JOIN Team AS t2 ON g.TeamId2 = t2.TeamId
    WHERE g.Date = '{date}';"""
    result = sql_db.execute_select(query)
    result = result.split("\n")
    print("<pre style='color: #FFEBCD;'>")
    print(f"<br/><b>Games on {date}:</b><br/>" + result[0] + "<br/>" + result[1] + "<br/>")
    for i in range(len(result) - 2):
        print(result[i + 2] + "<br/>")
    print('</pre>')
    sql_db.close_db()
    # close db
    sql_db.close_db()
except Exception as e:
    logging.error(traceback.format_exc())