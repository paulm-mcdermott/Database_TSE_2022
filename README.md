# Database_TSE_2022

This is code for a portion of my final project in my Databases course for my master's program. 

The goal is to implement a mysql database that represents a community living space. I use the python-mysql-connector to connect to a mysql server, to create the database, to create the tables, and to insert into the tables. Using python allows me to generate random data with which to fill the tables. For example, several tables require names. For this implementation, I have a list of many first names and a list of many surnames. I pull randomly from these lists when I need to insert (new) name information into a table. The inhabitants table, for example, utilizes this method. In general, the rest of the data generation follows this principle. There are some additional complexities; some table entries depend on other tables, for example, comments on the social network must be on actual posts, and the comment date must be after the post date.
