import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    #display all players
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)
    query = """SELECT p.PlayerId, t.Nickname AS Team, p.Name, p.position
    FROM Player p
    JOIN Team t ON p.TeamId = t.TeamId;"""
    result = sql_db.execute_select(query)
    result = result.split("\n")
    print('<pre>')
    print("<br/>Players:<br/>" + result[0] + "<br/>" + result[1] + "<br/>")
    for i in range(len(result) - 2):
        print(result[i + 2] + "<br/>")
    print('</pre>')
    sql_db.close_db()
    # close db
    sql_db.close_db()
except Exception as e:
    logging.error(traceback.format_exc())