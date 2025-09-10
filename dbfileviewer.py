import sqlite3
import datetime as dt
connection = sqlite3.connect("userdata.db")
cursor = connection.cursor()
newTable = """CREATE TABLE IF NOT EXISTS Login(
   "Username" text,
   "Password" text,
   "UserID" INTEGER PRIMARY KEY,
   "AccountType" text,
   "Email" text
);"""
progressTable = """CREATE TABLE IF NOT EXISTS Progress(
   "Username" text PRIMARY KEY,
   "CompletedLevel" text,
   "Date" text
)"""
ownershipTable = """CREATE TABLE IF NOT EXISTS Ownership(
   "Username" text PRIMARY KEY,
   "ItemOwned" text,
   "Date" text,
   "CurrentBalance" text
)"""
userInfo = [("idk",12345678,1,"Normal","h")]
cursor.execute(newTable)
cursor.execute(progressTable)
cursor.execute(ownershipTable)
connection.commit()
for row in cursor.execute("SELECT * FROM Login"):
  print(row)
print("---------------------")
# for row in cursor.execute("SELECT * FROM Progress"):
#    print(row)
# print("---------------------")
# for row in cursor.execute("SELECT * FROM Ownership"):
#    print(row)