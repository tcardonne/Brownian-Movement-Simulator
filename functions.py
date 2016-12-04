#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy


def simulate(N):
    x = numpy.empty([2, N+1])
    x[:, 0] = 0.0

    for i in range(1, N+1):
        x[0, i] = numpy.random.randn()
        x[1, i] = numpy.random.randn()

    return x
