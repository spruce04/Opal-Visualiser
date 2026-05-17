#SQL Queries for the data

## The total number of taps for each station in the given time period
def total_taps(start: str, end: str):
    return  f"""
            SELECT station_frequency.station_name, station_type, SUM(e_count) AS total_taps, lat, lon
            FROM station_frequency
            LEFT JOIN locations
                ON locations.station_name = station_frequency.station_name
            WHERE station_frequency.station_name != 'UNKNOWN' AND month BETWEEN '{start}' AND '{end}'
            GROUP BY station_frequency.station_name, station_type, lon, lat
            ORDER BY total_taps DESC; 
            """

#The total net taps for  station in the given time period. net taps = (tap on - tap off)
def net_taps(start: str, end: str):
    return  f"""
            SELECT station_frequency.station_name, station_type, SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END) AS net_taps, lat, lon
            FROM station_frequency
            LEFT JOIN locations
                ON locations.station_name = station_frequency.station_name
            WHERE station_frequency.station_name != 'UNKNOWN' AND month BETWEEN '{start}' AND '{end}'
            GROUP BY station_frequency.station_name, station_type, lon, lat
            ORDER BY ABS(SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END)) DESC;
            """