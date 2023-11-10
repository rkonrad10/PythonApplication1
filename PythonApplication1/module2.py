from math import radians
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def Generuj_pilu2():

    # definujeme parametry pilovitého prùbìhu
    amplituda = 1
    perioda = 10
    delka = 2 * perioda
    pocatek = 0
    krok = 0.1

    # https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    # generujeme hodnoty x
    x = np.linspace(pocatek, delka, int(delka/krok), endpoint=False)
    # print(x)

    # generujeme hodnoty y
    y = amplituda * np.abs(np.mod(x - perioda/2, perioda) - perioda/2)

    # print(y)
    # return
            
    # vykreslíme graf
    """
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pilovity prubeh')
    plt.grid()
    plt.show()
    """
    # provádíme FFT
    fft_vals = fft(y)
    freqs = fftfreq(len(y), krok)

    # vykreslíme graf pilovitého prùbìhu a jeho Fourierovu transformaci
    fig, axs = plt.subplots(2)
    fig.subplots_adjust(hspace=0.5)
    axs[0].plot(x, y)
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].set_title('Pilovity prubeh')
    axs[0].grid()

    axs[1].stem(freqs, np.abs(fft_vals))
    axs[1].set_xlabel('Frekvence [Hz]')
    axs[1].set_ylabel('Amplituda')
    axs[1].set_title('FFT')
    axs[1].grid()

    plt.show()





