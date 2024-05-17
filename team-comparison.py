import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    #display all players
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)
    query = f"""SELECT t.Nickname AS Team, t.Conference, t.Division, 
    (
		SELECT
			IFNULL(SUM(CASE WHEN g1.Score1 > g1.Score2 THEN 1 ELSE 0 END), 0)
		FROM
			Game AS g1
		WHERE
			g1.TeamId1 = t.TeamId
	) +
	(
		SELECT
			IFNULL(SUM(CASE WHEN g2.Score2 > g2.Score1 THEN 1 ELSE 0 END), 0)
		FROM
			Game AS g2
		WHERE
			g2.TeamId2 = t.TeamId
	)AS TotalWins,
	(
		SELECT
			IFNULL(SUM(CASE WHEN g1.Score1 > g1.Score2 AND t1.Conference = t2.Conference THEN 1 ELSE 0 END), 0)
		FROM
			Game AS g1
		LEFT JOIN 
            Team AS t1 ON g1.TeamId1 = t1.TeamId
        LEFT JOIN 
            Team AS t2 ON g1.TeamId2 = t2.TeamId
        WHERE
            t1.TeamId = t.TeamId
	) +
	(
		SELECT
			IFNULL(SUM(CASE WHEN g2.Score2 > g2.Score1 AND t3.Conference = t4.Conference THEN 1 ELSE 0 END), 0)
		FROM
			Game AS g2
		LEFT JOIN 
            Team AS t3 ON g2.TeamId1 = t3.TeamId
        LEFT JOIN 
            Team AS t4 ON g2.TeamId2 = t4.TeamId
        WHERE
            t4.TeamId = t.TeamId
	) AS ConferenceWins
    FROM Team AS t
    GROUP BY t.Conference, t.Location, t.Nickname, t.Division, t.TeamId
    ORDER BY t.Conference, TotalWins DESC, ConferenceWins DESC, t.Nickname ASC;"""
    result = sql_db.execute_select(query)
    result = result.split("\n")
    print("<pre style='color:#FFEBCD;'>")
    print("<br/><br/>" + result[0].replace("lW", "l W").replace("eW", "e W") + "<br/>" + result[1] + "<br/>")
    for i in range(len(result) - 2):
        print(result[i + 2] + "<br/>")
    print('</pre>')
    sql_db.close_db()
    # close db
    sql_db.close_db()
except Exception as e:
    logging.error(traceback.format_exc())