## This is a quick intro in batch-processing phylogenetic data files with PAUP* and Python

### Denropy and PAUP*

__There is the possibility to run PAUP* with DendroPy__. [Documented here](https://dendropy.org/primer/paup.html?highlight=paup) 

The thing is it didn't work out of the box for me, so I didn't really bother to do that properly. 

### Overview
The goal is to call PAUP* from a Python script to evaluate phylogenetic data both using both neighbor-joining and maximum parsimony.

In order to run, PAUP* relies on NEXUS-files. With a complete NEXUS-file you can run PAUP* with a single command using the non-interactive mode.

### Run PAUP* in the non-interactive mode in the command line

Step 1: Make sure that you can run PAUP* , i.e. your PAUP* installation is working. For me, typing ´paup4a166_ubuntu64´ in the terminal brings me to the interactive PAUP* mode.

<img src="figs/run_paup.png" alt="hi" class="inline"/>

You can quit PAUP* by typing ´q´

Step 2: Now that PAUP* is working, you can specify a NEXUS file that does what you want. I only did very simple analyses, so there is not a lot of configuation going on. 

The two methods I used were maximum parsimony and neighbor joining. Here are minimal examples for those two things: 

**Minimal Maximum Parsimony**
*minimal_MP.nex*
```
#NEXUS

Begin data;
  dimensions ntax=5 nchar=10;
  format datatype=protein missing=? gap=-;
  matrix
    A       AAAMMMWWWW
    B       LLLYMMYVVV
    C       MMMKKKKKAA
    D       AMFFFSKKSS
    E       LLLKKKKKSS
    ;
end;

Begin Paup;
set criterion = parsimony;
hsearch addseq=random nreps=1000;
savetrees /file=INSERTFILEPATH format=newick
;

end;
```


[link to a PAUP* intro from Berkeley.](http://ib.berkeley.edu/courses/ib200/2018/labs/04/lab04.pdf)
