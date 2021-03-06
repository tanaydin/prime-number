#!/usr/bin/env python

import lib
import sys

import prettyplotlib as ppl
import numpy as np

import matplotlib.pyplot as plt

if __name__=='__main__':

    # Parse command line options
    if len(sys.argv)<=1:
        print "Please set loop numbers"
        sys.exit()

    # Vars
    n = int(sys.argv[1])
    div = 100
    step = n / div

    # With range
    x = np.arange(0,n+step,step)
    drawx = x[1:]
    primes = lib.primesfrom3to(n)

    # Compute histogram
    hist = np.histogram(primes,bins=x)
    y = hist[0]

    # # Fit
    coefficients = np.polyfit(np.log(drawx), y, 1)
    fit = np.poly1d(coefficients)

    # Graph
    fig, ax = ppl.subplots(1)
    plt.ylabel('Number primes')
    plt.xlabel('In (%s) range (Less than)' % lib.human_format(int(step)) )

    ppl.plot(x[1:], y, 'o', label='number primes')
    ppl.plot(x, fit(np.log(x)), "--", label="fit")

    # Change x axis label
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    fig.canvas.draw()
    labels = [lib.human_format(int(item.get_text())) for item in ax.get_xticklabels()]
    ax.set_xticklabels(labels)
    ax = plt.gca()

    ppl.legend()
    plt.grid()
    plt.show()
