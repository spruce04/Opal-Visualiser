--Instructions to set up the database:
-- 1. Create TABLE with the following structure
CREATE TABLE IF NOT EXISTS station_frequency(month DATE, station_name TEXT, station_type TEXT, entry_exit TEXT, e_count TEXT);

--2. Load in the data from the .csv file
\copy station_frequency FROM '{path+to_file}/station_frequency.csv' DELIMITER ',' CSV HEADER;

--3. Change all "Less than 50" values to be -1
UPDATE station_frequency
SET e_count = '-1' WHERE e_count = 'Less than 50';

--4. Change all values in e_count to be INTEGERs
ALTER TABLE station_frequency
ALTER COLUMN e_count TYPE INTEGER
USING e_count::INTEGER;