-- This script creates the table 'unique_id' with columns 'id' (unique, default value 1) and 'name'.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
