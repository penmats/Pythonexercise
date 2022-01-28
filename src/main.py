import sys
import sqlite3
import pandas as pd

# Validate number of arguments passed
n = len(sys.argv)
if n!=3:
   print("Invalid arguments passed.")
   sys.exit(1)


def chk_conn(conn):
    try:
        conn.cursor()
        return True
    except Exception as ex:
        return False

myconn= sqlite3.connect('warehouse.db')

# Check database connection
if chk_conn(myconn)!=True:
    print("Database does not exists")


# Read the json files and load data to dataframes

Posts =pd.read_json(sys.argv[1])
Votes =pd.read_json(sys.argv[2])

Postsdf=pd.DataFrame.from_dict(Posts, orient='columns')
Votesdf=pd.DataFrame.from_dict(Votes, orient='columns')


# Load dataframes to tables

Postsdf.to_sql("Poststbl",con=myconn,if_exists='replace')
Votesdf.to_sql("Votestbl",con=myconn,if_exists='replace')

# Calculate mean votes per post per week
cur = myconn.cursor()

# Number of votes
cur.execute("select count(*) from Poststbl p inner join Votestbl v on p.Id=v.PostId")
y=cur.fetchone()[0]
print(y)


# Number of posts
Totalposts=cur.execute("select count(distinct p.Id) from Poststbl p inner join Votestbl v on p.Id=v.PostId")
z=cur.fetchone()[0]
print(z)


# Number of weeks
Totalweeks=cur.execute("select count(distinct strftime('%W%Y',v.CreationDate)) from Poststbl p inner join Votestbl v on p.Id=v.PostId")
p=cur.fetchone()[0]
print(p)

Mean=((y/z)/p)
print("Mean of votes per post per week is",Mean)






