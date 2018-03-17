import os
import time
import datetime

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'toor'
DB_NAME = 'assets'
BACKUP_PATH = '/backup/dbbackup/'

DATETIME = time.strftime('%m%d%Y-%H%M%S')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME

if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

print("Starting backup of database " + DB_NAME)

db = DB_NAME
os.chdir("C:\Program Files\MySQL\MySQL Server 5.7\\bin")
dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " --password " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
os.system(dumpcmd)
