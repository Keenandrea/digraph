"""===========================================================================
author:  Keenan Andrea

date:    8.21.2019

class:   CMPSCI4500-002

purpose: to implement a game of circles and arrows and traversals that tests f
or a strongly connected diagraph. the game settings are pulled in from a .txt, 
and the game data is pushed onto a seperate .txt.

data structures:

external files:

==========================================================================="""
#============================================================================#
# function definition that passes two parameters 'a' and 'b', casts both into#
# sets, then withdraws the common members between sets a and b. if no common #
# members are found between the two data structures passed in, print report  #
#============================================================================#
def common_member(a,b):
    set_a = set(a)
    set_b = set(b)
    if(set_a & set_b):
        return(set_a & set_b)
    else:
        print('there were no common members found between the two given sets')
#============================================================================#
#============================================================================#

#============================================================================#
# Imagine we have a game-board. the following programming sets up the pieces #
# that is, the circles, the arrows, and the connections therein, all of which#
# will be pulled from the given input file, in this case 'HW1infile.txt      #
#============================================================================#
# set input text file as
# variable name 'infile'
infile = 'HW1infile.txt'

# read and store the first two lines
# of infile as N and K respectively,
# setting N as the number of circles
# and K as the number of arrows
N = int(open(infile).readlines()[0])
K = int(open(infile).readlines()[1])

# read and store the remaining lines in
# dictionary 'arrows' as key, value pai
# rs labeled tail, head where tail repr
# esents the source or backend of the a
# rrow and where head represents the de
# stination or pointed end of the arrow
# casting each tail, head pair as integ
# er values as the program moves along.
lines = open(infile).readlines()[2:N + 2]
arrows = {}
for pair in lines:
    (tail, head) = pair.split()
    arrows[int(tail)] = int(head)
#============================================================================#
#============================================================================#

#============================================================================#
# Before we go any further, error-checking. we will check if N is a number be#
# tween 2 and 10, if N has a sufficient number of arrows to be a strongly con#
# nected diagraph, and, lastly, if our diagraph is strongly connected        #
#============================================================================#
if ((N < 2) or (N > 10)) or (len(arrows) < N):
    print('Error: either N is not a positive',
          'int between 2 and 10, or there is',
          'an insufficient number of arrows.')
    exit()
#============================================================================#
#============================================================================#
    
#============================================================================#
#============================================================================#
nodes = [] 
for node in range(1,N+1):
    nodes.append(node)

tails = list(arrows.keys())
heads = list(arrows.values())
#============================================================================#
#============================================================================#

#============================================================================#
#============================================================================#
# function calls to 'common_member', which
# , in this case, port arguments heads and 
# nodes for common members, and once again 
# checking with arguments nodes and tails 
common_heads = common_member(nodes, heads)
common_tails = common_member(nodes, tails)

# if, elif, else blocks to
# test the viability of th
# e game board. 'if' the n
# umber of common arrow he
# ads does not equal the n
# umber of circles, that i
# s, does not contain an a
# rrow pointing to each ci
# rcle, the diagraph is no
# t strongly connected. th
# e same condition is supp
# orted in the 'elif' stat
# ement for number of tail
# s. if both the number of
# heads as well as the num
# ber of tails equal the n
# umber of circles, it fol
# lows that the diagraph i
# s strongly connected   
if len(common_heads) != N:
    print('diagraph is not fully connected, is missing an arrow to a node')
    exit()
elif len(common_tails) != N:
    print('diagraph is not fully connected, is missing an arrow from a node')
    exit()
else:
    print('diagraph is fully connected')
#============================================================================#
#============================================================================#

#============================================================================#
#============================================================================#
# syntactic shortcut using 'with' block to
# close the file at the end of the block s
# o you don't have to. the second argument
# 'w' will overwrite the file on each call
with open("HW1AndreaOutfile.txt", "w") as f:
    print("Game Stats\n==========", file=f)
    print("Number of circles: {}".format(N), file=f)
    print("Number of arrows: {}".format(K), file=f)
    print("Total number of marks: {}".format(len(heads)), file=f)
    print("Average number of marked circles: {}".format(len(heads)/N), file=f)
    print("Maximum number of marks on one circle: ", file=f)
    print("Open HW1AndreaOutfile for results.")
    print("That's all folks!")
#============================================================================#
#============================================================================#
