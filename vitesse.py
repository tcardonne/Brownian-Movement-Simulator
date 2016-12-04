#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import *
from Tkinter import *
from pylab import hist, show, grid, xlabel, ylabel, title
from math import sqrt


def main():
    # Initial configuration by user
    while True:
        t_start = int(raw_input("Intervalle de temps - Début : "))
        if(type(t_start) is int and t_start >= 0):
            break
        else:
            print "Veuillez entrer un entier positif"

    while True:
        t_end = int(raw_input("Intervalle de temps - Fin : "))
        if(type(t_end) is int and t_start < t_end):
            break
        else:
            print "Veuillez entrer un entier positif strictement supérieur à %d" % t_start

    while True:
        iterations = int(raw_input("Nombre de répetitions : "))
        if(type(iterations) is int and iterations > 0):
            break
        else:
            print "Veuillez entrer un entier positif strictement supérieur à %d" % t_start

    # Total time
    T = t_end - t_start
    # Number of steps
    N = 10 * T  # 50 per seconds

    meanSpeeds = numpy.empty(N + 1)

    print "Calculating ..."
    for i in range(0, iterations):
        # Simulate positions
        x = simulate(N)

        # Position of n, at t_start
        Xn = x[0, 0]
        Yn = x[1, 0]
        # Position of m, at t_end
        Xm = x[0, N]
        Ym = x[1, N]

        # Calculate mean speed
        v = (sqrt((Xm - Xn)**2 + (Ym - Yn)**2)) / (t_end - t_start)

        meanSpeeds[i] = v

    print "OK. Drawing ..."
    # Draw an histogram of meanSpeeds
    hist(meanSpeeds, bins=N/2)
    title("Vitesse moyenne")
    xlabel("Vitesse")
    ylabel("Frequences")
    grid(True)
    show()

if __name__ == '__main__':
    main()
