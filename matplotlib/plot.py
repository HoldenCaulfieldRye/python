import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import os

if __name__ == '__main__':

    # arange() is like range() but allows floats
    t = pylab.arange(-6, 6, 0.01)
    s = np.maximum(0,t)

    # set y axis limits
    pylab.ylim([0,1.5])
    
    # logistic: s = 1/(1 + pylab.exp(-t))
    # sinus:    s = pylab.sin(2*pylab.pi*t)

    plt.plot(t, s)

    # plt.xlabel('Evidence for feature')
    # plt.ylabel('P(feature is present)')
    # plt.title('Single-Input Logistic Sigmoid Neuron')
    plt.grid(True)
    plt.savefig("/home/alex/Git/pipe-classification/reports/activation_functions/images/ReLU.png")
    # plt.show()

