from fastapi import FastAPI
from db import conn
from data import queries

app = FastAPI()

#Helper function - easily requests and returns the results of an SQL query
#Param s - the SQL command that we want to execute as a string, col_name - the name of the column that holds numberic data
def querier(s: str, col_name):
    #Create a cursor to be able to use the connection to the database
    cursor = conn.cursor()
    #Execute an SQL command
    cursor.execute(s)
    #Gather and return the results of the command
    results = cursor.fetchall()
    #Properly format the results - add all results to a list of dictionaries
    ret = []
    for i in results:
        temp = {} 
        temp["station_name"] = i[0]
        temp["station_type"] = i[1]
        temp[col_name] = i[2]
        ret.append(temp)
    return ret

#Function to run on the root
@app.get("/")
def func():
    return {"message": "hello"}

#Function to run on /totaltaps
@app.get("/totaltaps")
def get_total_taps():
    return querier(queries.total_taps, "total_taps")

#Function to run on /nettaps
@app.get("/nettaps")
def get_net_taps():
    return querier(queries.net_taps, "net_taps")
