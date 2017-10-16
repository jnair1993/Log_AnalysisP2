# Log Analysis Project

> Jayesh nair

## About

A large database is explored through complex queries to find answers to the questions listed below:

1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors?

### Software Required

- Python3
- Vagrant
- VirtualBox

### Installing

1. Install Vagrant And VirtualBox
2. Clone this repository

## Running the tests

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database.

Using `psql -d news`, create the views listed below. Simply copy and paste each view.

Once done with creating views, exit psql with `CTRL -D`.

Then run command `python newsdata.py` to run the queries.

## Views Used

"""sql
CREATE VIEW total AS
SELECT date(time), COUNT(*) AS views
FROM log
GROUP BY date(time)
ORDER BY date(time);
"""

"""sql
CREATE VIEW errors AS
SELECT date(time), COUNT(*) AS error_count
FROM log WHERE status like '%404%'
GROUP BY date(time)
ORDER BY date(time);
"""

"""sql
CREATE VIEW Error_Rate AS
SELECT total.date, round((100.0*errors.error_count/total.views),1) AS percent
FROM total, errors
WHERE total.date = errors.date
ORDER BY total.date;
"""
