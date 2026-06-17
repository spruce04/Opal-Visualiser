from fastapi import FastAPI
from db import connection_pool
from data import queries
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import date

app = FastAPI()

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Helper function - easily requests and returns the results of an SQL query
#Param query_data - the SQL command that we want to execute as a string, start and end dates, col_name - the name of the column that holds numberic data
def querier(query_data, col_name):
    #Unpack the SQL statement and dates
    sql, dates = query_data
    
    #Grab a connection from the pool for this specific request
    conn = connection_pool.getconn()
    cursor = None
    try:
        #As conn exists, we know related functions will work
        cursor = conn.cursor()
        cursor.execute(sql, dates)
        results = cursor.fetchall()
        
        ret = []
        for i in results:
            temp = {} 
            temp["station_name"] = i[0]
            temp["station_type"] = i[1]
            temp[col_name] = i[2]
            temp["lat"] = i[3]
            temp["lon"] = i[4]
            ret.append(temp)
        conn.commit() #Close on success
        return ret
    
    #Reset the connection if an error occurs
    except Exception as e:
        if conn:
            conn.rollback() 
        raise e    

    finally:
        #Always close if a cursor was opened
        if cursor:
            cursor.close()
        connection_pool.putconn(conn) #Return a now unused connection to the pool

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
