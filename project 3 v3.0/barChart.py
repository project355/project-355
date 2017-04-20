import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

X = 10
Y = 20
Z = 30
Q = 80
T = 10

def poi():
    objects = ('A1', 'A2', 'A3', 'A4', 'A5')
    y_pos = np.arange(len(objects))
    performance = [X,Y,Z,Q,T]
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('aantal doden')
    plt.title('Top 5 gevaarlijkste snelwegen')
 
    plt.show()

   