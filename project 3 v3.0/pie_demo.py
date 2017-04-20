from pylab import *


#uit de database: X = getal 1, Y = getal 2, Z = getal 3, Q = getal 4.



X = 1500 #auto
Y = 600 #vrachtwagen
Z = 900 #motor
Q = 10 #overig
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
    explode=(0, 0.05, 0, 0)

    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90)
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.

    title('Meest verongelukte voertuigen', bbox={'facecolor':'0.8', 'pad':5})

    show()
