#!/usr/bin/env python3

import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def fig1():
    with open("iops_mean.json", "r") as bwfile:
        json_data = json.loads(bwfile.read())
        iops = [x/1024 for x in json_data["jobs"][0]["steadystate"]["data"]["iops"]]

    x = list(range(len(iops)))
    mean = sum(iops) / len(iops)

    plt.clf()
    plt.plot(x, iops, ".")
    plt.axline(xy1=(0, 1.02*mean), slope=0, label="mean + 2%", linestyle="--")
    plt.axline(xy1=(0, mean), slope=0, label="mean = {:.0f}".format(mean))
    plt.axline(xy1=(0, 0.98*mean), slope=0, label="mean - 2%", linestyle="-.")
    plt.ylabel("IOPS")
    plt.xlabel("Time (seconds)")
    plt.title("Figure 1: IOPS Mean Deviation Example")
    plt.legend(loc="upper right", bbox_to_anchor=(1, 0.95))
    plt.savefig('Figure1')

def fig2():
    with open("bw_slope.json", "r") as bwfile:
        json_data = json.loads(bwfile.read())
        bw = [x/1024 for x in json_data["jobs"][0]["steadystate"]["data"]["bw"]]

    x = np.array(list(range(len(bw))))
    y = np.array(bw)
    m, b = np.polyfit(x, y, deg=1)

    plt.clf()
    plt.axline(xy1=(0, b), slope=m, label="slope = {:.2f}".format(m))
    plt.plot(x, bw, ".")
    plt.ylabel("Bandwidth KiB/s")
    plt.xlabel("Time (seconds)")
    plt.title("Figure 2: Steady State Bandwidth Slope Example")
    plt.legend()
    plt.savefig('Figure2')

if __name__ == "__main__":

    matplotlib.use("Agg")
    fig1()
    fig2()
