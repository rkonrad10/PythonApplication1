import numpy as np
import matplotlib.pyplot as plt

def Generuj_pilu():

    # nastavení parametrù signálu
    fs = 10      # vzorkovací frekvence
    f = 1          # frekvence pilového prùbìhu
    t = 2         # délka signálu v sekundách
    A = 1          # amplituda

    # vytvoøení èasové osy
    time = np.arange(0, t, 1/fs)

    print(time)

    # vytvoøení pilového prùbìhu
    signal = A * np.mod(f*time, 1)

    print(signal)

    # zobrazení signálu
    plt.plot(time, signal)
    plt.xlabel('Cas [s]')
    plt.ylabel('Amplituda')
    plt.title('Pilovy prubeh s frekvenci 1 Hz')
    plt.show()