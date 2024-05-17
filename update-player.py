import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    # get arguments
    player_id = sql_db.sanatize_input(sys.argv[1])
    player_name = sql_db.sanatize_input(sys.argv[2])
    team_name = sql_db.sanatize_input(sys.argv[3])
    position = sql_db.sanatize_input(sys.argv[4])

    # open db
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)

    # search for team and player
    result = sql_db.execute_select("SELECT TeamId FROM Team WHERE Nickname = '" + team_name + "';")
    result = result.split("\n")
    if not (len(result) > 2):
        print("Couldn't Find Team " + team_name + "<br/><br/>")
    else:
        team_id = int(result[2].strip())
        # search for ID to make sure it can be updated
        result = sql_db.execute_select("SELECT PlayerId FROM Player WHERE PlayerId = " + player_id + ";")
        result = result.split("\n")
        if not (len(result) > 2):
            print("Couldn't Find Player ID: " + player_id + "<br/><br/>")
        else:
            sql_db.execute_update(f"""UPDATE Player
            SET Name = '{player_name}', TeamId = {team_id}, Position = '{position}'
            WHERE PlayerId = {player_id}""")

    #print players
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