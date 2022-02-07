-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema hotel_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotel_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotel_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `hotel_db` ;

-- -----------------------------------------------------
-- Table `hotel_db`.`booked`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`booked` (
  `booking_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `contact_no` VARCHAR(255) NOT NULL,
  `address` TEXT NOT NULL,
  `email` VARCHAR(60) NOT NULL,
  `id_proof_type` CHAR(1) NOT NULL,
  `id_proof_no` VARCHAR(20) NOT NULL,
  `date_in` DATETIME NOT NULL,
  `date_out` DATETIME NOT NULL,
  `no_children` INT NOT NULL,
  `no_adults` INT NOT NULL,
  `room_preference` VARCHAR(1) NULL DEFAULT NULL,
  `comments` VARCHAR(255) NULL DEFAULT NULL,
  `time_booked` DATETIME NULL DEFAULT NULL,
  `status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '0: Not Confirmed 1: Checked In',
  PRIMARY KEY (`booking_id`),
  UNIQUE INDEX `id_proof_no_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB
  AUTO_INCREMENT = 9;


-- -----------------------------------------------------
-- Table `hotel_db`.`checked_in`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`checked_in` (
  `checkin_id` INT NOT NULL AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `room_id` INT NOT NULL,
  `name` TEXT NOT NULL,
  `contact_no` VARCHAR(255) NOT NULL,
  `address` TEXT NOT NULL,
  `email` VARCHAR(60) NOT NULL,
  `id_proof_type` CHAR(1) NOT NULL,
  `id_proof_no` VARCHAR(20) NOT NULL,
  `date_in` DATETIME NOT NULL,
  `date_out` DATETIME NOT NULL,
  `no_children` INT NOT NULL,
  `no_adults` INT NOT NULL,
  `booking_cid` INT NULL DEFAULT NULL,
  `status` TINYINT(1) NOT NULL DEFAULT '1' COMMENT '1: CheckedIN; 2: CheckedOUT',
  PRIMARY KEY (`checkin_id`),
  UNIQUE INDEX `customer_id_UNIQUE` (`customer_id` ASC) VISIBLE,
  UNIQUE INDEX `booking_cid_UNIQUE` (`booking_cid` ASC) VISIBLE)
ENGINE = InnoDB
  AUTO_INCREMENT = 990;


-- -----------------------------------------------------
-- Table `hotel_db`.`checkout`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`checkout` (
  `customer_id` INT NOT NULL,
  `checkout_time` DATETIME NOT NULL,
  PRIMARY KEY (`customer_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel_db`.`room_categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`room_categories` (
  `id` INT NOT NULL,
  `name` TEXT NOT NULL,
  `price` FLOAT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel_db`.`rooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`rooms` (
  `room_no` INT NOT NULL,
  `rooms` VARCHAR(45) NOT NULL,
  `category_id` INT NOT NULL,
  `status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '\'0 = Available/Unoccupied , 1= Unvailable/Occupied\'',
  PRIMARY KEY (`room_no`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel_db`.`services`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`services` (
  `index` INT NOT NULL AUTO_INCREMENT,
  `service_id` INT NULL DEFAULT NULL,
  `customer_id` INT NULL DEFAULT NULL,
  `service_date` DATETIME NOT NULL,
  `comments` TEXT NULL DEFAULT NULL,
  `bill` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`index`))
ENGINE = InnoDB
  AUTO_INCREMENT = 7;


-- -----------------------------------------------------
-- Table `hotel_db`.`services_categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`services_categories` (
  `id` VARCHAR(1) NOT NULL,
  `name` TEXT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_db`.`users` (
  `id` INT NOT NULL,
  `name` VARCHAR(200) NOT NULL,
  `username` VARCHAR(200) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `type` TINYINT(1) NOT NULL DEFAULT '2' COMMENT '\'1=admin , 2 = staff\'',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `password_UNIQUE` (`password` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
