import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="0000",
  host="127.0.0.1",
  port="5432"
)


print("Database opened successfully")
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS ADVERTISEMENT''')
cur.execute('''DROP TABLE IF EXISTS AUTO''')
cur.execute('''DROP TABLE IF EXISTS MODEL''')
cur.execute('''DROP TABLE IF EXISTS BRAND''')
cur.execute('''DROP TABLE IF EXISTS SELLER''')


cur.execute('''CREATE TABLE IF NOT EXISTS BRAND  
     (ID_OF_BRAND INT PRIMARY KEY NOT NULL,
     NAME_OF_BRAND CHAR(50));''')
print("Table BRAND - марка created successfully")

cur.execute('''CREATE TABLE IF NOT EXISTS MODEL  
     (ENGINE CHAR(50),
     SELECTOR CHAR(50),
     DRIVE CHAR(50),
     ID_OF_MODEL INT PRIMARY KEY NOT NULL,
     NAME_OF_MODEL CHAR(50),
     ID_OF_BRAND INT NOT NULL REFERENCES BRAND(ID_OF_BRAND));''')
print("Table MODEL - модель created successfully")

cur.execute('''CREATE TABLE IF NOT EXISTS AUTO  
     (VIN_NUMBER_OF_AUTO CHAR(50) PRIMARY KEY,
     AMOUNT_OF_FINES INT,
     COLOUR CHAR(50),
     YEAR_OF_RELEASE INT NOT NULL,
     MILEAGE INT,
     ID_OF_MODEL INT NOT NULL REFERENCES MODEL(ID_OF_MODEL));''')
print("Table AUTO - автомобиль created successfully")

cur.execute('''CREATE TABLE IF NOT EXISTS SELLER  
     (ID_OF_SELLER INT PRIMARY KEY NOT NULL,
     LOGIN CHAR(50),
     PASSWORD CHAR(50),
     FIO CHAR(50),
     TELEPHONE_NUMBER CHAR(50),
     RESIDENCE CHAR(50));''')
print("Table SELLER - продавец created successfully")

cur.execute('''CREATE TABLE IF NOT EXISTS ADVERTISEMENT  
     (STATE_NUMBER CHAR(50),
     SELLERS_COMMENT CHAR(200),
     ID_OF_ADVERTISEMENT INT PRIMARY KEY NOT NULL,
     NUMBER_OF_VIEWS INT,
     VIN_NUMBER_OF_AUTO CHAR(50) REFERENCES AUTO(VIN_NUMBER_OF_AUTO),
     ID_OF_SELLER INT NOT NULL REFERENCES SELLER(ID_OF_SELLER));''')
print("Table ADVERTISEMENT - объявление created successfully")


print("\nВнесение данных в таблицу BRAND - марка")
cur.execute(
  "INSERT INTO BRAND (ID_OF_BRAND,NAME_OF_BRAND) VALUES (1, 'AUDI')"
)
cur.execute(
  "INSERT INTO BRAND (ID_OF_BRAND,NAME_OF_BRAND) VALUES (2, 'BMW')"
)
cur.execute(
  "INSERT INTO BRAND (ID_OF_BRAND,NAME_OF_BRAND) VALUES (3, 'MERCEDES_BENZ')"
)
cur.execute(
  "INSERT INTO BRAND (ID_OF_BRAND,NAME_OF_BRAND) VALUES (4, 'TOYOTA')"
)
cur.execute(
  "INSERT INTO BRAND (ID_OF_BRAND,NAME_OF_BRAND) VALUES (5, 'NISSAN')"
)
print("Данные успешно внесены\n")


print("\nВнесение данных в таблицу MODEL - модель")
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('PETROL', 'AUTOMATIC', 'AWD', 11, 'A6', 1)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('PETROL', 'AUTOMATIC', 'AWD', 12, 'A8', 1)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('PETROL', 'AUTOMATIC', 'RWD', 21, 'M5', 2)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('DIESEL', 'AUTOMATIC', 'AWD', 22, 'X5', 2)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('PETROL', 'AUTOMATIC', 'RWD', 31, 'E-KLASSE', 3)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('PETROL', 'AUTOMATIC', 'RWD', 32, 'S-KLASSE', 3)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('PETROL', 'AUTOMATIC', 'FWD', 41, 'CAMRY', 4)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('DIESEL', 'AUTOMATIC', 'AWD', 42, 'LC200', 4)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('PETROL', 'MECHANIC', 'FWD', 51, 'ALMERA', 5)"
)
cur.execute(
  "INSERT INTO MODEL (ENGINE,SELECTOR,DRIVE,ID_OF_MODEL,NAME_OF_MODEL,ID_OF_BRAND) VALUES ('DIESEL', 'AUTOMATIC', 'AWD', 52, 'PARTFINDER', 5)"
)
print("Данные успешно внесены\n")


print("\nВнесение данных в таблицу AUTO - автомобиль")
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('WAUZZZ4G7FN123456', 0, 'WHITE', 2020, 15000, 11)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('WAUZZZ4G7FN123457', 1, 'BLACK', 2018, 45000, 12)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('WBAPN7C52AA778342', 1, 'GREEN', 2018, 42000, 21)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('WBAPN7C52AA778343', 0, 'BLUE', 2017, 50000, 22)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('WDB10702212008101', 1, 'GREEN', 2019, 40000, 31)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('WDB10702212008102', 1, 'BLACK', 2015, 75000, 32)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('JTDKB20U507848402', 0, 'WHITE', 2017, 150000, 41)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('JTDKB20U507848403', 0, 'BLACK', 2015, 75000, 42)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('SJNBAAP11U0289651', 0, 'GREY', 2015, 120000, 51)"
)
cur.execute(
  "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES ('SJNBAAP11U0289652', 1, 'BLACK', 2017, 60000, 52)"
)
print("Данные успешно внесены\n")


print("\nВнесение данных в таблицу SELLER - продавцы")
cur.execute(
  "INSERT INTO SELLER (ID_OF_SELLER,LOGIN,PASSWORD,FIO,TELEPHONE_NUMBER,RESIDENCE) VALUES (1111, 'IVAN', '11111', 'IVANOV IVAN IVANOVICH', '+111111', 'SAINTP')"
)
cur.execute(
  "INSERT INTO SELLER (ID_OF_SELLER,LOGIN,PASSWORD,FIO,TELEPHONE_NUMBER,RESIDENCE) VALUES (2222, 'VOVA', '22222', 'VLADIMIROV VLADIMIR VLADIMITOVICH', '+222222', 'MOSCOW')"
)
cur.execute(
  "INSERT INTO SELLER (ID_OF_SELLER,LOGIN,PASSWORD,FIO,TELEPHONE_NUMBER,RESIDENCE) VALUES (3333, 'KOLYA', '33333', 'NIKOLAEV NIKOLAI NIKOLAEVICH', '+333333', 'SAINTP')"
)
cur.execute(
  "INSERT INTO SELLER (ID_OF_SELLER,LOGIN,PASSWORD,FIO,TELEPHONE_NUMBER,RESIDENCE) VALUES (4444, 'VASYA', '44444', 'VASILYEV VASIKI VASILYEVICH', '+444444', 'MOSCOW')"
)
cur.execute(
  "INSERT INTO SELLER (ID_OF_SELLER,LOGIN,PASSWORD,FIO,TELEPHONE_NUMBER,RESIDENCE) VALUES (5555, 'PETYA', '55555', 'PETROV PETR PETROVICH', '+555555', 'NOVGOROD')"
)
print("Данные успешно внесены\n")


print("\nВнесение данных в таблицу ADVERTISEMENT - объявление")
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('A111AA', 'GOOD CAR', 1111111, 100, 'WAUZZZ4G7FN123456', 1111)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('B111BB', 'NORM CAR', 1111112, 150, 'WAUZZZ4G7FN123457', 1111)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('A222AA', 'BAD CAR', 2222222, 50, 'WBAPN7C52AA778342', 2222)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('B222BB', 'NORM CAR', 2222223, 70, 'WBAPN7C52AA778343', 2222)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('A333AA', 'BAD CAR', 3333333, 55, 'WDB10702212008101', 3333)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('B333BB', 'BEST CAR', 3333334, 75, 'WDB10702212008102', 3333)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('A444AA', 'GOOD CAR', 4444444, 65, 'JTDKB20U507848402', 4444)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('B444BB', 'BEST CAR', 4444445, 175, 'JTDKB20U507848403', 4444)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('A555AA', 'GOOD CAR', 5555555, 165, 'SJNBAAP11U0289651', 5555)"
)
cur.execute(
  "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES ('B555BB', 'BEST CAR', 5555556, 175, 'SJNBAAP11U0289652', 5555)"
)

print("Данные успешно внесены\n")


con.commit()
con.close()

