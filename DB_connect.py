import mysql.connector as sql
import check
mydb = sql.connect(
        host="localhost",
        user="root",
        passwd="root")
mycursor = mydb.cursor()
#this function checks if database exist or not, if not present it will create it else it will use the existing one
def create_tables():


    my_dbname = 'flood_relief'
    Affected_areas = 'affected_areas'
    Inventory = 'inventory'
    Rescued_People = 'rescued_people'

    #to check.check_dbandtable() checks if table exist or not
    val = check.check_dbandtable(my_dbname)

    # if condition, if database doesnot exist
    if val == False:
        mycursor.execute(f"CREATE DATABASE {my_dbname}")
        print('db created')
        mycursor.execute(f"USE {my_dbname}")
        mycursor.execute(f"CREATE TABLE {Affected_areas}(Pincode INT PRIMARY KEY,Location VARCHAR(30),Population INT )")
        mycursor.execute(f"CREATE TABLE {Inventory}(Item_ID INT PRIMARY KEY,Item_Name VARCHAR(30),Quantity INT )")
        mycursor.execute(f"CREATE TABLE {Rescued_People}(R_Id INT PRIMARY KEY,Name CHAR(30),Age INT,Address VARCHAR(30))")
        print('tables created')
    #if database exist already
    else:
       print("table already exist")


def insert_into_table(insertsql,record):
    mycursor.execute("USE flood_relief")
    mycursor.execute(insertsql,record)
    mydb.commit()

def search_in_table(disp_sql):
    mycursor.execute("USE flood_relief")
    mycursor.execute(disp_sql)
    row = mycursor.fetchone()
    if row is not None:
        return row
    else:
        return False


