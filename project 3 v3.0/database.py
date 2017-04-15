import psycopg2, psycopg2.extras, sys

# connextion
try:
    conn = psycopg2.connect("dbname='project3' user='postgres' password='root'")
except:
    print ("no connection")

# weg -> naam, gemiddelde file teverdenheid, gemiddelde wegdek tevredenheid 
ccw = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccw.execute("""SELECT naam, gft, gwt  FROM weg""")
except:
    print("I can't select weg")

# persson -> id_persoon, file teverdenheid, wegdek tevredenheid
ccp = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccp.execute("""SELECT id_persoon, ft, wt FROM persoon""")
except:
    print("I can't select persoon")

### weg (uit)###
def count_weg(naam):
    """select count(weg.naam)"""
    try:
        ccw.execute("SELECT count(naam) FROM weg where naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

def weg_naam():
    """select weg.naam"""
    try:
        ccw.execute("SELECT naam FROM weg")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

def weg_gft(naam):
    """select weg.gft on roadname"""
    try:
        ccw.execute("SELECT gft FROM weg WHERE naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

def weg_gwt(naam):
    """select weg.gwt on roadname"""
    try:
        ccw.execute("SELECT gwt FROM weg WHERE naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccw.fetchall()
    for row in result:
        return row[0]

### persoon (uit)###
def count_persoon():
    """select count(persoon.id_persoon)"""
    try:
        ccp.execute("SELECT count(id_persoon) FROM persoon")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

def persoon_id_persoon():
    """select persoon.id_persoon"""
    try:
        ccp.execute("SELECT id_persoon FROM persoon")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

def persoon_ft(id):
    """select persoon.ft on id_persoon"""
    try:
        ccp.execute("SELECT ft FROM persoon WHERE id_persoon = '"+id+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

def persoon_wt(id):
    """select persoon.wt on id_persoon"""
    try:
        ccp.execute("SELECT wt FROM persoon WHERE id_persoon = '"+id+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccp.fetchall()
    for row in result:
        return row[0]

### weg (in)###
def update_weg(weg, gft, gwt):
    """gemiddelde beoordeling importeren"""
    try:
        ccw.execute("""UPDATE weg SET gft = %s, gwt = %s WHERE naam === %s""" "'"+weg+"'", (gft, gwt))
    except Exception as error:
        return(error)
    conn.commit()

### persoon (in)###
def insert_into_persoon(weg, ft, wt):
    """beoordeling persoon importeren"""
    try:
        ccp.execute("""insert into persoon(id_persoon,weg, ft,wt) Values (nextval('id_persoon_sequence'),%s, %s,%s) """, (weg,ft, wt))
    except Exception as error:
        return(error)
    conn.commit()