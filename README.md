# Get-Off-the-Ice
CSCI 603 - Computational Problem Solving - LAB 9

### Implementation

For the implementation portion of this assignment, you will write code that reads in a maze
from a file, constructs a graph, finds out from which squares you can escape and for those
squares from which you can escape, how quickly you can.

### File format

The pond will be given to you in a file with the following format. The first line consists of
three numbers: the height of the pond, the width of the pond, and the row in which the pond
can be escaped. The escape point will always be along the right side of the pond, and the
row number given will be 0 for the topmost row and increase from there downward. After
that, each row of the pond will be given with one character per square — . for ice and * for
rock — separated by spaces. For example, for the first pond given in problem solving, the
file would look like this:

5 5 1

. . * . .

. . . . .

. . . . .

. . . * .

. * . . .

### Internal representation

You should read in the pond and construct a graph (so that it can more efficiently searched
many times). Don’t forget to include a node for the escape point. You are free (and encouraged)
to use the graph code from lecture, with proper citation. It is on the course website
under the graph week (labelled with the link Lecture Code). You can modify any of the
code provided to suit your needs.

### Output

Once you have built your data, we would like to know which ice squares can escape, and
for each one, how quickly. Specifically, you should print this information out in order by the
number of steps in the shortest escape. For example, the output for the pond given in the
file above would look like this:

1: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]

2: [(2, 2), (2, 3), (2, 4)]

3: [(0, 3), (1, 3), (3, 4), (4, 4)]

4: [(1, 0), (4, 0), (1, 2), (4, 2), (4, 3)]

5: [(0, 0), (3, 0), (0, 2), (3, 2)]

6: [(0, 4)]

If there are starting squares for which you cannot escape the pond, those should appear after
the successful squares, in a single line like those given above, except that it starts with No
path.
