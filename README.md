# HBT_correlations

modifications to THERMINATOR2 simulator (https://therminator2.ifj.edu.pl/)
enabling comparision to ATLAS HBT radii measurements 
from: https://arxiv.org/abs/1704.01621

it contains: 
* modified fitting function
* scripts running fits and plotting against data collected by ATLAS in automatic way


## usage:

#### manually:
Scripts should be executed in following order:
```
$ python run_fits.py
$ python collect_data.py
$ python plotEmAll.py
```
to receive *.png output graphs from matplotlib for specific set of parameters. All these scripts read parameters from file "config" or any other passed as argument.

In order to include uncertainties as results obtained for different _rejectionRange_ values, one should run:
```
$ python run_fits
$ python collect_data
```
for three different _rejectionRange_. And then:
```
$ python txt2rootGraph
```
which writes output to ROOT format.

#### automatically:
To run fits and convert results with uncertainties into ROOT format:
```sh
$ python get_therm_results
```

#### comparision with ATLAS:
In order to plot results against ATLAS data:
```sh
$ root
```
and in ROOT:
```
root [0]  .L hbtCompareAll.C
root [1]  hbtCompareAll("01")
```
where "01" is centrality 0-1%.

## Input format:
#### therminator:
correlations_c01/\
|-- m0505\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- femtopipi1a.root\
|-- m1505\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- femtopipi1a.root\
|-- m1zero\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- femtopipi1a.root\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- femtopipi2a.root\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- femtopipi3a.root\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- femtopipi4a.root\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- femtopipi5a.root\

#### ATLAS data
File name format: "fig_23a_cent01.dat", which corresponds to figure 23 a) in ATLAS paper, centrality 0-1%.
Each file should contain coordinates for points (middles), upper-left and lower-right edges of uncertainties boxes (x-y), e.g.
```
# points
0.17	4.40
0.25	4.04
0.33	3.50
# upper left
0.14	4.66
0.22	4.24
0.30    3.70
# lower right
0.19	4.12
0.28	3.79
0.35    3.12
```




