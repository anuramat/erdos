import csv
import psycopg2
from app.logic.clusters import get_cluster, get_tag
from psycopg2 import errors


def intx(s: str, default) -> int:
    try:
        return int(float(s))
    except ValueError:
        return default


def start():
    con = psycopg2.connect(
        "dbname=erdosdb user=erdos host=db password=w84kgj3vptg4m239"
    )
    with open("data.csv") as csvfile:
        datareader = csv.reader(csvfile, delimiter=",", quotechar='"')
        next(datareader)
        for row in datareader:

            cur = con.cursor()
            try:
                # not always there
                abs = row[19]
                doi = row[16][:49]

                try:
                    authors = eval(row[8])
                except:
                    raise errors.UniqueViolation
                lang = row[7]
                n_cit = intx(row[6], 0)
                year = intx(row[4], None)
                title = row[2]
                pid = row[1]

                cluster = get_cluster(abs)
                tag = get_tag(cluster)

                cur.execute(
                    "INSERT INTO papers (id, year, citation_number, language, doi, tag, cluster) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (pid, year, n_cit, lang, doi, tag, cluster),
                )

                cur.execute(
                    "INSERT INTO abstracts (paper_id, text, title) VALUES (%s, %s, %s)",
                    (pid, abs, title),
                )

                for author in authors:
                    # check if author exists
                    try:
                        aid = author["_id"]
                        name = author["name"]
                    except KeyError:
                        continue
                    cur.execute("SELECT id FROM authors WHERE id = %s", (aid,))
                    author_exists = bool(cur.fetchone())
                    if not author_exists:
                        # create author if it doesn't exist
                        cur.execute(
                            "INSERT INTO authors (id, name, rating) VALUES (%s, %s, %s)",
                            (aid, name, 0),
                        )
                    # update ratings
                    cur.execute("UPDATE authors SET rating = rating + %s", (n_cit,))

                    # add papers_authors entry
                    cur.execute(
                        "INSERT INTO paper_authors (paper_id, author_id) VALUES (%s, %s)",
                        (pid, aid),
                    )
            except errors.UniqueViolation:
                con.rollback()
                cur.close()
                continue

            con.commit()
            cur.close()

    con.close()
