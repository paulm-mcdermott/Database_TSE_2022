# contains all the mysql commands to create tables
create_activity = """
    CREATE TABLE IF NOT EXISTS SkillActivity(
        ActivityName VARCHAR(50),
        Difficulty INT,
        Price DECIMAL(4,2),
        PRIMARY KEY(ActivityName)
    );
"""

create_contact = """
    CREATE TABLE IF NOT EXISTS ContactPerson(
      ContactId INT AUTO_INCREMENT PRIMARY KEY,
      ContactName VARCHAR(50),
      ContactLastName VARCHAR(50),
      ContactPhoneNumber VARCHAR(50)
    );
"""

create_nurse = """
    CREATE TABLE IF NOT EXISTS Nurse(
      NurseId INT AUTO_INCREMENT PRIMARY KEY,
      Surname VARCHAR(50),
      Name VARCHAR(50),
      NurseAddress VARCHAR(50),
      PhoneNb VARCHAR(50)
    );
"""

create_medication = """
    CREATE TABLE IF NOT EXISTS Medication(
      NameM VARCHAR(50),
      ActiveSubstance VARCHAR(50),
      PRIMARY KEY(NameM)
    );
"""

create_inhabitant = """
    CREATE TABLE IF NOT EXISTS Inhabitant(
      InHabitantId INT AUTO_INCREMENT PRIMARY KEY,
      LastName VARCHAR(50),
      FirstName VARCHAR(50),
      Category CHAR(50),
      Address VARCHAR(50),
      PhoneNumber VARCHAR(50),
      Gender VARCHAR(10),
      NurseId_Follows INT,
      ContactId INT,
      FOREIGN KEY(NurseId_Follows) REFERENCES Nurse(NurseId),
      FOREIGN KEY(ContactId) REFERENCES ContactPerson(ContactId)
    );
"""

create_session = """
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
"""

create_userSN = """
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
"""

create_comments = """
    CREATE TABLE IF NOT EXISTS Comments(
      CommentID INT AUTO_INCREMENT PRIMARY KEY,
      DateComment DATETIME,
      Content VARCHAR(140),
      CommentID_isCommentedBy INT,
      LogIn VARCHAR(50) NOT NULL,
      FOREIGN KEY(CommentID_isCommentedBy) REFERENCES Comments(CommentID),
      FOREIGN KEY(LogIn) REFERENCES UserSN(LogIn)
    );
"""

create_visit = """
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
"""

create_participation = """
    CREATE TABLE IF NOT EXISTS Participation(
      InHabitantId INT,
      SessionId INT,
      Rating INT,
      PRIMARY KEY(InHabitantId, SessionId),
      FOREIGN KEY(InHabitantId) REFERENCES Inhabitant(InHabitantId),
      FOREIGN KEY(SessionId) REFERENCES Session(SessionId)
    );
"""

create_declaring = """
    CREATE TABLE IF NOT EXISTS Declaring(
      ActivityName VARCHAR(50),
      LogIn VARCHAR(50),
      LevelD VARCHAR(50),
      PRIMARY KEY(ActivityName, LogIn),
      FOREIGN KEY(ActivityName) REFERENCES SkillActivity(ActivityName),
      FOREIGN KEY(LogIn) REFERENCES UserSN(LogIn)
    );
"""
create_recommending = """
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
"""

create_following = """
    CREATE TABLE IF NOT EXISTS Following(
      LogIn_Is_Followed_by_ VARCHAR(50),
      LogIn_Follows VARCHAR(50),
      PRIMARY KEY(LogIn_Is_Followed_by_, LogIn_Follows),
      FOREIGN KEY(LogIn_Is_Followed_by_) REFERENCES UserSN(LogIn),
      FOREIGN KEY(LogIn_Follows) REFERENCES UserSN(LogIn)
);
"""

create_liking = """
    CREATE TABLE IF NOT EXISTS Liking(
      LogIn VARCHAR(50),
      CommentID INT,
      PRIMARY KEY(LogIn, CommentID),
      FOREIGN KEY(LogIn) REFERENCES UserSN(LogIn),
      FOREIGN KEY(CommentID) REFERENCES Comments(CommentID)
);
"""

create_prescribing = """
    CREATE TABLE IF NOT EXISTS Prescribing(
      InHabitantId INT,
      NameM VARCHAR(50),
      Startingtime DATE,
      Duration INT,
      PRIMARY KEY(InHabitantId, NameM),
      FOREIGN KEY(InHabitantId) REFERENCES Inhabitant(InHabitantId),
      FOREIGN KEY(NameM) REFERENCES Medication(NameM)
);
"""