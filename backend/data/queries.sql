-- --5. Specific queries

--5.a. View only data from within the selected date range
SELECT * FROM station_frequency
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01' --Dates can be changed as neccessary
ORDER BY e_count DESC;


--5.a. "total_taps" - the total number of taps for each station
SELECT station_name, SUM(e_count) AS total_taps, month
FROM station_frequency 
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01'
GROUP BY station_name, month
ORDER BY total_taps DESC; 

--To sum the count of all months instead of listing them differently
SELECT station_name, SUM(e_count) AS total_taps
FROM station_frequency 
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01'
GROUP BY station_name
ORDER BY total_taps DESC; 

--5.b. "net_taps" - contains the net taps for each station (tap ons - tap offs)
SELECT station_name, SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END) AS net_taps, month
FROM station_frequency
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01'
GROUP BY station_name, month
ORDER BY ABS(SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END)) DESC;

--To sum the count of all months instead of listing them differently
SELECT station_name, SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END) AS net_taps
FROM station_frequency
WHERE station_name != 'UNKNOWN' AND month BETWEEN '2026-01-01' AND '2026-04-01'
GROUP BY station_name
ORDER BY ABS(SUM(CASE WHEN entry_exit = 'Entry' THEN e_count WHEN entry_exit = 'Exit' THEN -e_count END)) DESC;