import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
def chart():
    objects = ('A1', 'A2', 'A3', 'A4', 'A5')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2]
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('aantal doden')
    plt.title('Top 5 gevaarlijkste snelwegen')
 
    plt.show()