# Use of While True Loop
import sqlite3 as lite

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(ID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,description TEXT,price TEXT,is_private BOOLEAN NOT NULL DEFAULT 1)"
                    )
        except:
            print("Database Error")

    def insert_data(self,data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                "INSERT INTO course(name,description,price,is_private) VALUES(?,?,?,?)",data
                )
                return True
        except:
            print("Data insertion Error")
    
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except:
            print("Data Reading Error")
            return False
    def delete_data(self,ID):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE ID = ?"
                cur.execute(sql,[ID])
                return True
        except:
            print ("Deletion Error")

#TODO: GUI For USER

def main():
    print("*"*40)
    print("\n :: Course Management ::\n")
    print("*"*40)
    print("\n")

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    db = DatabaseManage()

    print("\n Press 1. Insert a new course\n")
    print(" Press 2. Show all course\n")
    print(" Press 3. Delete a course[NEED ID OF COURSE]\n")
    print("#"*40)
    print("\n")

    while True:

        choice = input("\n Enter a choice: ")

        if choice == "1":
            name = input("\n Enter Course Name: ")
            description = input("\n Enter Course Descripton: ")
            price = input("\n Enter Course Price: ")
            private = input("\n Is this Course Private(0/1): ")

            if db.insert_data([name,description,price,private]):
                print("Course was inserted successfully\n")
            else:
                print("OOPS Something is Wrong\n")

        elif choice == "2":
            print("\n:: Course List :: ")
        
            for index, item in enumerate(db.fetch_data()):
                print("\nSerial No : "+str(index+1))
                print("Course ID: "+str(item[0]))
                print("Course Name: "+str(item[1]))
                print("Course Description: "+str(item[2]))
                print("Course Price: "+str(item[3]))
                private = "Yes" if item[4] else "No"
                print("Is Private: ",private)

                #print("\n")

        elif choice == "3":
            record_id = input("Enter the course ID: ")
            if db.delete_data(record_id):
                print("Course was Deleted with a success")
            else:
                print("OOPS Something went wrong")
        elif choice == "@":
            return False
        else: 
            print("\n BAD CHOICE ")

if __name__ == "__main__":
    main()