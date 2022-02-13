
import psycopg2
from flask import Flask, render_template, request, redirect, url_for
import os
con = psycopg2.connect(
  database="deg3mejm6ogkqb",
  user="kzzmmyofisvjcy",
  password="87b9060c983ba8aadd645124d94806c31954efa110382624a4adc3c0ecaabde4",
  host="ec2-34-250-16-127.eu-west-1.compute.amazonaws.com",
  port="5432"
)


print("Database opened successfully")
cur = con.cursor()

app = Flask(__name__)

imgFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = imgFolder
img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ind.jpg')
img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'autor.jpg')
img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'reg.jpg')

@app.route('/')
def index():
    cur.execute("""SELECT * from brand,model,auto,advertisement
                WHERE BRAND.ID_OF_BRAND = MODEL.ID_OF_BRAND AND AUTO.ID_OF_MODEL = MODEL.ID_OF_MODEL AND AUTO.VIN_NUMBER_OF_AUTO = ADVERTISEMENT.VIN_NUMBER_OF_AUTO AND BRAND.NAME_OF_BRAND = 'AUDI';""")
    rowsa = cur.fetchall()

    cur.execute("""SELECT * from BRAND,MODEL,AUTO,ADVERTISEMENT
                WHERE BRAND.ID_OF_BRAND = MODEL.ID_OF_BRAND AND AUTO.ID_OF_MODEL = MODEL.ID_OF_MODEL AND AUTO.VIN_NUMBER_OF_AUTO = ADVERTISEMENT.VIN_NUMBER_OF_AUTO AND BRAND.NAME_OF_BRAND = 'BMW';""")
    rowsb = cur.fetchall()

    cur.execute("""SELECT * from BRAND,MODEL,AUTO,ADVERTISEMENT
                WHERE BRAND.ID_OF_BRAND = MODEL.ID_OF_BRAND AND AUTO.ID_OF_MODEL = MODEL.ID_OF_MODEL AND AUTO.VIN_NUMBER_OF_AUTO = ADVERTISEMENT.VIN_NUMBER_OF_AUTO AND BRAND.NAME_OF_BRAND = 'MERCEDES_BENZ';""")
    rowsm = cur.fetchall()

    cur.execute("""SELECT * from BRAND,MODEL,AUTO,ADVERTISEMENT
                WHERE BRAND.ID_OF_BRAND = MODEL.ID_OF_BRAND AND AUTO.ID_OF_MODEL = MODEL.ID_OF_MODEL AND AUTO.VIN_NUMBER_OF_AUTO = ADVERTISEMENT.VIN_NUMBER_OF_AUTO AND BRAND.NAME_OF_BRAND = 'TOYOTA';""")
    rowst = cur.fetchall()

    cur.execute("""SELECT * from BRAND,MODEL,AUTO,ADVERTISEMENT
                WHERE BRAND.ID_OF_BRAND = MODEL.ID_OF_BRAND AND AUTO.ID_OF_MODEL = MODEL.ID_OF_MODEL AND AUTO.VIN_NUMBER_OF_AUTO = ADVERTISEMENT.VIN_NUMBER_OF_AUTO AND BRAND.NAME_OF_BRAND = 'NISSAN';""")
    rowsn = cur.fetchall()

    return render_template('index.html', rowsa=rowsa, rowsb=rowsb, rowsm=rowsm, rowst=rowst, rowsn=rowsn, image = img1)





@app.route('/Autorization', methods=["POST", "GET"])
def autorization():
    cur = con.cursor()
    if request.method == 'POST' and request.form["name"].replace(" ", "") != '' and request.form["pass"].replace(" ", "") != '':
        login = request.form["name"]
        passw = request.form["pass"]
        cur.execute("SELECT * from SELLER")
        rowslog = cur.fetchall()
        for r in rowslog:
            if(login == (r[1].replace(" ", ""))) and (passw == (r[2].replace(" ", ""))):
                ident = int(r[0])
                return redirect(url_for('lk', ident = ident))


    return render_template('Autorization.html', image = img2)

@app.route('/lk/<ident>', methods=["POST", "GET"])
def lk(ident):

    cur = con.cursor()
    cur.execute("SELECT * from SELLER WHERE ID_OF_SELLER =  %s", [ident])

    rowslog = cur.fetchall()
    for r in rowslog:
            ident = int(r[0])
            fio = r[3]
            tnumber = r[4]
            resid = r[5]
    cur.execute("SELECT  * from AUTO,ADVERTISEMENT WHERE ID_OF_SELLER =  %s AND AUTO.VIN_NUMBER_OF_AUTO = ADVERTISEMENT.VIN_NUMBER_OF_AUTO", [ident])
    rowslk = cur.fetchall()
    if request.method == 'POST' and request.form['submit_1'] == "Изменить" and request.form["redact"] != 'Не выбрано':
        if request.form["redact"] == 'Изменить информацию о себе':
            return redirect(url_for('lkredactor', ident=ident))
        if request.form["redact"] == 'Добавить объявление':
            return redirect(url_for('avtoplus', ident=ident))
        if request.form["redact"] == 'Изменить существующее':
            return redirect(url_for('advred', ident=ident))

    return render_template('lk.html', ident = ident, fio=fio, rows =rowslk, resid = resid, tnumber = tnumber)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST' and request.form["login"].replace(" ", "") != '' and request.form["password"].replace(" ", "") != '' and request.form["fio"].replace(" ", "") != '' and request.form["telephone"].replace(" ", "") != '' and request.form["residence"].replace(" ", "") != '':
        cur.execute("SELECT * from SELLER")
        rowslog = cur.fetchall()
        for r in rowslog:
            id = (r[0])
        id = id + 1
        log = request.form["login"]
        pas = request.form["password"]
        fio = request.form["fio"]
        tel = request.form["telephone"]
        res = request.form["residence"]
        cur.execute(
            "INSERT INTO SELLER (ID_OF_SELLER,LOGIN,PASSWORD,FIO,TELEPHONE_NUMBER,RESIDENCE) VALUES (%s, %s, %s, %s, %s, %s)",
            (id, log, pas, fio, tel, res)
        )
        con.commit()
        return render_template('Autorization.html')

    return render_template('register.html', image=img3)

@app.route('/lkredactor/<ident>', methods=["POST", "GET"])
def lkredactor(ident):
    cur.execute("SELECT * from SELLER WHERE ID_OF_SELLER =  %s", [ident])
    rowslog = cur.fetchall()
    for r in rowslog:
            ident = int(r[0])
            fio = r[3]
            tnumber = r[4]
            resid = r[5]
    if request.method == 'POST' and request.form['submit_1'] == "Изменить" and (request.form["fio"]!= '' or request.form["telephone"] != '' or request.form["residence"] != 'Не выбрано'):
        if fio != request.form["fio"] and request.form["fio"]!= '':
            cur.execute("UPDATE SELLER SET FIO =  %s WHERE ID_OF_SELLER = %s", (request.form["fio"], ident))
            con.commit()
        if tnumber != request.form["telephone"] and request.form["telephone"] != '':
            cur.execute("UPDATE SELLER SET TELEPHONE_NUMBER =  %s WHERE ID_OF_SELLER = %s", (request.form["telephone"], ident))
            con.commit()
        if resid != request.form["residence"] and request.form["residence"] != 'Не выбрано':
            cur.execute("UPDATE SELLER SET RESIDENCE =  %s WHERE ID_OF_SELLER = %s", (request.form["residence"], ident))
            con.commit()


        return redirect(url_for('autorization'), 301)

    return render_template('lkredactor.html', fio = fio, tnumber = tnumber, resid = resid)

@app.route('/avtoplus/<ident>', methods=["POST", "GET"])
def avtoplus(ident):
    cur.execute("SELECT * from BRAND")
    rowslog = cur.fetchall()
    if request.method == 'POST' and request.form["bran"] != 'Не выбрано':
        bra = request.form["bran"]
        cur.execute("SELECT * from BRAND WHERE NAME_OF_BRAND =  %s", [bra])
        br = cur.fetchall()
        for r in br:
            idbr = (br[0][0])
        return redirect(url_for('avtoplusb', ident=ident, idbr = idbr))
    return render_template('avtoplus.html', ident = ident, rows = rowslog)

@app.route('/avtoplusb/<ident>/<idbr>', methods=["POST", "GET"])
def avtoplusb(ident, idbr):
    idbr = int(idbr)
    cur.execute("SELECT * from MODEL WHERE ID_OF_BRAND =  %s", [idbr])
    rows = cur.fetchall()
    cur.execute("SELECT NAME_OF_BRAND from BRAND WHERE ID_OF_BRAND =  %s", [idbr])
    nmbr = cur.fetchall()
    for r in nmbr:
        nambr = (nmbr[0][0])
    if request.method == 'POST' and request.form["model"] != 'Не выбрано':
        m = request.form["model"]
        cur.execute("SELECT * from MODEL WHERE NAME_OF_MODEL =  %s", [m])
        mm = cur.fetchall()
        for r in mm:
            identm = int(r[3])
        return redirect(url_for('avtopluss', ident=ident, identm=identm))

    return render_template('avtoplusb.html', ident = ident, nambr = nambr, rows = rows, idbr = idbr)

@app.route('/avtopluss/<ident>/<identm>', methods=["POST", "GET"])
def avtopluss(ident, identm):
    cur.execute("SELECT * from MODEL WHERE ID_OF_MODEL =  %s", [identm])
    rows = cur.fetchall()
    cur.execute("SELECT NAME_OF_BRAND from BRAND WHERE ID_OF_BRAND =  %s", [rows[0][5]])
    rowss = cur.fetchall()
    if request.method == 'POST' and request.form["vin"]!= '' and request.form["amount"]!= '' and request.form["col"]!= '' and request.form["year"]!= '' and request.form["mile"]!= '' and request.form["mile"]!= '' and request.form["state"]!= '' and request.form["comm"]!= '':
        vin = request.form["vin"]
        amount = request.form["amount"]
        col = request.form["col"]
        year = request.form["year"]
        mile = request.form["mile"]
        state = request.form["state"]
        comm = request.form["comm"]
        cur.execute(
            "INSERT INTO AUTO (VIN_NUMBER_OF_AUTO,AMOUNT_OF_FINES,COLOUR,YEAR_OF_RELEASE,MILEAGE,ID_OF_MODEL) VALUES (%s, %s, %s, %s, %s, %s)",
            (vin, amount, col, year, mile, identm)
        )
        con.commit()
        cur.execute("SELECT * from ADVERTISEMENT")
        rowssss= cur.fetchall()
        for r in rowssss:
            ide = (r[2])
        ide = ide + 1
        cur.execute(
            "INSERT INTO ADVERTISEMENT (STATE_NUMBER,SELLERS_COMMENT,ID_OF_ADVERTISEMENT,NUMBER_OF_VIEWS,VIN_NUMBER_OF_AUTO,ID_OF_SELLER) VALUES (%s, %s, %s, %s, %s, %s)",
            (state, comm, ide, 0, vin, ident)
        )
        con.commit()
        return redirect(url_for('index'), 301)

    return render_template('avtopluss.html', ident=ident, rows=rows, rowss = rowss)

@app.route('/advred/<ident>', methods=["POST", "GET"])
def advred(ident):
    cur.execute("SELECT  * from ADVERTISEMENT WHERE ID_OF_SELLER =  %s", [ident])
    rowslk = cur.fetchall()
    if request.method == 'POST' and request.form["redact"]!= 'Не выбрано':
        vinn = request.form["redact"]
        return redirect(url_for('advred1', vinn=vinn, ident = ident))
    return render_template('advred.html', ident = ident, rows = rowslk)

@app.route('/advred1/<vinn>/<ident>', methods=["POST", "GET"])
def advred1(vinn,ident):
    cur.execute("SELECT  * from ADVERTISEMENT WHERE VIN_NUMBER_OF_AUTO =  %s", [vinn])
    rows1 = cur.fetchall()
    for r in rows1:
        state = r[0]
        comm = r[1]
    cur.execute("SELECT  * from AUTO WHERE VIN_NUMBER_OF_AUTO =  %s", [vinn])
    rows2 = cur.fetchall()
    for r in rows2:
        amo = r[1]
        col = r[2]
        year = r[3]
        mileage = r[4]

    if request.method == 'POST' and (request.form["num"] != '' or request.form["com"] != '' or request.form["amon"] != '' or request.form["colo"] != '' or request.form["yea"] != '' or request.form["mile"] != ''):
        if state != request.form["num"] and request.form["num"] != '':
            cur.execute("UPDATE ADVERTISEMENT SET STATE_NUMBER =  %s WHERE VIN_NUMBER_OF_AUTO = %s", (request.form["num"], vinn))
            con.commit()
        if comm != request.form["com"] and request.form["com"] != '':
            cur.execute("UPDATE ADVERTISEMENT SET SELLERS_COMMENT =  %s WHERE VIN_NUMBER_OF_AUTO = %s", (request.form["com"], vinn))
            con.commit()
        if amo != request.form["amon"] and request.form["amon"] != '':
            cur.execute("UPDATE AUTO SET AMOUNT_OF_FINES =  %s WHERE VIN_NUMBER_OF_AUTO = %s", (request.form["amon"], vinn))
            con.commit()
        if col != request.form["colo"] and request.form["colo"] != '':
            cur.execute("UPDATE AUTO SET COLOUR =  %s WHERE VIN_NUMBER_OF_AUTO = %s", (request.form["colo"], vinn))
            con.commit()
        if year != request.form["yea"] and request.form["yea"] != '':
            cur.execute("UPDATE AUTO SET YEAR_OF_RELEASE =  %s WHERE VIN_NUMBER_OF_AUTO = %s", (request.form["yea"], vinn))
            con.commit()
        if mileage != request.form["mile"] and request.form["mile"] != '':
            cur.execute("UPDATE AUTO SET MILEAGE =  %s WHERE VIN_NUMBER_OF_AUTO = %s", (request.form["mile"], vinn))
            con.commit()
        return redirect(url_for('lk', ident=ident))

    return render_template('advred1.html', vinn=vinn, state=state, comm=comm, amo=amo, col=col, year=year, mileage=mileage)

if __name__ == "__main__":
    app.run(debug= True)






