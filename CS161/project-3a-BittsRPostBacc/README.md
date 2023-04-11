# project-3a

Write a program that asks the user how many integers they would like to enter.  You can assume that this initial input will be an integer >= 1.  The program will then prompt the user to enter that many integers.  After all the numbers have been entered, the program should display the largest and smallest of those numbers (no, you cannot use lists, or any other material we haven't covered). Your code should work correctly no matter what integers the user enters. When you run your program it should match the following format:
```
How many integers would you like to enter?
4
Please enter 4 integers.
-4
105
2
-7
min: -7
max: 105
```
Hints: How many numbers do you actually need to remember at a time?  If someone were reciting a long list of numbers to you, and you had to tell them the max and min at the end, how would you do it?  How should you initialize your variables?  What happens if the user only enters one integer?

More hints: Don't use arbitrary small/large values in your code for this assignment - remember that a user could always enter a smaller/larger value than what you picked. Also remember that we haven't covered infinity, so you're not allowed to use that. You don't need initial values that are smaller/larger than all values that **could** be entered - you're only concerned with the values that actually **are** entered.

The file must be named: min_max.py
