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

    print("Open")
    query = f"SELECT * \
        FROM Player \
        JOIN Team ON Player.TeamId = Team.TeamId \
        WHERE Team.Nickname = '{team_nickname}'"
    result = sql_db.execute_select(query)
    print("Query")
    # Print the results if there are any
    if result:
        print("Players for Team: " + team_nickname + "<br/>")
        print("<pre style='color: #FFEBCD;'>")
        print(result)
        print('</pre>')
    else:
        print("No players found for Team: " + team_nickname)

    # Close database connection
    sql_db.close_db()


except Exception as e:
    logging.error(traceback.format_exc())
