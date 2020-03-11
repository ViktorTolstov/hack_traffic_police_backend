import sqlite3

database = 'database.sqlite'

def init_db():
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("""
    CREATE table user (
        id integer primary key,
        name text
    );
    """)
    cursor.execute("""
    CREATE table violation (
        id integer primary key,
        geo_lat real,
        geo_long real,
        time_v number,
        car_number text,
        viol_type text,
        user_id integer,
        FOREIGN KEY (user_id) REFERENCES user (id)
    );
    """)
    connect.close()

# init_db()

def add_violation(geo_lat,geo_long,time_v,car_number,viol_type):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM violation")
    try:
        new_id = str(cursor.fetchall()[-1][0] + 1)
    except:
        new_id = 1
    cursor.execute("insert into violation values ("+str(new_id)+","+str(geo_lat)+","+str(geo_long)+","+str(time_v)+",'"+car_number+"','"+viol_type+"',0)")
    connect.commit()
    connect.close()

def get_db(table):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM "+table)
    result = cursor.fetchall()
    connect.close()
    return result

# def get_post():
#     connect = sqlite3.connect(database)
#     cursor = connect.cursor()
#     cursor = connect.cursor()
#     cursor.execute("SELECT id FROM posts")
#     # test_id = cursor.fetchall()[-1][0]
#     cursor.execute("SELECT * FROM posts")
#     res = cursor.fetchall()
#     connect.close()
#     posts = []
#     for i in range(0,len(res)):
#         res[i] = list(res[i])
#         text = res[i][1]
#         time = res[i][2]
#         date = str(res[i][3])
#         group = res[i][4]
#         attachments = get_attachment(res[i][0])
#         post = {
#             "text":text,
#             "attachments":attachments,
#             "time":time,
#             "date":date,
#             "group":group
#         }
#         posts.append(post)
#         posts_json ={"posts":posts}
#     return posts_json

# def get_attachment(post_id):
#     connect = sqlite3.connect(database)
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM attachment where post_id="+str(post_id))
#     res = cursor.fetchall()
#     connect.close()
#     attachments = []
#     for attachment in res:
#         attachments.append(attachment[1])
#     return attachments

# def update_group(group):
#     if group == "group2":
#         dialog = 2
#     elif group == "group3":
#         dialog = 3
#     elif group == "group4":
#         dialog = 4
#     elif group == "group5":
#         dialog = 5
#     connect = sqlite3.connect(database)
#     cursor = connect.cursor()
#     cursor.execute("SELECT id FROM posts")
#     last_id = cursor.fetchall()[-1][0]
#     cursor.execute("UPDATE posts SET dialog="+str(dialog)+" where id="+str(last_id))
#     connect.commit()
#     connect.close()

# def update_date(day,mounth,year):
#     new_date = str(datetime.date(int(year), int(mounth), int(day)))
#     connect = sqlite3.connect(database)
#     cursor = connect.cursor()
#     cursor.execute("SELECT id FROM posts")
#     last_id = cursor.fetchall()[-1][0]
#     cursor.execute("UPDATE posts SET date='"+new_date+"' where id="+str(last_id))
#     connect.commit()
#     connect.close()

# def update_time(post_time):
#     connect = sqlite3.connect(database)
#     cursor = connect.cursor()
#     cursor.execute("SELECT id FROM posts")
#     last_id = cursor.fetchall()[-1][0]
#     cursor.execute("UPDATE posts SET time='"+post_time+"' where id="+str(last_id))
#     connect.commit()
#     connect.close()

# update_date(11,11,1111)
# get_db("posts")