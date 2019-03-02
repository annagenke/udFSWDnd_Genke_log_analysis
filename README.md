# Project 3 Log Analysis
This is the repository for the Log Analysis Project.

##Before Running
In order to run this project you must have the news postgreSQL database set up on the Vagrant VM.
Instructions for setting up the VM and PostgreSQL DB can be found in lessons for this unit.
You must save the log_analysis.py file in the shared folder for Vagrant

###Running
In order to  run the log analysis program, save the python file log_analysis.py 
in the directory shared with the Vagrant VM. 
From this directory run the command
`/path/to/python log_analysis.py`

##Output
Following the above directions will result in output that looks like the following
 (actual results will depend on data):
```commandline
What are the most popular three articles of all time?
        Candidate is jerk, alleges rival - 338647
        Bears love berries, alleges bear - 253801
        Bad things gone, say good people - 170098


Who are the most popular article authors of all time?
        Ursula La Multa - 507594
        Rudolf von Treppenwitz - 423457
        Anonymous Contributor - 170098
        Markoff Chaney - 84557


On which days did more than 1% of requests lead to errors? (%)
        July 17th, 2016 - 2.26
```