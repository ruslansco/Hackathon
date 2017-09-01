CCSCNE-2017: Programming Context April 7th, 2017

1.Smoots Problem

One of the most-celebrated units of measurement in some circles is the “smoot.” The smoot is
defined as the height of Oliver R. Smoot in October of 1958 when he was a student at the
Massachusetts Institute of Technology. He had a distinguished career after graduation and was
the chair of the American National Standards Institute (ANSI) for a year. 

Mr. Smoot was 5 feet, 7 inches tall in 1958. He was used to measure the Harvard Bridge in Boston which is 364.4 smoots
plus 1 ear. The Patroon Island Bridge over the Hudson River is 1795 feet. This is 321.5 smoots.

Write a program which will be given the length of a bridge in feet. You are to print the length of
the Bridge in smoots. Round the answer to one decimal digit.

Input
Your program will accept multiple test cases. Each test case will be an integer number of feet on
its own line. The program should terminate when a negative number is read.

Output
For each test case, the number of smoots rounded to one decimal digit on its own line. The
terminating case should not have any output associated with it.

Sample Input
1795
2030
-1

Sample Output
321.5
364.4


2. Indian Pearls Problem

In Victor Katz book on the history of mathematics, he gives an example of a problem from an
Indian source. A modified version of this goes like this:

An Indian princess was in her garden with five of her lady companions. She dropped her
pearl necklace and all the pearls fell to the ground. Each of her companions picked up
some proportion of the pearls but they missed some.
Later, her daughter went into the garden and picked up the remainder of the pearls. We
know how many pearls the daughter found and what proportion of the five companions
found. From this information, we ask you to write a program to give us the total number of
pearls in the necklace.

Input
Your program will accept multiple test cases, each on its own line. For each test case the input
will be six positive integers. The first integer will be how many pearls the daughter found. The
other five will represent the fractions found by the companions. For example, if a companion
found 1/10 of the pearls, we will input 10 and if a companion found 1/5 of the pearls, we will
input 5. We guarantee you that the sum of the fractions will be less than 1. The terminal input
will contain six 0s.

Output
You are to print the total number of pearls. The answer will always be an integer.

Sample Input
5 10 10 10 10 10
10 4 8 16 32 32
1228 5 7 10 15 8
0 0 0 0 0 0

Sample Output
10
20
3360
