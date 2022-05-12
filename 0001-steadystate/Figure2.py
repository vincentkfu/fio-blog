#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def fig2():
    bw = [x/1024 for x in [
            36331520,
            36507648,
            37880824,
            37212160,
            36990976,
            36724596,
            36462592,
            36380188,
            36499456,
            36798464,
            38315435,
            38684444,
            36892672,
            36449889,
            37289984,
            37552816,
            37253120,
            37896192,
            37716820,
            37244928,
            38504040,
            39492164,
            37822464,
            37040304,
            36487168,
            37511168,
            37274010,
            36499091,
            37150720,
            36737024,
            37511815,
            37774222,
            37228908,
            36400688,
            38282634,
            38040728,
            36569088,
            ]]

    x = np.array(list(range(30)))
    y = np.array(bw[-30:])
    m1, b1 = np.polyfit(x, y, deg=1)
    x1 = [len(bw)-30, len(bw)-1]
    y1 = [b1, b1+29*m1]

    y = np.array(bw[0:30])
    m2, b2 = np.polyfit(x, y, deg=1)
    x2 = [0, 29]
    y2 = [b2, b2+29*m2]

    plt.clf()
    plt.plot(x1, y1, "-", label="slope = {:.2f}".format(m1))
    plt.plot(x2, y2, "--", label="slope = {:.2f}".format(m2))
    plt.plot(list(range(len(bw))), bw, ".")
    plt.ylabel("Bandwidth KiB/s")
    plt.xlabel("Time (seconds)")
    plt.title("Figure 2: Steady State Bandwidth Slope Example")
    plt.legend()
    plt.savefig('Figure2')

if __name__ == "__main__":

    matplotlib.use("Agg")
    fig2()
