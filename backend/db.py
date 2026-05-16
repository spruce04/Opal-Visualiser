#Connect to the "opal" postgresql database
from dotenv import load_dotenv
from os import getenv
import psycopg2

load_dotenv()
conn = psycopg2.connect(getenv("DATABASE_URL"))

if __name__ == "__main__":
    print("db.py ran directly")
    print(conn)