import random
from datetime import datetime, timedelta
import mysql.connector

# several functions to help build out the necessary elements

# generate a random French phone number
def generate_phone_number():
    # french phone numbers have the format "01 XX XX XX XX"
    return ("01 " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + " " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + " " + 
    str(random.randint(0, 9)) + str(random.randint(0, 9)))

# need existing random nurse id as foreign key
def get_rand_nurse(cursor):
  query = "SELECT NurseId FROM Nurse ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  cursor.execute(query)
  nurse_id_row = cursor.fetchone()
  return nurse_id_row[0]

# need existing random contact id as a foreign key
def get_rand_contact(cursor):
  query = "SELECT ContactId FROM ContactPerson ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  cursor.execute(query)
  contact_id_row = cursor.fetchone()
  return contact_id_row[0]

# need existing random inhabitant id as foreign key
def get_rand_inhabitant(cursor):
  query = "SELECT InHabitantId FROM Inhabitant ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  cursor.execute(query)
  inhabitant_id_row = cursor.fetchone()
  return inhabitant_id_row[0]

# need existing random activity as foreign key
def get_rand_activity(cursor):
  query = "SELECT ActivityName FROM SkillActivity ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  cursor.execute(query)
  activity_name_row = cursor.fetchone()
  return activity_name_row[0]

def get_random_user(cursor):
  query = "SELECT LogIn FROM UserSN ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  cursor.execute(query)
  user_login_row = cursor.fetchone()
  return user_login_row[0]

# for generating a random date
def generate_random_date(start_date : datetime, end_date : datetime):
  # calculate the number of days in the date range
  num_days = (end_date - start_date).days

  # pick a random day within the date range
  random_day = random.randint(0, num_days)

  # calculate the random date by adding the random number of days to the start date
  random_date = start_date + timedelta(days=random_day)

  # format the random date as a string in the desired format
  random_date_str = random_date.strftime("%Y-%m-%d")
  return random_date_str

# get id, first name, and last name for all existing inhabitants
def get_inhabitant_info(connection):
  # create a unique cursor for this function
  inhabitant_cursor = connection.cursor(buffered=True)
  # define select statement to get id and name info from inhabitant table
  select_st = "SELECT InHabitantId, LastName, FirstName FROM Inhabitant"
  inhabitant_cursor.execute(select_st)
  inhabitant_list =[]
  # Iterate over the result set
  for (id, first_name, last_name) in inhabitant_cursor:
    # Print the values of the id, first_name, and last_name columns
    inhabitant_list.append([id, first_name, last_name])
  # close inhabitant cursor  
  inhabitant_cursor.close()
  # return list with inhabitant information
  return inhabitant_list

def get_all_logins(connection):
  # create a unique cursor for this function
  login_cursor = connection.cursor(buffered=True)
  # define select statement to get id and name info from login table
  select_st = "SELECT LogIn FROM UserSN"
  login_cursor.execute(select_st)
  login_list = []
  # Iterate over the result set
  for login in login_cursor:
    # Print the values of the id, first_name, and last_name columns
    login_list.append(login[0])
  # close login cursor  
  login_cursor.close()
  # return list with login information
  return login_list

# generates time of date in for '00:00:00'
def generate_random_time():
  hour=random.randint(0, 23)
  minute=random.randint(0, 59)
  second=random.randint(0, 59)
  time = str(hour) + ":" + str(minute) + ":" + str(second)
  return time

# gets all comment ids
def get_all_comment_ids(connection):
  # create a unique cursor for this function
  comment_cursor = connection.cursor(buffered=True)
  # define select statement to get id from comments table
  select_st = "SELECT CommentId FROM Comments"
  comment_cursor.execute(select_st)
  comment_list =[]
  # iterate over the result set
  for comment in comment_cursor:
    # print the values of the CommentId columns
    comment_list.append(comment[0])
  # close comment cursor  
  comment_cursor.close()
  # return list with comment ids
  return comment_list

# get comment id, datecomment, and login of who posted the comment, didn't want to modify the get comment id function
def get_all_comment_info(connection):
  # create a unique cursor for this function
  comment_info_cursor = connection.cursor(buffered=True)
  # define select statement to get id from comments table
  select_st = "SELECT CommentId, DateComment, LogIn FROM Comments"
  comment_info_cursor.execute(select_st)
  comment_info_list =[]
  # iterate over the result set
  for comment in comment_info_cursor:
    # print the values of the CommentId columns
    comment_info_list.append(list(comment))
  # close comment cursor  
  comment_info_cursor.close()
  # return list with comment ids
  return comment_info_list

# content for comments
def generate_comment_content():
  positive_words = ["amazing","beautiful","great","exciting","fantastic"]
  random_pos_word = random.choice(positive_words)
  comments = [f"This is {random_pos_word}!", "I love to swim!","How is everybody doing?","I'm eating nachos",f"what a {random_pos_word} occasion",f"that's {random_pos_word} news!",
  "should I see that movie?","have you been to Australia?","when is breakfast?","youtube videos are videos",f"{random_pos_word}"]
  return random.choice(comments)

# for each item in left list, between 0 and num_right items randomly selected from right list are joined and make a new list consisting of an
# element from left_list and an element from right list
def bind_lists(left_list,right_list,num_right):
  # the new list to be created
  binded_list = []
  # iterate over the items in the original list
  for item in left_list:
    # generate a random number between 0 and 5
    random_number = random.randint(0, num_right)
    # pick activities
    right_list_sample = random.sample(right_list,random_number)
    # add the item to the new list the number of times generated
    for i in range(random_number):
        binded_list.append([item,right_list_sample.pop(0)])

  # return the repeat list
  return binded_list

def get_followers(connection, login_id : str):
  # create a unique cursor for this function
  id_is_followed = login_id
  query = f"SELECT LogIn_Follows FROM Following WHERE LogIn_Is_Followed_by_ = '{id_is_followed}'"
  followers_cursor = connection.cursor(buffered=True)

  # we need a try except statement to handle if the login is not in the table
  try:
    # define select statement to get id from comments table
    followers_cursor.execute(query)
  except mysql.connector.Error as error:
    return f'Error: {error}'
  else:
    follower_list =[]
    # iterate over the result set
    for follower in followers_cursor:
      # add all followers to a list
      follower_list.append(follower[0])
    # close follower cursor  
    followers_cursor.close()
    # return list with followers
    return follower_list




