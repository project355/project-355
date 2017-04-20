import psycopg2, psycopg2.extras
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

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
    ccm.execute("select field10 as weg, count(field1) as dooie from mytable where field1 = '2015' and field10 like 'Rijksweg A%' group by weg order by dooie desc limit 5")
except Exception as error:
    print(error)
conn.commit()
result = ccm.fetchall()

d1, d2, d3, d4, d5 = 0,0,0,0,0
w1, w2, w3, w4, w5 = "", "", "", "", ""
# result 1
w1 = result[0][0] # weg
d1 = result[0][1] # dooie
# result 2
w2 = result[1][0] # weg
d2 = result[1][1] # dooie
# result 3
w3 = result[2][0] # weg
d3 = result[2][1] # dooie
# result 4
w4 = result[3][0] # weg
d4 = result[3][1] # dooie
# result 5
w5 = result[4][0] # weg
d5 = result[4][1] # dooie

print(d1, d2, d3, d4, d5)
print(w1, w2, w3, w4, w5)

########## end database ##########


def poi():
    objects = (w1, w2,w3, w4, w5)
    y_pos = np.arange(len(objects))
    performance = [d1,d2,d3,d4,d5]
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('aantal doden')
    plt.title('Top 5 gevaarlijkste snelwegen') 
    plt.show()   
