-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel_db
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `booked`
--

DROP TABLE IF EXISTS `booked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booked` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL,
  `address` text NOT NULL,
  `email` varchar(60) NOT NULL,
  `id_proof_type` char(1) NOT NULL,
  `id_proof_no` varchar(20) NOT NULL,
  `date_in` datetime NOT NULL,
  `date_out` datetime NOT NULL,
  `no_children` int NOT NULL,
  `no_adults` int NOT NULL,
  `room_preference` varchar(1) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `time_booked` datetime DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0: Not Confirmed 1: Checked In',
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booked`
--

LOCK TABLES `booked` WRITE;
/*!40000 ALTER TABLE `booked` DISABLE KEYS */;
INSERT INTO `booked` VALUES (21,'Aniket Negi','9876543210','d-2, VK','aniketnegi@duck.com','A','112','2022-02-10 00:00:00','2022-02-12 00:00:00',1,1,'2','NULL','2022-02-05 09:00:31',1),(22,'Rajeev Negi','9999037395','55-J, CBI Complex, Vasant Vihar','aniketnegi@duck.com','A','12354','2022-02-12 00:00:00','2022-02-14 00:00:00',1,2,'1','NULL','2022-02-05 09:17:56',1),(23,'Ananya Negi','0291801293','23847923875klsjfkdsuhksj','sjfhjksdhf@gmail.com','A','1248723897598','2022-02-06 00:00:00','2022-02-08 00:00:00',328947928,23875893,'1','NULL','2022-02-05 09:29:41',1),(24,'Neetu Negi','9999037395','dsf','neetu@gmail.com','A','1248723897598','2022-02-05 00:00:00','2022-02-06 00:00:00',2,2,'1','NULL','2022-02-05 09:44:58',1),(25,'Arjun','2947823479','2479','3874@gmail.com','A','238947','2022-02-05 00:00:00','2022-02-08 00:00:00',241,3,'1','NULL','2022-02-05 09:49:39',1),(26,'John Doe','0192849754','21','john@gmail.com','A','12123','2022-02-08 00:00:00','2022-02-10 00:00:00',2,3,'2','NULL','2022-02-05 14:33:16',1),(28,'Aniket Negi','9999999999','238238957298','aniketnegi@duck.com','A','382759287','2022-02-10 00:00:00','2022-02-15 00:00:00',12321,213,'1','NULL','2022-02-05 14:49:38',0);
/*!40000 ALTER TABLE `booked` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-06  1:53:00
