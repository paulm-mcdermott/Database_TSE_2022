import random
from utilities import *


# This file contains all functions that fill tables in the database

########################################
# Fill SkillActivity table
########################################

def fill_skill_activities(cursor, activities_list : list):
  # Create a dictionary to store the activity information
  activity_dict = {}

  # Generate random information for each activity
  for activity in activities_list:
      # Generate a random difficulty level between 1 and 5
      difficulty = random.randint(0, 5)

      # Generate a random price between 0 and 10
      price = round(random.uniform(0, 10),2)

      # Store the activity information in the dictionary
      activity_dict[activity] = {"difficulty": difficulty, "price": price}

  # iterate over the items in the activities dictionary
  for name, info in activity_dict.items():
      # get the difficulty and price for the activity
      difficulty = info["difficulty"]
      price = info["price"]
      
      # use the INSERT statement to add the activity data to the database
      cursor.execute("INSERT IGNORE INTO SkillActivity (ActivityName, Difficulty, Price) VALUES (%s, %s, %s)", (name, difficulty, price))

########################################
# fill ContactPerson tables
########################################

def fill_contacts_tables(cursor, first_names : list, surnames : list, num_generate : int):
    for i in range(num_generate):
        # get necessary items for entry
        first_name = random.choice(first_names)
        last_name = random.choice(surnames)
        phone_number = generate_phone_number()
        # use the INSERT statement to add the contact person data to the database
        cursor.execute("INSERT IGNORE INTO ContactPerson (ContactName, ContactLastName, ContactPhoneNumber) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))



########################################
# fill the Nurse table
########################################

def fill_nurse_table(cursor, first_names : list, surnames : list, nurse_addresses : list, num_nurses : int):
  for i in range(num_nurses):
    # get necessary items for entry
    first_name = random.choice(first_names)
    last_name = random.choice(surnames)
    phone_number = generate_phone_number()
    prof_address = random.choice(nurse_addresses)
    # use the INSERT statement to add the nurse data to the database
    cursor.execute("INSERT IGNORE INTO Nurse (Surname, Name, NurseAddress, PhoneNb) VALUES (%s, %s, %s, %s)", (last_name, first_name, prof_address, phone_number))

########################################
# fill Medication table
########################################
def fill_medication_table(cursor,medication_dict):
  for name, info in medication_dict.items():
    # use the INSERT statement to add the medicine data to the database
    cursor.execute("INSERT IGNORE INTO Medication (NameM, ActiveSubstance) VALUES (%s, %s)", (name, info))


########################################
# fill Inhabitants table
########################################
def fill_inhabitants_table(cursor, female_names : list, male_names : list, surnames : list, num_female : int, num_male : int, inh_categories : list, community_address : str):
	total_inhabitants = num_female + num_male
	address_number = range(1, total_inhabitants + 1)
	address_numbers_f = random.sample(address_number, num_female)
	address_numbers_m = random.sample(address_number, num_male)
	# make female inhabitants
	for i in range(num_female):
		# get necessary items for entry
		first_name = random.choice(female_names)
		last_name = random.choice(surnames)
		category = random.choice(inh_categories)
		address = community_address + ' Appt. ' + str(address_numbers_f.pop())
		phone_number = generate_phone_number()
		gender = 'F'
		NurseId_f = get_rand_nurse(cursor)
		ContactId = get_rand_contact(cursor)

  	# use the INSERT statement to add the inhabitant data to the database
		cursor.execute("INSERT IGNORE INTO Inhabitant (LastName, FirstName, Category, Address, PhoneNumber, Gender, NurseId_Follows, ContactId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
  	(last_name, first_name, category, address, phone_number, gender, NurseId_f, ContactId))

	# make 100 male inhabitants
	for i in range(num_male):
		# get necessary items for entry
		first_name = random.choice(male_names)
		last_name = random.choice(surnames)
		category = random.choice(inh_categories)
		address = community_address + ' Appt. ' + str(address_numbers_m.pop())
		phone_number = generate_phone_number()
		gender = 'M'
		NurseId_m = get_rand_nurse(cursor)
		ContactId = get_rand_contact(cursor)

		# use the INSERT statement to add the inhabitant data to the database
		cursor.execute("INSERT IGNORE INTO Inhabitant (LastName, FirstName, Category, Address, PhoneNumber, Gender, NurseId_Follows, ContactId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
		(last_name, first_name, category, address, phone_number, gender, NurseId_m, ContactId))

########################################
# fill Sessions table
########################################
def fill_session_table(cursor, start_date : datetime, end_date : datetime, session_times : list, num_sessions : int, session_durations : list):
	for i in range(num_sessions):
		# get necessary items for entry
		session_date = generate_random_date(start_date,end_date)
		starting_time_str = random.choice(session_times)
		starting_time = datetime.strptime(starting_time_str, "%H:%M:%S")
		duration = random.choice(session_durations)
		ending_time = str(starting_time + duration)
		activity_name = get_rand_activity(cursor)
		inhabitant_id = get_rand_inhabitant(cursor)
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Session (Dates, StartingTime, EndingTime, ActivityName, InHabitantId) VALUES (%s, %s, %s, %s, %s)", 
		(session_date, starting_time_str, ending_time, activity_name, inhabitant_id))



########################################
# fill UserSN table
########################################
def fill_user_sn_table(connection, cursor, account_likelihood : float):
	# all of the entries will need to be constructed on existing inhabitants
	inhabitant_list = get_inhabitant_info(connection)
	# probability that an inhabitant makes an account

	for i in inhabitant_list:
		inhabitant_id = i[0]
		last_name = i[1]
		first_name = i[2]
		# Login will be first name + last name + InhabitantId
		log_in = first_name + last_name + str(inhabitant_id)
		# password will be last name + random activity + inhabitantId
		password = last_name + str(get_rand_activity(cursor)) + str(inhabitant_id)
		#psuedo with be the same as log_in
		psuedo = log_in
		# email will be "firstname.lastname@fakemail.com"
		email = first_name + "." + last_name + "@fakemail.com"
		
		# not everyone will make an account, so we draw a probability for likelihood of making an account
		account_draw = random.uniform(0,1)
		if account_draw < account_likelihood:
			# use the INSERT statement to add the activity data to the database
			cursor.execute("INSERT IGNORE INTO UserSN (LogIn, Password, Pseudo, Email, InHabitantId) VALUES (%s, %s, %s, %s, %s)", 
			(log_in, password, psuedo, email, inhabitant_id))


########################################
# fill Comments table
########################################
# these are only initial comments, if it's original, response id is set to 0 TODO implement the responses
def fill_comments_table(cursor, start_date : datetime, end_date : datetime, num_comments : int):
	for i in range(num_comments):
		date = generate_random_date(start_date, end_date)
		time = generate_random_time()
		date_time = date + " " + time
		content = generate_comment_content()
		user_login = get_random_user(cursor)

		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Comments (DateComment, Content, CommentID_isCommentedBy, LogIn) VALUES (%s, %s, %s, %s)", 
		(date_time, content, 0, user_login)) # reminder, implement responses

########################################
# fill Visit table
########################################
def fill_visit_table(cursor, first_visit_date : datetime, last_visit_date : datetime, reason_list : list, remark_list, num_visits : int):
	for i in range(num_visits):
		date = generate_random_date(first_visit_date,last_visit_date)
		time = generate_random_time()
		date_time = date + " " + time
		duration = random.randint(20,30)
		reason = random.choice(reason_list)
		textual_remark = random.choice(remark_list)
		systolic = random.randint(100,150)
		diastolic = int(0.66*(systolic))
		sugar_level = random.randint(60,126)
		inhab_id = get_rand_inhabitant(cursor)
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Visit (DateVisit, Duration, Reason, TextualRemark, BloodPressureSystolic, BloodPressureDiastolic, SugarLevel, InHabitantId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
		(date_time, duration, reason, textual_remark, systolic, diastolic, sugar_level, inhab_id))

########################################
# fill Declaring table
########################################
def fill_declaring_list(connection, cursor, activities : list, max_declarations : int):
	sn_logins = get_all_logins(connection)
	sn_logins_declaring = bind_lists(sn_logins, activities, max_declarations)

	for item in sn_logins_declaring:
		login = item[0]
		activity = item[1]
		level_d = random.randint(0,5)
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Declaring (ActivityName, LogIn, LevelD) VALUES (%s, %s, %s)", 
		(activity, login, level_d))

########################################
# fill Participation table
########################################
def fill_participation_table(connection, cursor, num_sessions : int, max_attendance : int):
	inhabitant_id_list = []
	for item in get_inhabitant_info(connection):
		inhabitant_id_list.append(item[0])

	# reusing bind list, up to 15 inhabitants per session
	session_inhabitants = bind_lists(list(range(1,num_sessions+1)), inhabitant_id_list, max_attendance)

	for item in session_inhabitants:
		session_id = item[0]
		inhabitant_id = item[1]
		rating = random.randint(0,5)
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Participation (InHabitantId, SessionId, Rating) VALUES (%s, %s, %s)", 
		(session_id, inhabitant_id, rating))

########################################
# fill Recommending table
########################################
def fill_recommending_table(connection, cursor, activities : list, likelihood_recommend : float, max_user_recommend : int):
	#randomly sample from all the logins to choose which logins will have recommendations
	all_logins = get_all_logins(connection)
	recommended_logins = random.sample(all_logins,int(likelihood_recommend * len(all_logins)))

	# bind this sample with some activities
	recommended_with_activities = bind_lists(recommended_logins, activities, max_user_recommend)
	for item in recommended_with_activities:
		# choose recommender, difference is to prevent someone from recommending themselves
		recommender = random.choice(list(set(all_logins).difference(item[0])))
		item.append(recommender)

	for item in recommended_with_activities:
		recommended = item[0]
		activity = item[1]
		recommender = item[2]
		level_r = random.randint(0,5)
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Recommending (ActivityName, LogIn_is_recommended_by, LogIn_recommends, LevelR) VALUES (%s, %s, %s, %s)", 
		(activity, recommended, recommender, level_r))


########################################
# fill Following table
########################################
def fill_following_table(connection, cursor, prob_follow : float):
	all_logins = get_all_logins(connection)
	# create following, note that each follower,followed pair could exist twice, we do not allow this
	follow_pairs = []
	for follower in all_logins:
		for follows in all_logins:
			follow_draw = random.uniform(0,1)
			if prob_follow > follow_draw and follower != follows:
				follow_pairs.append([follower,follows])

	for item in follow_pairs:
		is_followed = item[1]
		follows = item[0]
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Following (LogIn_Is_Followed_by_,LogIn_Follows) VALUES (%s, %s)", 
		(is_followed,follows))


########################################
# fill Liking table
########################################
def fill_liking_table(connection, cursor, max_likes : int):
	all_comments = get_all_comment_ids(connection)
	all_logins = get_all_logins(connection)
	comments_liked_by = bind_lists(all_comments, all_logins, max_likes)

	for item in comments_liked_by:
		comment_id = item[0]
		user_likes = item[1]
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Liking (LogIn,CommentId) VALUES (%s, %s)", 
		(user_likes,comment_id))


########################################
# fill Prescribing table
########################################
def fill_prescribing_table(connection, cursor, first_prescription_date : datetime, last_prescription_date : datetime, medication_dict : dict, max_prescriptions : int):
	inhabitant_id_list = []
	for item in get_inhabitant_info(connection):
		inhabitant_id_list.append(item[0])
	# fill prescribing
	medications_list = medication_dict.keys()
	inhabitant_prescribed_meds = bind_lists(inhabitant_id_list,medications_list, max_prescriptions)
	prescription_mod = 0.4
	prescriptions = random.sample(inhabitant_prescribed_meds,int(prescription_mod*len(inhabitant_prescribed_meds)))

	# SQL insert
	for item in prescriptions:
		inhabitant_prescribed = item[0]
		medicine_prescribed = item[1]
		starting_date = generate_random_date(first_prescription_date,last_prescription_date)
		duration = random.randint(7,45)
		# use the INSERT statement to add the activity data to the database
		cursor.execute("INSERT IGNORE INTO Prescribing (InHabitantId, NameM, Startingtime, Duration) VALUES (%s, %s, %s, %s)", 
		(inhabitant_prescribed,medicine_prescribed,starting_date,duration))
