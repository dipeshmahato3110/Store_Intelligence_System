import sqlite3

DB_NAME = "store_intelligence.db"


def get_connection():

    return sqlite3.connect(DB_NAME)