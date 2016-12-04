#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import *
from Tkinter import *
from pylab import hist, show, grid, axis, xlabel, ylabel, title
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

        print v
        meanSpeeds[i] = v

    # Draw an histogram of meanSpeeds
    hist(meanSpeeds)
    title("Vitesse moyenne")
    xlabel("Vitesse")
    ylabel("Frequences")
    show()


    # # Mark the start and end points.
    # plot(x[0, 0], x[1, 0], 'go')
    # plot(x[0, -1], x[1, -1], 'ro')

    # # More plot decorations.
    # title('Mouvement 2D')
    # xlabel('x', fontsize=16)
    # ylabel('y', fontsize=16)
    # axis('equal')
    # grid(True)
    # show()

    # root = Tk()
    # root.title('Simulation mouvement particule')

    # root.mainloop()

if __name__ == '__main__':
    main()
