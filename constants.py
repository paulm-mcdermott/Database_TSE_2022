from datetime import datetime, timedelta

# years for which the community h
sessions_start_date = datetime(2019, 1, 1)
sessions_end_date = datetime(2022, 1, 1)

# For Nurse, Contact, and Inhabitant tables
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

# For SkillActivity table
# list of all activities
all_activities = ["Hiking", "Biking", "Swimming", "Yoga", "Pilates", "Running", "Walking", "Tennis", "Golf", "Dancing", "Singing", "Acting", "Painting", 
"Drawing", "Sculpting", "Photography", "Cooking", "Baking", "Gardening", "Horseback riding", "Skydiving", "Paragliding"]

# For Nurse table
# we'll make 3 addresses for their professional addresses. we can think of this as there being 3 nurse agencies
nurse_addresses = ['72 Rue des Arbres','302 Avenue de la Lune','93 Boulevard de la Mer']

# For Medicine table
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

# For Inhabitants table
# inhabitants will share the main part of their address, and fall into categories
community_address = '300 Rue des Fleurs'
categories = ['Senior','Adult','Young']

# For Sessions table
# give date window in the form of start_date and end_date in datetime form
sessions_start_date = datetime(2019, 1, 1)
sessions_end_date = datetime(2022, 1, 1)

# now we will make sessions can start on the hour for 8 hours, and duration can either be 30 minutes or an hour
session_times = ['09:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00','17:00:00']
session_durations = [timedelta(minutes=30),timedelta(minutes=60)]
# number of sessions will be useful to have
num_sessions = 100

# For Comments table
# give date window for social media in the form of start_date and end_date in datetime form
sn_start_date = datetime(2019, 1, 1)
sn_end_date = datetime(2022, 1, 1)

# For Visits table
reasons = ['felt sick', 'annual check up', 'pregnancy health-check', 'post-natal check-up', 'sports injury', 
'surgery follow up', 'medication renewal', 'blood tests', 'skin issues', 'chronic illness check up', 'other',
'they are a virgo']
textual_remarks = ['all better','may prescribe medicine', '3 days to live', 'hypochondria',
'booked off work for a week', 'no exercise for two months', 'should begin to attend a physiotherapist',  'died during appointment',
'follow up appointment next week', 'blood tests completed, awaiting results']

# For visits table
# years for which the visits have occured
first_visit_date = datetime(2019, 1, 1)
last_visit_date = datetime(2022, 1, 1)