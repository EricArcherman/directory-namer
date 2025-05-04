# name-fetcher

gets Roxbury Latin student directory and prints out in .csv format for donation tracking.

----
details:

The script "reshape.py" gets necessary student data for tracking service drive donations.

Future service drives:

1. copy paste exported RL directory into directory.txt
2. run reshape.py
   parses the txt with a regex for student and grad year
   puts it into "students.csv"
3. put students.csv into this year's google sheet
