# 535-project2
It's a small world

# _**Group members:**_

Hardik Bhawsar  hardik_bhawsar@csu.fullerton.edu

Anvit Patil     anvit.patil@csu.fullerton.edu     

Praveen Singh   praveen.singh@csu.fullerton.edu



# _**Description:**_

The given project is the spin-off of the popular game “Six Degrees of Kevin Bacon” The Six Degrees of Kevin Bacon game is based upon the concept of six degrees of separation. This concept states that any two people on earth can be linked together through six or less acquaintances. For the Kevin Bacon game, the challenge is to find the shortest path possible between Kevin Bacon and another actor. Similarly, this project suggest us to find the shortest connection between the cast of two movies. The shortest connection can be either 1, 2, or greater than 2 or may be no connection at all. We assume that the name of each actor is a string, thus a cast is a set of strings, ordered in alphabetical order. But it does not matter whether they are listed alphabetically or not, but for simplicity, let’s list them in alphabetical order. 
The input will be a positive integer n > 2, and a list of n casts from which the first two sets are more significant, CAST[0] and CAST[1]. If the two casts CAST[0] and CAST[1] have at least one string in common, then the shortest connection is 1. If the two casts CAST[0] and CAST[1] do not have any string in common, then look for another cast in the list of n casts, let’s called it tempCast, such that CAST[0] and tempCast have a string in common, and CAST[1] and tempCast have a string common, then the shortest connection is 2. Else the shortest connection is greater than 2 or there is no connection.



# _**Output:**_ 

The shortest connection is 1 , then shortest connection and common string , if shortest connect = 2 , then shortest connection and connon list of cast connecting them , Otherwise display Connection > 2 or no connection


