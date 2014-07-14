import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np
import os

if __name__ == '__main__':

    # arange() is like range() but allows floats
    t = pylab.arange(-6, 6, 0.01)
    s = (1/(1 + pylab.exp(-t)))*(1-(1/(1 + pylab.exp(-t))))

    # set y axis limits
    pylab.ylim([-0.1, 0.4])

    # relu:     s = np.maximum(0,t)
    # logistic: s = 1/(1 + pylab.exp(-t))
    # sinus:    s = pylab.sin(2*pylab.pi*t)

    plt.plot(t, s)

    plt.xlabel('marginal evidence for feature')
    plt.ylabel('marginal P(feature is present)')
    # plt.title('Single-Input Logistic Sigmoid Neuron')
    plt.grid(True)
    plt.savefig("/home/alex/Git/pipe-classification/reports/activation_functions/images/.png")
    # plt.show()

