import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    # get date
    position = sql_db.sanatize_input(sys.argv[1])
    #display all players
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)
    query = f"""SELECT p.Name, t.Nickname AS Team
    FROM Player AS p
    JOIN Team AS t ON p.TeamId = t.TeamId
    WHERE p.position = '{position}';"""
    result = sql_db.execute_select(query)
    result = result.split("\n")
    print("<pre style='color: #FFEBCD;'>")
    print(f"<br/><b>{position} Players:</b><br/>" + result[0] + "<br/>" + result[1] + "<br/>")
    for i in range(len(result) - 2):
        print(result[i + 2] + "<br/>")
    print('</pre>')
    sql_db.close_db()
    # close db
    sql_db.close_db()
except Exception as e:
    logging.error(traceback.format_exc())