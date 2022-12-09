import mysql.connector
import random
import string

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


my_connection = mysql.connector.connect(
  host="localhost",
  user="pmcderm27",
  database="DatabasesProjectTSE"
)

print(my_connection)

my_cursor = my_connection.cursor(buffered=True)

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS ContactPerson(
      ContactId INT AUTO_INCREMENT PRIMARY KEY,
      ContactName VARCHAR(50),
      ContactLastName VARCHAR(50),
      ContactPhoneNumber VARCHAR(50)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS SkillActivity(
        ActivityName VARCHAR(50),
        Difficulty INT,
        Price DECIMAL(4,2),
        PRIMARY KEY(ActivityName)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Nurse(
      NurseId INT AUTO_INCREMENT PRIMARY KEY,
      Surname VARCHAR(50),
      Name VARCHAR(50),
      NurseAddress VARCHAR(50),
      PhoneNb INT
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Medication(
      NameM VARCHAR(50),
      ActiveSubstance VARCHAR(50),
      PRIMARY KEY(NameM)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inhabitant(
      InHabitantId INT AUTO_INCREMENT PRIMARY KEY,
      LastName VARCHAR(50),
      FirstName VARCHAR(50),
      Category CHAR(50),
      Address VARCHAR(50),
      PhoneNumber VARCHAR(50),
      Gender BINARY(50),
      NurseId_Follows INT,
      ContactId INT,
      FOREIGN KEY(NurseId_Follows) REFERENCES Nurse(NurseId),
      FOREIGN KEY(ContactId) REFERENCES ContactPerson(ContactId)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Session(
      SessionId INT AUTO_INCREMENT PRIMARY KEY,
      Dates DATE,
      StartingTime TIME,
      EndingTime TIME,
      ActivityName VARCHAR(50) NOT NULL,
      InHabitantId INT NOT NULL,
      FOREIGN KEY(ActivityName) REFERENCES SkillActivity(ActivityName),
      FOREIGN KEY(InHabitantId) REFERENCES Inhabitant(InHabitantId)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS UserSN(
      LogIn VARCHAR(50),
      Password VARCHAR(50),
      Pseudo VARCHAR(50),
      Email VARCHAR(50),
      InHabitantId INT NOT NULL,
      PRIMARY KEY(LogIn),
      UNIQUE(InHabitantId),
      FOREIGN KEY(InHabitantId) REFERENCES Inhabitant(InHabitantId)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Comments(
      CommentID INT AUTO_INCREMENT PRIMARY KEY,
      DateComment DATETIME,
      Content VARCHAR(140),
      CommentID_isCommentedBy INT,
      LogIn VARCHAR(50) NOT NULL,
      FOREIGN KEY(CommentID_isCommentedBy) REFERENCES Comments(CommentID),
      FOREIGN KEY(LogIn) REFERENCES UserSN(LogIn)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Visit(
      VisitId INT AUTO_INCREMENT PRIMARY KEY,
      DateVisit DATETIME,
      Duration INT,
      Reason CHAR(50),
      TextualRemark VARCHAR(200),
      BloodPressureSystolic INT,
      BloodPressureDiastolic INT,
      SugarLevel INT,
      InHabitantId INT NOT NULL,
      FOREIGN KEY(InHabitantId) REFERENCES Inhabitant(InHabitantId)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Participation(
      InHabitantId INT,
      SessionId INT,
      Rating INT,
      PRIMARY KEY(InHabitantId, SessionId),
      FOREIGN KEY(InHabitantId) REFERENCES Inhabitant(InHabitantId),
      FOREIGN KEY(SessionId) REFERENCES Session(SessionId)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Declaring(
      ActivityName VARCHAR(50),
      LogIn VARCHAR(50),
      LevelD VARCHAR(50),
      PRIMARY KEY(ActivityName, LogIn),
      FOREIGN KEY(ActivityName) REFERENCES SkillActivity(ActivityName),
      FOREIGN KEY(LogIn) REFERENCES UserSN(LogIn)
    );
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recommending(
      ActivityName VARCHAR(50),
      LogIn_is_recommended_by VARCHAR(50),
      LogIn_recommends VARCHAR(50),
      LevelR VARCHAR(50),
      PRIMARY KEY(ActivityName, LogIn_is_recommended_by, LogIn_recommends),
      FOREIGN KEY(ActivityName) REFERENCES SkillActivity(ActivityName),
      FOREIGN KEY(LogIn_is_recommended_by) REFERENCES UserSN(LogIn),
      FOREIGN KEY(LogIn_recommends) REFERENCES UserSN(LogIn)
);
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Following(
      LogIn_Is_Followed_by_ VARCHAR(50),
      LogIn_Follows VARCHAR(50),
      PRIMARY KEY(LogIn_Is_Followed_by_, LogIn_Follows),
      FOREIGN KEY(LogIn_Is_Followed_by_) REFERENCES UserSN(LogIn),
      FOREIGN KEY(LogIn_Follows) REFERENCES UserSN(LogIn)
);
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Liking(
      LogIn VARCHAR(50),
      CommentID INT,
      PRIMARY KEY(LogIn, CommentID),
      FOREIGN KEY(LogIn) REFERENCES UserSN(LogIn),
      FOREIGN KEY(CommentID) REFERENCES Comments(CommentID)
);
""")

my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Prescribing(
      InHabitantId INT,
      NameM VARCHAR(50),
      Startingtime DATE,
      Duration INT,
      PRIMARY KEY(InHabitantId, NameM),
      FOREIGN KEY(InHabitantId) REFERENCES Inhabitant(InHabitantId),
      FOREIGN KEY(NameM) REFERENCES Medication(NameM)
);
""")

# Fill activities table
# Iterate over the items in the activities dictionary
for name, info in activity_dict.items():
    # Get the difficulty and price for the activity
    difficulty = info["difficulty"]
    price = info["price"]
    print(name, price, difficulty)
    # Use the INSERT statement to add the activity data to the database
    my_cursor.execute("INSERT IGNORE INTO SkillActivity (ActivityName, Difficulty, Price) VALUES (%s, %s, %s)", (name, difficulty, price))

    
  
my_cursor.execute("SELECT * FROM SkillActivity")

myresult = my_cursor.fetchall()

for x in myresult:
  print(x)

