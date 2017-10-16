#!/usr/bin/env python3

import psycopg2
DB_NAME = "news"


def connect():
    try:
        db = psycopg2.connect(database=DB_NAME)
        c = db.cursor()
        return db, c
    except:
        print("Error connecting to Database")

# Queries

q_1 = "What are the most popular three articles of all time?"
query_1 = """
    SELECT title, count(*) as views
    FROM articles, log
    WHERE log.path like concat('%', articles.slug)
    GROUP by  title ORDER by views desc
    LIMIT 3;
"""

q_2 = "Who are the most popular article authors of all time?"
query_2 = """
    SELECT authors.name, count(articles.author) as views
    FROM authors, log, articles
    WHERE log.path like concat('%', articles.slug)
    AND articles.author = authors.id
    GROUP by authors.name
    ORDER by views desc;
"""

q_3 = "On which days did more than 1% of requests lead to errors?"
query_3 = """
    SELECT *
    FROM Error_Rate
    WHERE Error_Rate.percent > 1
    ORDER BY Error_Rate.percent DESC;
"""


# Gets and Prints the query
def print_query(q, query):
    print "\n" + q + "\n"
    db, c = connect()
    c.execute(query)
    new_print = c.fetchall()
    db.close()
    if q == q_1:
        for result in new_print:
            print('\t' + '"' + str(result[0]) + '"' + ' --- ' +
                  str(result[1]) + " views")

    elif q == q_2:
        for result in new_print:
            print('\t' + str(result[0]) + ' --- ' +
                  str(result[1]) + " views")

    elif q == q_3:
        for result in new_print:
            print('\t' + str(result[0]) + ' ---> ' +
                  str(result[1]) + "% errors")

print_query(q_1, query_1)
print_query(q_2, query_2)
print_query(q_3, query_3)
