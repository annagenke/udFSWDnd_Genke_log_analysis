import psycopg2

queries = [
    {"title": "What are the most popular three articles of all time?",
     "query":
         """
        SELECT title, count(*)
        FROM articles
            LEFT JOIN log ON '/article/' || articles.slug = log.path
                GROUP BY title
                ORDER BY count DESC
                LIMIT 3;
        """
     },
    {"title": "Who are the most popular article authors of all time?",
     "query":
         """
        SELECT name AS author, count(*) AS views
        FROM authors
            LEFT JOIN articles ON authors.id=articles.author
            LEFT JOIN log ON '/article/' || articles.slug = log.path
                GROUP BY authors.name
                ORDER BY count DESC;
        """,
     },
    {"title": "On which days did more than 1% of requests lead to errors?",
     "query":
         """
        SELECT *
        FROM  (SELECT T1.date,
                      Round
                      (Cast(Cast(error AS FLOAT) / Cast(total AS FLOAT) * 100
                      AS
                                 NUMERIC)
                      , 2) AS
                      perc
               FROM   (SELECT Cast(time AS DATE) AS date,
                              Count(*)           AS error
                       FROM   log
                       WHERE '200 OK' != status
                        GROUP  BY date) AS T1
                      JOIN (SELECT Cast(time AS DATE) AS date,
                                   Count(*)           AS total
                            FROM   log
                            GROUP  BY date) AS T2
                        ON T1.date = T2.date) AS perc_table
        WHERE  perc >= 1;
      """
     }
]
def main():
    db_conn_str = "dbname = \"news\""

    conn = psycopg2.connect("dbname=news")



if __name__ == "__main__":
    main()
