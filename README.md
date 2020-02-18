# Monopoly-Game-
CMPSC HW3

Homework 3

21 February 2020

This is a continuation of the previous assignment, and introduces use of conditional decisions to solve some parts of the problem.  It is hoped that the previous assignment was designed flexibly enough to allow for easy modification.

Problem Description

The previous assignment had a simplifying assumption that the amount of money would be limited, such that the builder could not afford more than four houses on any property.   This assignment will lift that restriction.

There is nothing really special about building hotels in Monopoly.  That purchase is simply equal to the price of five houses, and is built ONLY in the same circumstances that would permit five houses (no other property may have fewer than four).

The inputs to the program will be essentially the same -- the color of a property group and the amount of money to be spent.   But the following cases should be addressed:

if no building is affordable, display "You cannot afford even one house." instead of building 0 houses everywhere.
If any property could have 5 houses, announce that such properties would have a hotel instead.
if any property could have more than 5 houses, still only build one hotel there, and nothing more
omit the word 'none' in the output (i..e don't say 'one property has none' or 'none have two')
Comparing Homework 2 to Homework 3

The difference in these programs primarily appears in the final output statement:

Hypothetical Homework 2 Output	Corresponding Homework 3 Output
 	
three will have none and none will have one	You cannot afford even one house.
one will have one and two will have two	one will have one and two will have two
one will have none and two will have one	two will have one
three will have one and none will have two	three will have one
three will have three and none will have four	three will have three
two will have four and one will have five	two will have four and one will have a hotel
two will have five and none will have six	two will have a hotel
one will have seven and two will have eight	three will have a hotel
Hint:  The simplest and clearest solutions will use 'else' and 'elif' and will not need 'and' or 'or'.
A portion of your grade is based on how clear your code is, and how well it avoids producing contradictory output.

Note:  All of these decisions in this chart are entirely based on the results of the previous program, so your code should do the same -- wait until the calculations are complete before deciding how to display the results.   Do not make your program unnecessarily complicated by trying to identify the different cases before doing any math.

Also Note:  three hotels have the cost of 15 houses, which may require a slight modification to how you displayed numbers in the previous assignment.   You may have your program state that they can only afford 15 houses, even if they could afford many more than that.   Allowing for all the numbers from 16 to 100 (or 1000) is more cumbersome than interesting at this time.

Extra Credit Option

It is quite possible that the user chooses a color that is not accepted. Write code that would allow the user to try again, until a suitable input is found.

It might be good to treat "blue" as a special case, since it is not so much wrong as it is simply ambiguous.

For best results, write a solution that does not involve exception handling (no ValueError or KeyError)

Note: This option would require a lateranguage element from Cengage Unit 3.
