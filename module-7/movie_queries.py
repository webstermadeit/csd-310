# Aaron Crose
# Module 7.2

import mysql.connector
from mysql.connector import errorcode

config = {
"user": "root",
"password": "12qwaszx!@QWASZX",
"host": "127.0.0.1",
"database" : "movies",
"raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MysQl on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print ("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)



# select all fields for genre 
cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name FROM studio")
studios = cursor.fetchall()
print("Displaying Studio Records")
for studio in studios:
    print("Studio ID: {}\n Studio Name: {}\n".format(studio[0], studio[1])) #three fields



# select all fields for genre 
cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre")
genres = cursor.fetchall()
print("Displaying Genre Records")
for genre in genres:
    print("Genre ID: {}\n Genre Name: {}\n".format(genre[0], genre[1])) #three fields


# select short films
cursor = db.cursor()
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")
films = cursor.fetchall()
print("Displaying Short Film Records")
for film in films:
    print("Film Name: {}\n Film Runtime: {}\n".format(film[0], film[1])) #two fields

# film names by director
cursor = db.cursor()
cursor.execute("SELECT film_name, film_director FROM film GROUP BY film_director, film_name")
films = cursor.fetchall()
print("Displaying Director Records In Order")
for film in films:
    print("Film Name: {}\n Film Director: {}\n".format(film[0], film[1])) #two fields