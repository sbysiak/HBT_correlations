import sys
from read_config import read_config
from plotter import plot


def plotEmAll(configuration):
    plot(configuration, 'rout_1a.dat', '23b')
    plot(configuration, 'rside_1a.dat', '24b')
    plot(configuration, 'rlong_1a.dat', '25b')
    plot(configuration, 'lambda_1a.dat', '29b')
    plot(configuration, 'routlong_1a.dat', '34a')

    plot(configuration, 'rout_m1zero.dat', '23a')
    plot(configuration, 'rside_m1zero.dat', '24a')
    plot(configuration, 'rlong_m1zero.dat', '25a')
    plot(configuration, 'lambda_m1zero.dat', '29a')
    plot(configuration, 'routlong_m1zero.dat', '34_kt')

if __name__ == '__main__':
    if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
    else: configuration = read_config()

    plotEmAll(configuration)


