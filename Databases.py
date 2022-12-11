import mysql.connector
import random
import table_creation_strings
from datetime import datetime, timedelta
from fill_tables import *
import constants
import os


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
my_cursor.execute("SET FOREIGN_KEY_CHECKS = 0") # in order to drop tables, foreign key checks must be 0

# drop statement if needed
my_cursor.execute("DROP table Nurse, Inhabitant, ContactPerson, Session, UserSN, Visit, Participation, Prescribing, Comments, Declaring, Recommending, Following, Liking")

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

# fill comments table, must be filled in two parts. this part is just the initial comments
# TODO there is comment on comment functionality that needs to be built in, for now i'm setting is commented by to 1
# stages should be: set original comments, iterate through looking for followers, make a follower comment at a prob
fill_comments_table(my_cursor,constants.sn_start_date, constants.sn_end_date, 120)

# fill visit table
fill_visit_table(my_cursor,constants.first_visit_date, constants.last_visit_date, constants.reasons, constants.textual_remarks, 50)
fill_declaring_list(my_connection,my_cursor, constants.all_activities, 5)
fill_participation_table(my_connection, my_cursor, constants.num_sessions, 15)
fill_recommending_table(my_connection,my_cursor, constants.all_activities, 0.4, 3)
fill_following_table(my_connection, my_cursor, 0.03)
fill_liking_table(my_connection, my_cursor, 11)
fill_prescribing_table(my_connection, my_cursor, constants.first_visit_date, constants.last_visit_date, constants.medications, 3)

my_cursor.execute("SELECT * FROM Prescribing")

""" my_cursor.execute("SELECT * FROM SkillActivity")
my_cursor.execute("SELECT * FROM ContactPerson")
my_cursor.execute("SELECT * FROM Nurse")
my_cursor.execute("SELECT * FROM Medication")
"""
myresult = my_cursor.fetchall()

for x in myresult:
  print(x) 

