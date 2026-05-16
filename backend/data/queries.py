#SQL Queries for the data

'''
View only data from within the selected date range
SELECT * FROM station_frequency
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01' --Dates can be changed as neccessary
ORDER BY e_count DESC;
'''

'''
"total_taps" - the total number of taps for each station
SELECT station_name, SUM(e_count) AS total_taps, month
FROM station_frequency 
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01'
GROUP BY station_name, month
ORDER BY total_taps DESC; 
'''
## The total number of taps for each station in the given time period
total_taps = """
SELECT station_name, station_type, SUM(e_count) AS total_taps
FROM station_frequency 
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-04-01' AND '2026-04-01'
GROUP BY station_name, station_type
ORDER BY total_taps DESC; 
"""

'''
"net_taps" - contai taps for each station (tap ons - tap offs)
SELECT station_name, S WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END) AS net_taps, month
FROM station_frequency
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01'
GROUP BY station_name, month
ORDER BY ABS(SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END)) DESC;
'''

#The total net taps for  station in the given time period. net taps = (tap on - tap off)
net_taps = """
SELECT station_name, station_type, SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END) AS net_taps
FROM station_frequency
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-04-01' AND '2026-04-01'
GROUP BY station_name, station_type
ORDER BY ABS(SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END)) DESC;
"""

#Combine net_taps with the existing coordinates for each station
new_net_taps = """
SELECT station_frequency.station_name, station_type, SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END) AS net_taps, MAX(stop_lat) AS lat, MAX(stop_lon) AS lon
FROM station_frequency
LEFT JOIN locations
    ON locations.stop_name = TRIM(REGEXP_REPLACE(station_frequency.station_name, '\s+', ' ', 'g')) AND location_type = '1'
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-04-01' AND '2026-04-01'
GROUP BY station_name, station_type, locations.stop_lat, locations.stop_lon
ORDER BY station_name DESC;
"""

#Combine total_taps with the coordinates
new_total_taps = """
SELECT station_name, station_type, SUM(e_count) AS total_taps, MAX(stop_lat) AS lat, MAX(stop_lon) AS lon
FROM station_frequency 
LEFT JOIN locations
    ON locations.stop_name = TRIM(REGEXP_REPLACE(station_frequency.station_name, '\s+', ' ', 'g')) AND location_type = '1'
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-04-01' AND '2026-04-01'
GROUP BY station_name, station_type, locations.stop_lat, locations.stop_lon
ORDER BY total_taps DESC; 
"""