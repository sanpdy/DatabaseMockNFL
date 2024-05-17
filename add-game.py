import sys
import traceback
import logging
import sql_db

mysql_username = 'amw137'
mysql_password = 'ga8Aega1'

try:
    # get arguments
    team_1 = sql_db.sanatize_input(sys.argv[1])
    team_1_score = sql_db.sanatize_input(sys.argv[2])
    team_2 = sql_db.sanatize_input(sys.argv[3])
    team_2_score = sql_db.sanatize_input(sys.argv[4])
    date = sql_db.sanatize_input(sys.argv[5])


    # open database
    sql_db.open_database('localhost', mysql_username, mysql_password, mysql_username)

    #serch team list for team_1 before adding
    result = sql_db.execute_select("SELECT TeamId FROM Team WHERE Nickname = '" + team_1 + "';")
    result = result.split("\n")
    if not (len(result) > 2):
        print("<p style='color:#FFEBCD;'>Couldn't Find Team " + team_1 + "</p>")
    else:
        team_id_1 = int(result[2].strip())

        # serch team list for team_1 before adding
        result = sql_db.execute_select("SELECT TeamId FROM Team WHERE Nickname = '" + team_2 + "';")
        result = result.split("\n")
        if not (len(result) > 2):
            print("<p style='color:#FFEBCD;'>Couldn't Find Team " + team_2 + "</p>")
        else:
            team_id_2 = int(result[2].strip())
            # add game
            sql_db.execute_update(f"""INSERT INTO Game (TeamId1, TeamId2, Score1, Score2, Date)
            VALUES ('{team_id_1}', '{team_id_2}', '{team_1_score}', '{team_2_score}', '{date}');""")
    # close db
    sql_db.close_db()
except Exception as e:
    logging.error(traceback.format_exc())