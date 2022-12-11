import mysql.connector
import random
import table_creation_strings
from datetime import datetime, timedelta

# make mysql connection
my_connection = mysql.connector.connect(
  host="localhost",
  user="pmcderm27",
  database="DatabasesProjectTSE"
)

# check connection
print(my_connection)

# create cursor
my_cursor = my_connection.cursor(buffered=True)
my_cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

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

###Fill activities table

# Define a list of common activities
activities = ["Hiking", "Biking", "Swimming", "Yoga", "Pilates", "Running", "Walking", "Tennis", "Golf", "Dancing", "Singing", "Acting", "Painting", 
"Drawing", "Sculpting", "Photography", "Cooking", "Baking", "Gardening", "Horseback riding", "Skydiving", "Paragliding"]

# Create a dictionary to store the activity information
activity_dict = {}

# Generate random information for each activity
for activity in activities:
    # Generate a random difficulty level between 1 and 5
    difficulty = random.randint(1, 5)

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
    my_cursor.execute("INSERT IGNORE INTO SkillActivity (ActivityName, Difficulty, Price) VALUES (%s, %s, %s)", (name, difficulty, price))

# we're going to create the names by randomly selecting from a list of first and last names, so we make lists of names to choose from
female_names = ["Emily", "Emma", "Madison", "Abigail", "Olivia", "Isabella", "Sophia", "Ava", "Charlotte", "Mia", "Amelia", "Evelyn", 
"Abby", "Ellie", "Harper", "Emily", "Avery", "Ella", "Grace", "Sofia", "Chloe", "Zoe", "Victoria", "Aubrey", "Scarlett", "Hannah", 
"Lily", "Aria", "Layla", "Riley", "Zoey", "Samantha", "Nora", "Leah", "Audrey", "Brooklyn", "Bella", "Violet", "Claire", "Savannah", 
"Allison", "Sydney", "Skylar", "Camila", "Natalie", "Solange"]

male_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", 
"Matthew", "George", "Donald", "Anthony", "Paul", "Mark", "Edward", "Steven", "Kenneth", "Andrew", "Brian", "Joshua", "Kevin", "Ronald",
"Timothy", "Jason", "Jeffrey", "Frank", "Gary", "Ryan", "Nicholas", "Eric", "Stephen", "Jacob", "Larry", "Jonathan", "Scott", "Raymond", 
"Justin", "Brandon", "Gregory", "Samuel", "Benjamin"]

surnames = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau", "Simon", "Laurent", 
"Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux", "Vincent", "Fournier", "Morel", "Girard", "Andre", "Leclerc", "Mercier", "Dupont", 
"Lambert", "Bonnet", "Francois", "Martinez", "Legrand", "Garnier", "Faure", "Rousseau", "Blanc", "Guerin", "Muller", "Henry", "Roussel", "Nicolas", 
"Perrin", "Morin", "Mathieu", "Clement"]

# some tables don't specify sex
first_names = female_names + male_names

# fill the contact table

# requires a phone number, so we create a function to generate a random french phone number
# generate a random French phone number
def generate_phone_number():
    # french phone numbers have the format "01 XX XX XX XX"
    return ("01 " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + " " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + " " + 
    str(random.randint(0, 9)) + str(random.randint(0, 9)))

# we'll create 20 contacts and add to the contacts table
for i in range(20):
  # get necessary items for entry
  first_name = random.choice(first_names)
  last_name = random.choice(surnames)
  phone_number = generate_phone_number()
  # use the INSERT statement to add the activity data to the database
  my_cursor.execute("INSERT IGNORE INTO ContactPerson (ContactName, ContactLastName, ContactPhoneNumber) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))

# fill the nurse table
# we'll make 3 addresses for their professional addresses. we can think of this as there being 3 nurse agencies
nurse_addresses = ['72 Rue des Arbres','302 Avenue de la Lune','93 Boulevard de la Mer']
# we'll create 15 nurses and add to the contacts table
for i in range(15):
  # get necessary items for entry
  first_name = random.choice(first_names)
  last_name = random.choice(surnames)
  phone_number = generate_phone_number()
  prof_address = random.choice(nurse_addresses)
  # use the INSERT statement to add the activity data to the database
  my_cursor.execute("INSERT IGNORE INTO Nurse (Surname, Name, NurseAddress, PhoneNb) VALUES (%s, %s, %s, %s)", (last_name, first_name, prof_address, phone_number))


# fill the medication table
# dictionary of common medications for the elderly, and their active ingredients
medications = {
    "Bayer Aspirin": "acetylsalicylic acid",
    "Advil" : "ibuprofen",
    "Zocor": "simvastatin",
    "Prinivil": "lisinopril",
    "Glucophage": "metformin",
    "Amoxil": "amoxicillin",
    "Lasix": "furosemide",
    "Levoxyl": "levothyroxine",
    "Lipitor": "atorvastatin",
}

for name, info in medications.items():
    # use the INSERT statement to add the activity data to the database
    my_cursor.execute("INSERT IGNORE INTO Medication (NameM, ActiveSubstance) VALUES (%s, %s)", (name, info))

# filling inhabitant table
# need existing random nurse id as foreign key
def get_rand_nurse():
  query = "SELECT NurseId FROM Nurse ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  my_cursor.execute(query)
  nurse_id_row = my_cursor.fetchone()
  return nurse_id_row[0]

# need existing random contact id as a foreign key
def get_rand_contact():
  query = "SELECT ContactId FROM ContactPerson ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  my_cursor.execute(query)
  contact_id_row = my_cursor.fetchone()
  return contact_id_row[0]

# need existing inhabitant id as foreign key
def get_rand_inhabitant():
  query = "SELECT InHabitantId FROM Inhabitant ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  my_cursor.execute(query)
  inhabitant_id_row = my_cursor.fetchone()
  return inhabitant_id_row[0]

# need existing activity as foreign key
def get_rand_activity():
  query = "SELECT Activity FROM SkillActivity ORDER BY RAND() LIMIT 1"
  # execute the SQL query
  my_cursor.execute(query)
  activity_name_row = my_cursor.fetchone()
  return activity_name_row[0]

# since inhabibants live in the same community, they will have the same address, but with different apartment numbers
# each inhabitant falls into a category
address_number = range(1,201)
address_numbers_f = random.sample(address_number,100)
address_numbers_m = random.sample(address_number,100)
community_address = '300 Rue des Fleurs'
categories = ['Senior','Adult','Young']

# make 100 female inhabitants
for i in range(100):
  # get necessary items for entry
  first_name = random.choice(female_names)
  last_name = random.choice(surnames)
  category = random.choice(categories)
  address = community_address + ' Appt. ' + str(address_numbers_f.pop())
  phone_number = generate_phone_number()
  gender = 'F'
  NurseId = get_rand_nurse()
  ContactId = get_rand_contact()
  
  # use the INSERT statement to add the activity data to the database
  my_cursor.execute("INSERT IGNORE INTO Inhabitant (LastName, FirstName, Category, Address, PhoneNumber, Gender, NurseId_Follows, ContactId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
  (last_name, first_name, category, address, phone_number, gender, NurseId, ContactId))

# make 100 male inhabitants
for i in range(100):
  # get necessary items for entry
  first_name = random.choice(male_names)
  last_name = random.choice(surnames)
  category = random.choice(categories)
  address = community_address + ' Appt. ' + str(address_numbers_m.pop())
  phone_number = generate_phone_number()
  gender = 'M'
  NurseId_Follows = get_rand_nurse()
  ContactId = get_rand_contact()

  # use the INSERT statement to add the activity data to the database
  my_cursor.execute("INSERT IGNORE INTO Inhabitant (LastName, FirstName, Category, Address, PhoneNumber, Gender, NurseId_Follows, ContactId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
  (last_name, first_name, category, address, phone_number, gender, NurseId, ContactId))

# filling the Sessions tables
# first challenge is dates, the following code generates a random date from Jan 1 2017 to Jan 1 2021
def generate_random_date():
  # Set the start and end dates for the date range
  start_date = datetime(2017, 1, 1)
  end_date = datetime(2022, 1, 1)

  # Calculate the number of days in the date range
  num_days = (end_date - start_date).days

  # Pick a random day within the date range
  random_day = random.randint(0, num_days)

  # Calculate the random date by adding the random number of days to the start date
  random_date = start_date + timedelta(days=random_day)

  # Format the random date as a string in the desired format
  random_date_str = random_date.strftime("%Y-%m-%d")
  return random_date_str

# now we will make sessions can start on the hour for 8 hours, and duration can either be 30 minutes or an hour
session_times = ['09:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00','17:00:00']
session_duration = [timedelta(minutes=30),timedelta(minutes=60)]

for i in range(15):
  # get necessary items for entry
  first_name = random.choice(first_names)
  last_name = random.choice(surnames)
  phone_number = generate_phone_number()
  prof_address = random.choice(nurse_addresses)
  # use the INSERT statement to add the activity data to the database
  my_cursor.execute("INSERT IGNORE INTO Nurse (Surname, Name, NurseAddress, PhoneNb) VALUES (%s, %s, %s, %s)", (last_name, first_name, prof_address, phone_number))



my_cursor.execute("SELECT * FROM Inhabitant")

""" my_cursor.execute("SELECT * FROM SkillActivity")
my_cursor.execute("SELECT * FROM ContactPerson")
my_cursor.execute("SELECT * FROM Nurse")
my_cursor.execute("SELECT * FROM Medication")
"""
myresult = my_cursor.fetchall()

for x in myresult:
  print(x) 

