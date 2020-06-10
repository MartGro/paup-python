## This is a quick intro in batch-processing phylogenetic data files with PAUP* and Python

### Denropy and PAUP*

__There is the possibility to run PAUP* with DendroPy__. (Documented here)[https://dendropy.org/primer/paup.html?highlight=paup] The thing is it didn't work out of the box for me, so I didn't really bother to do that properly. 

### Overview
The goal is to call PAUP* from a Python script to evaluate phylogenetic data both using both neighbor-joining and maximum parsimony.

In order to run, PAUP* relies on NEXUS-files. With a complete NEXUS-file you can run PAUP* with a single command using the non-interactive mode.

### Run PAUP* in the non-interactive mode in the command line

Step 1: Make sure that you can run PAUP* , i.e. your PAUP* installation is working. For me, typing ´paup4a166_ubuntu64´ in the terminal brings me to the interactive PAUP* mode.

<img src="figs/run_paup.png" alt="hi" class="inline"/>

You can quit PAUP* by typing ´q´

Step 2: Now that PAUP* is working, you can specify a NEXUS file that 



[link to a PAUP* intro from Berkeley.](http://ib.berkeley.edu/courses/ib200/2018/labs/04/lab04.pdf)
