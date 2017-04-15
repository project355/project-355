import psycopg2, psycopg2.extras, sys

# connextion
try:
    conn = psycopg2.connect("dbname='project3' user='postgres' password='root'")
except:
    print ("no connection")

# weg -> naam, gemiddelde file teverdenheid, gemiddelde wegdek tevredenheid 
ccn = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccn.execute("""SELECT naam, gft, gwt  FROM weg""")
except:
    print("I can't select weg")

# persson -> id_persoon, file teverdenheid, wegdek tevredenheid
ccar = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccar.execute("""SELECT id_persoon, ft, wt FROM persoon""")
except:
    print("I can't select persoon")

### weg (uit)###
def count_weg(naam):
    """select count(weg.naam)"""
    try:
        ccn.execute("SELECT count(naam) FROM weg where naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

def weg_naam():
    """select weg.naam"""
    try:
        ccn.execute("SELECT naam FROM weg")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

def weg_gft(naam):
    """select weg.gft on roadname"""
    try:
        ccn.execute("SELECT gft FROM weg WHERE naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

def weg_gwt(naam):
    """select weg.gwt on roadname"""
    try:
        ccn.execute("SELECT gwt FROM weg WHERE naam = '"+naam+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

### persoon (uit)###
def count_persoon():
    """select count(persoon.id_persoon)"""
    try:
        ccn.execute("SELECT count(id_persoon) FROM persoon")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

def persoon_id_persoon():
    """select persoon.id_persoon"""
    try:
        ccn.execute("SELECT id_persoon FROM persoon")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

def persoon_ft(id):
    """select persoon.ft on id_persoon"""
    try:
        ccn.execute("SELECT ft FROM persoon WHERE id_persoon = '"+id+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

def persoon_wt(id):
    """select persoon.wt on id_persoon"""
    try:
        ccn.execute("SELECT wt FROM persoon WHERE id_persoon = '"+id+"'")
    except Exception as error:
        return(error)
    conn.commit()
    result = ccn.fetchall()    for row in result:
        return row[0]

### weg (in)###
def insert_into_weg(weg, gft, gwt):
    """gemiddelde beoordeling importeren"""
    try:
        ccp.execute("""insert into weg(gft, gwt) values (%s, %s) WHERE naam === """ "'"+weg+"'", (gft, gwt))
    except Exception as error:
        return(error)
    conn.commit()

### persoon (in)###
def insert_into_persoon(weg, ft, wt):
    """beoordeling persoon importeren"""
    try:
        ccp.execute("""insert into persoon(id_persoon,weg, ft,wt) Values (nextval('id_persoon_sequence'),%s,%s) WHERE weg === """ "'"+weg+"'", (ft, wt))
    except Exception as error:
        return(error)
    conn.commit()