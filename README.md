# Project 3 Log Analysis
This is the repository for the Log Analysis Project. It consists of a single python script and uses
the psycopq2 library to connect and query a database with 3 tables that hold information about online articles. 
The program will answer 3 hard-coded questions about the data.

## Before Running
In order to run this project you must have a news postgreSQL database set up and populated.

sample data can be found at:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 


In order to create and populate the PostgreSQL DB you will have to run the following command

`psql -d news -f newsdata.sql`



### Running 
In order to run the program, from the directory where you saved the log_analysis.py file, use the command
`/path/to/python log_analysis.py`

## Output
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