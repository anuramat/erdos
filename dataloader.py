import csv
import psycopg2

con = psycopg2.connect("dbname=erdosdb user=erdos host= password=w84kgj3vptg4m239")
with open("data.csv") as csvfile:
    datareader = csv.reader(csvfile, delimiter=",", quotechar='"')
    next(datareader)
    for row in datareader:

        cur = con.cursor()

        # not always there
        abs = row[19]
        doi = row[16]

        authors = eval(row[8])
        lang = row[7]
        n_cit = int(float(row[6]))
        year = int(float(row[4]))
        title = row[2]
        pid = row[1]

        cur.execute(
            "INSERT INTO papers (id, title, year, citation_number, language, doi VALUES (%s, %s, %s, %s, %s, %s)",
            (pid, title, year, n_cit, lang, doi),
        )

        cur.execute(
            "INSERT INTO abstracts (paper_id, text) VALUES (%s, %s)", (pid, abs)
        )


        for author in authors:
            # check if author exists
            aid = author["id"]
            name = author["name"]
            cur.execute("SELECT id FROM authors WHERE id = %s", (aid))
            author_exists = bool(cur.fetchone())
            if not author_exists:
                # create author if it doesn't exist
                cur.execute(
                    "INSERT INTO authors (id, name) VALUES (%s, %s)", (aid, name)
                )
            # update ratings
            cur.execute("UPDATE authors SET rating = rating + %s", (n_cit,))

            # add papers_authors entry
            cur.execute(
                "INSERT INTO paper_authors (paper_id, author_id) VALUES (%s, %s)",
                (pid, aid),
            )

        con.commit()
        cur.close()

con.close()
