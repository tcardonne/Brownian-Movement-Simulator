#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import *
from Tkinter import *
from pylab import plot, show, grid, axis, xlabel, ylabel, title


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

    # Total time
    T = t_end - t_start
    # Number of steps
    N = 10 * T  # 50 per seconds

    # Simulate positions
    x = simulate(N)

    # Plot the 2D trajectory.
    plot(x[0], x[1])

    # Mark the start and end points.
    plot(x[0, 0], x[1, 0], 'go')
    plot(x[0, -1], x[1, -1], 'ro')

    # More plot decorations.
    title('Mouvement 2D')
    xlabel('x', fontsize=16)
    ylabel('y', fontsize=16)
    axis('equal')
    grid(True)
    show()

if __name__ == '__main__':
    main()
