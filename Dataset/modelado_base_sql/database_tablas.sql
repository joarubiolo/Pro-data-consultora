-- Eliminar la base de datos si ya existe y crearla de nuevo
DROP DATABASE IF EXISTS pro_data;
CREATE DATABASE pro_data;
USE pro_data;

-- Eliminar las tablas si existen antes de crearlas
DROP TABLE IF EXISTS reviews_y;
DROP TABLE IF EXISTS reviews_gm;
DROP TABLE IF EXISTS metadata_categories;
DROP TABLE IF EXISTS business_categories;
DROP TABLE IF EXISTS metadata;
DROP TABLE IF EXISTS business;
DROP TABLE IF EXISTS categoria;
DROP TABLE IF EXISTS ciudades;

-- Tabla de Ciudades
CREATE TABLE ciudades (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city VARCHAR(255) NOT NULL,
    population INT NOT NULL,
    city_normalized VARCHAR(255) NOT NULL
);

-- Tabla de Categorías
CREATE TABLE categoria (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category VARCHAR(255) NOT NULL
);

-- Tabla de Negocios (Business)
CREATE TABLE business (
    id VARCHAR(50) PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    postal_code INT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    city_id INT NOT NULL,
    stars FLOAT NOT NULL CHECK (stars BETWEEN 1 AND 5),
    review_count INT NOT NULL DEFAULT 0,
    address VARCHAR(255),
    is_open BOOLEAN NOT NULL,
    delivery BOOLEAN NOT NULL,
    takeout BOOLEAN NOT NULL,
    outdoor_seating BOOLEAN NOT NULL,
    drivethrough BOOLEAN NOT NULL,
    wheelchair_friendly BOOLEAN NOT NULL,
    alcohol_beverage BOOLEAN NOT NULL,
    dancing BOOLEAN NOT NULL,
    catering BOOLEAN NOT NULL,
    counter_service BOOLEAN NOT NULL,
    seating BOOLEAN NOT NULL,
    dogs_allowed BOOLEAN NOT NULL,
    bike_parking BOOLEAN NOT NULL,
    parking BOOLEAN NOT NULL,
    breakfast BOOLEAN NOT NULL,
    lunch BOOLEAN NOT NULL,
    dinner BOOLEAN NOT NULL,
    dessert BOOLEAN NOT NULL,
    casual BOOLEAN NOT NULL,
    romantic BOOLEAN NOT NULL,
    formal BOOLEAN NOT NULL,
    trendy BOOLEAN NOT NULL,
    with_reservation BOOLEAN NOT NULL,
    live_entertainment BOOLEAN NOT NULL,
    groups_friendly BOOLEAN NOT NULL,
    kids_friendly BOOLEAN NOT NULL,
    wifi BOOLEAN NOT NULL,
    bar_onsite BOOLEAN NOT NULL,
    credit_cards BOOLEAN NOT NULL,
    FOREIGN KEY (city_id) REFERENCES ciudades(city_id)
);

-- Tabla de Metadata (Información de Restaurantes)
CREATE TABLE metadata (
    id VARCHAR(50) PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    street_address VARCHAR(255),
    postal_code INT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    city_id INT NOT NULL,
    stars FLOAT NOT NULL CHECK (stars BETWEEN 1 AND 5),
    review_count INT NOT NULL DEFAULT 0,
    is_open BOOLEAN NOT NULL,
    delivery BOOLEAN NOT NULL,
    takeout BOOLEAN NOT NULL,
    dinein BOOLEAN NOT NULL,
    outdoor_seating BOOLEAN NOT NULL,
    drivethrough BOOLEAN NOT NULL,
    good_for_working_on_laptop BOOLEAN NOT NULL,
    solo_dining BOOLEAN NOT NULL,
    wheelchair_friendly BOOLEAN NOT NULL,
    alcohol_beverage BOOLEAN NOT NULL,
    healthy_food BOOLEAN NOT NULL,
    fast_comfort_food BOOLEAN NOT NULL,
    braille_menu BOOLEAN NOT NULL,
    all_you_can_eat BOOLEAN NOT NULL,
    coffee BOOLEAN NOT NULL,
    dancing BOOLEAN NOT NULL,
    catering BOOLEAN NOT NULL,
    counter_service BOOLEAN NOT NULL,
    pay_ahead BOOLEAN NOT NULL,
    seating BOOLEAN NOT NULL,
    breakfast BOOLEAN NOT NULL,
    lunch BOOLEAN NOT NULL,
    dinner BOOLEAN NOT NULL,
    dessert BOOLEAN NOT NULL,
    casual BOOLEAN NOT NULL,
    romantic BOOLEAN NOT NULL,
    formal BOOLEAN NOT NULL,
    trendy BOOLEAN NOT NULL,
    with_reservation BOOLEAN NOT NULL,
    usually_a_wait BOOLEAN NOT NULL,
    quick_visit BOOLEAN NOT NULL,
    black_owned BOOLEAN NOT NULL,
    women_led BOOLEAN NOT NULL,
    veteran_led BOOLEAN NOT NULL,
    entertainment BOOLEAN NOT NULL,
    live_entertainment BOOLEAN NOT NULL,
    lgbtq_friendly BOOLEAN NOT NULL,
    fast_service BOOLEAN NOT NULL,
    fireplace BOOLEAN NOT NULL,
    rooftop_seating BOOLEAN NOT NULL,
    sports BOOLEAN NOT NULL,
    college_students BOOLEAN NOT NULL,
    family_friendly BOOLEAN NOT NULL,
    groups_friendly BOOLEAN NOT NULL,
    locals BOOLEAN NOT NULL,
    tourists BOOLEAN NOT NULL,
    kids_friendly BOOLEAN NOT NULL,
    wi_fi BOOLEAN NOT NULL,
    bar_onsite BOOLEAN NOT NULL,
    cash_only BOOLEAN NOT NULL,
    checks BOOLEAN NOT NULL,
    credit_cards BOOLEAN NOT NULL,
    debit_cards BOOLEAN NOT NULL,
    nfc_mobile_payments BOOLEAN NOT NULL,
    recycling BOOLEAN NOT NULL,
    FOREIGN KEY (city_id) REFERENCES ciudades(city_id)
);

-- Tabla intermedia para la relación muchos a muchos entre business y categorías
CREATE TABLE business_categories (
    id VARCHAR(50) NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (id, category_id),
    FOREIGN KEY (id) REFERENCES business(id),
    FOREIGN KEY (category_id) REFERENCES categoria(category_id)
);

-- Tabla intermedia para la relación muchos a muchos entre metadata y categorías
CREATE TABLE metadata_categories (
    id VARCHAR(50) NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (id, category_id),
    FOREIGN KEY (id) REFERENCES metadata(id),
    FOREIGN KEY (category_id) REFERENCES categoria(category_id)
);

-- Tabla de Reseñas de Google Maps
CREATE TABLE reviews_gm (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(50) NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    has_text BOOLEAN NOT NULL,
    vader_score FLOAT NOT NULL,
    textblob_score FLOAT NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (id) REFERENCES metadata(id)
);

-- Tabla de Reseñas de Yelp
CREATE TABLE reviews_y (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(50) NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    has_text BOOLEAN NOT NULL,
    vader_score FLOAT NOT NULL,
    textblob_score FLOAT NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (id) REFERENCES business(id)
);
