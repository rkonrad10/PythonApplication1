import numpy as np
import matplotlib.pyplot as plt

def Generuj_pilu():

    # nastaven� parametr� sign�lu
    fs = 10      # vzorkovac� frekvence
    f = 1          # frekvence pilov�ho pr�b�hu
    t = 2         # d�lka sign�lu v sekund�ch
    A = 1          # amplituda

    # vytvo�en� �asov� osy
    time = np.arange(0, t, 1/fs)

    print(time)

    # vytvo�en� pilov�ho pr�b�hu
    signal = A * np.mod(f*time, 1)

    print(signal)

    # zobrazen� sign�lu
    plt.plot(time, signal)
    plt.xlabel('Cas [s]')
    plt.ylabel('Amplituda')
    plt.title('Pilovy prubeh s frekvenci 1 Hz')
    plt.show()