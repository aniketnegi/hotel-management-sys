DROP DATABASE IF EXISTS hotel_mgmt;
CREATE DATABASE hotel_mgmt;
USE hotel_mgmt;

CREATE TABLE hotel_mgmt.guest_details (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone_number VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE hotel_mgmt.employee_login (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE hotel_mgmt.room_details (
  id INT NOT NULL AUTO_INCREMENT,
  room_number INT NOT NULL,
  room_type VARCHAR(255) NOT NULL,
  room_price INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE hotel_mgmt.booking_details (
  id INT NOT NULL AUTO_INCREMENT,
  guest_id INT NOT NULL,
  room_id INT NOT NULL,
  check_in_date DATE NOT NULL,
  check_out_date DATE NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE hotel_mgmt.payment_details (
  id INT NOT NULL AUTO_INCREMENT,
  booking_id INT NOT NULL,
  payment_date DATE NOT NULL,
  amount INT NOT NULL,
  PRIMARY KEY (id)
);