import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    # get arguments
    player_name = sql_db.sanatize_input(sys.argv[1])
    team_name = sql_db.sanatize_input(sys.argv[2])
    position = sql_db.sanatize_input(sys.argv[3])

    #serch team list for team before adding
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)
    result = sql_db.execute_select("SELECT TeamId FROM Team WHERE Nickname = '" + team_name + "';")
    result = result.split("\n")
    if not (len(result) > 2):
        print("<p style='color:#FFEBCD;'>Couldn't find team " + team_name + "</p>")
    else:
        team_id = int(result[2].strip())
        sql_db.execute_update(f"""INSERT INTO Player (TeamId, Name, Position)
        VALUES ('{team_id}', '{player_name}', '{position}');""")
    # close db
    sql_db.close_db()
except Exception as e:
    logging.error(traceback.format_exc())