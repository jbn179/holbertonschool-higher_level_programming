-- This script creates the table 'force_name' with columns 'id' and 'name' (name cannot be null).
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
