import psycopg2, psycopg2.extras
from pylab import *

########## start database ##########
try:
    conn = psycopg2.connect("dbname='project3' user='postgres' password='root'")
except:
    print ("no connection")

ccm = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccm.execute("""select * from mytable""")
except:
    print("I can't select mytable")

try:
    ccm.execute("select field4 as voertuig, field10 as weg from mytable where field1 = '2015' and field10 like 'Rijksweg%' ")
except Exception as error:
    print(error)
conn.commit()
result = ccm.fetchall()

auto, vrachtwagen, motor, overig = 0,0,0,0,
for row in result:
    if row[0] == "personenauto" or row[0] == "Personenauto":
        auto = auto + 1
    elif row[0] == "Vrachtauto" or row[0] == "Bestelauto":
        vrachtwagen = vrachtwagen + 1
    elif row[0] == "Motor":
        motor = motor + 1
    elif (row[0] != "personenauto" or row[0] == "Personenauto") and row[1] != "Motor" and row[1] != "Vrachtauto" :
        overig = overig + 1
print(auto, vrachtwagen, motor, overig)

########## end database ##########

X = auto
Y = vrachtwagen
Z = motor
Q = overig
totaal = X + Y + Z + Q
X_PRO = (X/totaal) * 100
Y_PRO = (Y/totaal) * 100
Z_PRO = (Z/totaal) * 100
Q_PRO = (Q/totaal) * 100

def poi():
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'auto', 'vrachtwagen', 'motor', 'overig'
    fracs = [X_PRO, Y_PRO, Z_PRO, Q_PRO]
    explode=(0, 0, 0, 0)

    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90)
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.

    title('Meest verongelukte voertuigen', bbox={'facecolor':'0.8', 'pad':5})
    show()