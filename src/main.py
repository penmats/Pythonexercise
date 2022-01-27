import json
import sqlite3
import pandas as pd

# with open('uncommitted/Posts.json') as f:
#      json.load(f)

Posts =pd.read_json ('uncommitted/Posts.json')
Votes =pd.read_json ('uncommitted/Votes.json')

Postsdf=pd.DataFrame.from_dict(Posts, orient='columns')
Votesdf=pd.DataFrame.from_dict(Posts, orient='columns')


con= sqlite3.connect('warehouse.db')

Postsdf.to_sql("Posts",con=con,if_exists='replace')
Votesdf.to_sql("Votes",con=con,if_exists='replace')


#
# con= sqlite3.connect('warehouse.db')
# colnames=[]
#
# for row in data:
#     colnames.extend(row.keys())
# con.execute(f"create table  if not exists test {tuple(set(colnames))}")
#
# cursor = con.cursor()
# for row in data:
#     keys = ','.join(row.keys())
#     question_marks = ','.join(list('?'*len(row)))
#     values = tuple(row.values())
#     # print('INSERT INTO test ('+keys+') VALUES ('+question_marks+')', values)
#     cursor.execute('INSERT INTO test ('+keys+') VALUES ('+question_marks+')', values)
#




# # read the json file
# data = json.loads(f.read())
#
# # Iterating through the json
# # list
# for i in data:
#     print(i)

# Closing file
# f.close()

