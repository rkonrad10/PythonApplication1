from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt

# https://docs.scipy.org/doc/scipy/tutorial/fft.html
import scipy

# import wikipedia  

# Seaching a title  
# import sys
# from chatgpt import Conversation

# import openai
# openai.api_key = "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"
# model_engine = "davinci"
# zmena2 vetev1

import module1
import module2
import module3

def main():

    # module1.Generuj_pilu()
    
    # pilovy prubeh  + fft
    # module2.Generuj_pilu2()

    # sinusovy prubeh + fft
    # module2.Generuj_pilu2()

    module3.Generuj_sinus3()



    return

    """
    from scipy.fft import fft, fftfreq
    import numpy as np
    # Number of sample points
    # N = 600
    N = 20
    # sample spacing
    # T = 1.0 / 800.0
    T = 20
    # x = np.linspace(0.0, N*T, N, endpoint=False)
    x = np.linspace(0.0, T, N, endpoint=False)
    # y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    y = x
    print(y)
    yf = fft(y)
    print(yf)
    xf = fftfreq(N, T)[:N//2]
    print(xf)
    import matplotlib.pyplot as plt
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.show()
    """


    """
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()
    """
    
    """
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    )
    """
    # vypiste vetev1
    """
    answer = response.choices[0].text.strip()
    print(answer)
    """

main()
