import peewee as pw

db=pw.MySQLDatabase("assets",
                    host="localhost",
                    port=3306,
                    user="root",
                    password="toor")
db.connect()

db.execute_sql("""create user 'admin' identified by 'admin';""")

db.execute_sql("""grant all privileges on *.* to 'admin' with grant option;""")

db.execute_sql("flush privileges;")

db.execute_sql("""create table authentication(
               user_name varchar(40) primary key NOT NULL,
               pwd varchar(40) NOT NULL,
               acs long
               );""")

db.execute_sql("""insert into authentication values('admin','admin','');""")

db.execute_sql("""create table item_master(
  items varchar(40) primary key);
  """)

db.execute_sql("""create table vendor(
  vendor_id varchar(40) primary key NOT NULL,
  vnd_name varchar(40),
  company_name varchar(40),
  address long,
  prefer_item long,
  company_url varchar(40),
  contact_no varchar(10),
  vendor_details long
);""")

db.execute_sql("""create table software_master(
  soft_id varchar(40) primary key,
  name varchar(40),
  type varchar(20),
  licenced numeric(3),
  licence_no varchar(40),
  price integer,
  vendor_details varchar(40),
  exp_date date,
  open_source numeric(3),
  soft_details long,
  FOREIGN KEY (vendor_details) REFERENCES vendor(vendor_id)
);""")

db.execute_sql("""create table department_master(
  department_id varchar(40) primary key,
  department_name varchar(40));
  """)

db.execute_sql("""create table staff_master(
  staff_id varchar(40) primary key ,
  staff_name varchar(40),
  desig varchar(40),
  phone varchar(10),
  email varchar(40),
  email2 varchar(40),
  address long,
  dept varchar(40),
  join_date date,
  FOREIGN KEY (dept) REFERENCES department_master(department_id)
);""")

db.execute_sql("""create table laboratory_master(
  lab_id varchar(40) primary key,
  department_id varchar(40),
  lab_name varchar(40),
  lab_incharge varchar(40),
  FOREIGN KEY (department_id) REFERENCES department_master(department_id),
  FOREIGN KEY (lab_incharge) REFERENCES staff_master(staff_id));
  """)

db.execute_sql("""create table user_master(
  user_id varchar(40) primary key ,
  staff_id varchar(40),
  pwd varchar(40),
  access_right long,
  FOREIGN KEY (staff_id) REFERENCES staff_master(staff_id)
);
""")

db.execute_sql("""create table purchase_order(
  id varchar(40) NOT NULL,
  purchase_no varchar(40) primary key NOT NULL,
  purchase_date date NOT NULL,
  vendor_id varchar(40),
  amount_tot integer,
  amount_given integer,
  feedback long,
  FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id)
);""")

db.execute_sql("""create table equipment(
  machine varchar(40) primary key,
  serial_no varchar(40),
  configuration long,
  type varchar(40),
  soft_support numeric(3),
  purchase date,
  vendor_details varchar(40),
  price integer,
  model varchar(40),
  department varchar(40),
  installation varchar(40),
  warranty date,
  responsible varchar(40),
  used_by long,
  issuable numeric(3),
  po_num varchar(40),
  machine_type varchar(40),
  remarks long,
  FOREIGN KEY (vendor_details) REFERENCES vendor(vendor_id),
  FOREIGN KEY (department) REFERENCES department_master(department_id),
  FOREIGN KEY (installation) REFERENCES laboratory_master(lab_id),
  FOREIGN KEY (responsible) REFERENCES staff_master(staff_id),
  FOREIGN KEY (po_num) REFERENCES purchase_order(purchase_no),
  FOREIGN KEY (type) REFERENCES item_master(items)
);""")

db.execute_sql("""create table item_issue (
  issue numeric(3),
  machine_id varchar(40),
  issue_date date,
  issued_by varchar(40),
  issued_to varchar(40),
  return_date date,
  return_on date,
  ret_accepted_by varchar(40),
  remark long,
  FOREIGN KEY (machine_id) REFERENCES equipment(machine)
);""")

db.execute_sql("""create table update_details(
  machine_id varchar(40),
  rep_date date,
  problem long,
  vendor_id varchar(40),
  cost integer,
  solution long,
  call_id varchar(40),
  FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id),
  FOREIGN KEY (machine_id) REFERENCES equipment(machine)
);""")

db.execute_sql("""create table transfer_details(
  machine_id varchar(40),
  transfer_date date,
  department varchar(40),
  FOREIGN KEY (machine_id) REFERENCES equipment(machine),
  FOREIGN KEY (department) REFERENCES department_master(department_id)
);""")

db.execute_sql("""create table amc(
  machine_id varchar(40),
  purchase_no varchar(40),
  start_date date,
  end_date date,
  vendor_id varchar(40),
  FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id),
  FOREIGN KEY (machine_id) REFERENCES equipment(machine),
  FOREIGN KEY (purchase_no) REFERENCES purchase_order(purchase_no)
);""")

for tables in db.get_tables():
    print(tables)

db.close()

print("Successful")
