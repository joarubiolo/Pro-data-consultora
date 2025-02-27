-- Habilitar la carga de archivos locales (solo si es necesario)
SET GLOBAL local_infile = 1;

-- Cargar categories_normalized.csv
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/categories_normalized.csv'
INTO TABLE categoria
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar ciudades_normal.csv
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ciudades_normal.csv'
INTO TABLE ciudades
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar business_normal.csv
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/business_normal.csv'
INTO TABLE business
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar metadata_normal.csv
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/metadata_normal.csv'
INTO TABLE metadata
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SET FOREIGN_KEY_CHECKS = 0;

-- Cargar reviews_gm_normal.csv
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/reviews_gm_normal.csv'
INTO TABLE reviews_gm
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r'
IGNORE 1 ROWS;

-- Cargar reviews_normal.csv
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/reviews_normal.csv'
INTO TABLE reviews_y
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r'
IGNORE 1 ROWS;

SET FOREIGN_KEY_CHECKS = 1;

-- Cargar business_categories_normal.csv (tabla intermedia)
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/business_categories.csv'
INTO TABLE business_categories
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar metadata_categories_normal.csv (tabla intermedia)
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/metadata_categories.csv'
INTO TABLE metadata_categories
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

ALTER TABLE metadata DROP COLUMN category_id;
ALTER TABLE business DROP COLUMN category_id;