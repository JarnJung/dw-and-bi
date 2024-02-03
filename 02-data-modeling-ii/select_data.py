import glob
import json
import os
from typing import List

from cassandra.cluster import Cluster

def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Create keyspace
    try:
        session.execute(
            """
            CREATE KEYSPACE IF NOT EXISTS github_events
            WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
            """
        )
    except Exception as e:
        print(e)

    # Set keyspace
    try:
        session.set_keyspace("github_events")
    except Exception as e:
        print(e)

    # Select data in Cassandra and print them to stdout
    query = """
    SELECT * from events
    """
    rows = session.execute(query)

    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()