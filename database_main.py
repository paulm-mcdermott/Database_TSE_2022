import mysql.connector
import random
import table_creation_strings
from datetime import datetime, timedelta
from fill_tables import *
import constants
import os

# NOTE: The current file is set up to connect to our local mysql servers, and is currently written assuming that the database already exists (note the 'database =' parameter
# in the connector). To be run on a new mysql server, you will need to fill in the host and user parameters in the connector, and add a password field if your mysql user has
# a password. Once the database exists, you can use the database parameter in the connector as well. To create the database, you can either create it directly in mysql (this is what
# we did), or execute the CREATE DATABASE line. Note that if you try to execute CREATE DATABASE line when the database already exists, it will prevent the script from running. Also,
# if you have already created the tables, then you will need to activate the DROP tables command (currently commented out) to get the file to run. This is because the script will
# halt at table creation due to the fact that tables already exist. Last note, in order to execute the commands to mysql server, you need to run the command my_cursor.commit() (currently
# commented out at the end of the file). If you do not run this command, the mysql server will not reflect the commands in this script.


# make mysql connection
my_connection = mysql.connector.connect(
  host = os.environ['DATABASE_TSE2022_HOST'],
  user = os.environ['DATABASE_TSE2022_USER'],
  database = os.environ['DATABASE_TSE2022_DATABASE']
)

# check connection
print(my_connection)

# create cursor
my_cursor = my_connection.cursor(buffered=True)

# current file assumes that database is already made. If you are running from a fresh file, you need to run this line to create the database.
# my_cursor.execute("CREATE DATABASE DatabaseTSE2022")

# drop statement is needed if the tables already exist, and you want to reset them. Need to set foreign key checks to zero to successfully drop table.
# my_cursor.execute("SET FOREIGN_KEY_CHECKS = 0") # in order to drop tables, foreign key checks must be 0
# my_cursor.execute("DROP table Nurse, Inhabitant, ContactPerson, Session, UserSN, Visit, Participation, Prescribing, Comments, Declaring, Recommending, Following, Liking")

# create all the mysql tables
my_cursor.execute(table_creation_strings.create_activity)
my_cursor.execute(table_creation_strings.create_contact)
my_cursor.execute(table_creation_strings.create_nurse)
my_cursor.execute(table_creation_strings.create_medication)
my_cursor.execute(table_creation_strings.create_inhabitant)
my_cursor.execute(table_creation_strings.create_session)
my_cursor.execute(table_creation_strings.create_userSN)
my_cursor.execute(table_creation_strings.create_comments)
my_cursor.execute(table_creation_strings.create_visit)
my_cursor.execute(table_creation_strings.create_participation)
my_cursor.execute(table_creation_strings.create_declaring)
my_cursor.execute(table_creation_strings.create_recommending)
my_cursor.execute(table_creation_strings.create_following)
my_cursor.execute(table_creation_strings.create_liking)
my_cursor.execute(table_creation_strings.create_prescribing)

# fill the first several tables, need to fill in order due to table dependencies
fill_skill_activities(my_cursor,constants.all_activities)
fill_contacts_tables(my_cursor,constants.first_names,constants.surnames,20)
fill_nurse_table(my_cursor,constants.first_names,constants.surnames,constants.nurse_addresses,10)
fill_medication_table(my_cursor,constants.medications)
fill_inhabitants_table(my_cursor, constants.female_names, constants.male_names, constants.surnames, 100, 100, constants.categories, constants.community_address)
fill_session_table(my_cursor, constants.sessions_start_date, constants.sessions_end_date, constants.session_times, 40, constants.session_durations)
fill_user_sn_table(my_connection, my_cursor, 0.6)

# note: this only fills the initial comment; those that are not responses. we can only fill responses once we have followers
fill_comments_table(my_cursor,constants.sn_start_date, constants.sn_end_date, 120)

# fill more tables
fill_visit_table(my_cursor,constants.first_visit_date, constants.last_visit_date, constants.reasons, constants.textual_remarks, 50)
fill_declaring_list(my_connection,my_cursor, constants.all_activities, 5)
fill_participation_table(my_connection, my_cursor, constants.num_sessions, 15)
fill_recommending_table(my_connection,my_cursor, constants.all_activities, 0.4, 3)
fill_following_table(my_connection, my_cursor, 0.03)
fill_liking_table(my_connection, my_cursor, 11)
fill_prescribing_table(my_connection, my_cursor, constants.first_visit_date, constants.last_visit_date, constants.medications, 3)

# this fills more entries into comments tables. they are responses to existing comments, and with the restriction that a user
# can only respond to a post of a user which they follow
fill_responses_comments_table(my_connection,my_cursor,0.2)

myresult = my_cursor.fetchall()

for x in myresult:
  print(x) 

# in order to actually update the database on the mysql server, you must commit the commands
# commented out because we don't want to recommit
# my_connection.commit()
