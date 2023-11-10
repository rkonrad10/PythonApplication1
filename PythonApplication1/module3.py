import numpy as np
import matplotlib.pyplot as plt

def Generuj_sinus3():


    # definujeme parametry sinusového prùbìhu
    amplituda = 1
    frekvence = 2
    faze = 0
    delka = 2 * np.pi
    krok = 0.1

    # generujeme hodnoty x
    # x = np.arange(0, delka, krok)

    # generujeme hodnoty y
    # y = amplituda * np.sin(2 * np.pi * frekvence * x + faze)

    x = np.arange(0, 5*np.pi, krok)
    y = np.sin(x)
    
    # provedeme rychlou Fourierovu transformaci (FFT)
    fft_y = np.fft.fft(y)

    # vykreslíme graf sinusového prùbìhu a jeho FFT
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    axs[0].plot(x, y)
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].set_title('Sinusovy prubeh')

    # vypoèteme frekvence pro osu x
    frekvence_x = np.fft.fftfreq(len(y), krok)
    axs[1].plot(frekvence_x, np.abs(fft_y))
    axs[1].set_xlabel('Frekvence')
    axs[1].set_ylabel('Amplituda')
    axs[1].set_title('FFT sinusoveho prubehu')
    axs[1].set_xlim([0, 5]) # omezíme zobrazené frekvence na interval 0 až 5

    plt.tight_layout()
    plt.show()
   



