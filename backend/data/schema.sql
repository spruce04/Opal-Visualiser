-- Instructions to set up the database:
-- Please note that you will need the following files from Transport NSW's open data set
-- Train, metro, and light rail monthly usage: https://opendata.transport.nsw.gov.au/data/dataset/train-station-entries-and-exits-data/resource/f8bb2918-0540-4bb3-9ccf-f7aef04d4249
-- I have renamed this file to station_frequency.csv
-- stops.txt, which you can get from the zip at https://opendata.transport.nsw.gov.au/dataset/timetables-complete-gtfs

-- 1. Create a table to store the station_frequency data with the following structure
CREATE TABLE IF NOT EXISTS station_frequency(month DATE, station_name TEXT, station_type TEXT, entry_exit TEXT, e_count TEXT);

--2. Load in the data from the station_frequency.csv file
\copy station_frequency FROM '{path+to_file}/station_frequency.csv' DELIMITER ',' CSV HEADER;

--3. Change all "Less than 50" values to be -1
UPDATE station_frequency
SET e_count = '-1' WHERE e_count = 'Less than 50';

--4. Change all values in e_count to be INTEGERs
ALTER TABLE station_frequency
ALTER COLUMN e_count TYPE INTEGER
USING e_count::INTEGER;

--5. Create a table for the locations of stops, that will read from the .txt file
CREATE TABLE locations(station_name TEXT, lat DOUBLE PRECISION, lon DOUBLE PRECISION);

--6. Load in the data from the locations.csv file
\copy locations FROM './backend/data/locations.csv' DELIMITER ',' CSV HEADER;