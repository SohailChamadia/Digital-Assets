import os
import time
import datetime

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'toor'
DB_NAME = 'assets'
BACKUP_PATH = '/backup/dbbackup/'

x=os.listdir(BACKUP_PATH)
print("Select backup to restore")
for items in x:
    print(items)
z=int(input())

TODAYBACKUPPATH = BACKUP_PATH + x[z-1]

print("Starting restore of database " + DB_NAME)

db = DB_NAME
os.chdir("C:\Program Files\MySQL\MySQL Server 5.7\\bin")
dumpcmd = "mysqldump -u " + DB_USER + " -h " + DB_HOST + " -p " + db + " < " + TODAYBACKUPPATH + "/" + db + ".sql"
os.system(dumpcmd)
