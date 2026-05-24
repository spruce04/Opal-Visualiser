from fastapi import FastAPI
from db import conn
from data import queries
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#Helper function - easily requests and returns the results of an SQL query
#Param sql - the SQL command that we want to execute as a string, col_name - the name of the column that holds numberic data
def querier(sql, col_name):
    #Create a cursor to be able to use the connection to the database
    cursor = conn.cursor()
    #Execute an SQL command
    cursor.execute(sql)
    #Gather and return the results of the command
    results = cursor.fetchall()
    #Properly format the results - add all results to a list of dictionaries
    ret = []
    for i in results:
        temp = {} 
        temp["station_name"] = i[0]
        temp["station_type"] = i[1]
        temp[col_name] = i[2]
        temp["lat"] = i[3]
        temp["lon"] = i[4]
        ret.append(temp)
    return ret

#Function to run on the root
@app.get("/")
def func():
    return {"message": "hello"}

#Function to run on /totaltaps
@app.get("/total_taps")
def get_total_taps(start: str='2026-04-01', end: str='2026-04-01'):
    return querier(queries.total_taps(start,end), "total_taps")

#Function to run on /nettaps
@app.get("/net_taps")
def get_net_taps(start: str='2026-04-01', end: str='2026-04-01'):
    return querier(queries.net_taps(start, end), "net_taps")
