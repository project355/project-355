import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

X = 10
Y = 20
Z = 30
Q = 80
T = 10

X_naam = 'A1'
Y_naam = 'A1'
Z_naam = 'A1'
Q_naam = 'A1'
T_naam = 'A1'

def poi():
    objects = (X_naam, Y_naam,Z_naam, Q_naam, T_naam)
    y_pos = np.arange(len(objects))
    performance = [X,Y,Z,Q,T]
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('aantal doden')
    plt.title('Top 5 gevaarlijkste snelwegen')
 
    plt.show()

   
