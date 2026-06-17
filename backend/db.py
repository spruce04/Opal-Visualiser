#Connect to the "opal" postgresql database
from dotenv import load_dotenv
from os import getenv
from psycopg2 import pool

load_dotenv()

# Create a pool of 1 to 10 connections
connection_pool = pool.SimpleConnectionPool(1, 10, getenv("DATABASE_URL"))

if __name__ == "__main__":
    print("db.py ran directly")