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
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `room_no` int NOT NULL,
  `rooms` varchar(45) NOT NULL,
  `category_id` int NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '''0 = Available/Unoccupied , 1= Unvailable/Occupied',
  PRIMARY KEY (`room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (101,'Twin Bed Room',4,0),(102,'Deluxe Room',1,0),(103,'Single Room',2,0),(104,'Twin Bed Room',4,0),(105,'Family Room',3,0),(106,'Twin Bed Room',4,0),(107,'Deluxe Room',1,0),(108,'Twin Bed Room',4,0),(109,'Twin Bed Room',4,0),(110,'Deluxe Room',1,0),(201,'Twin Bed Room',4,0),(202,'Deluxe Room',1,0),(203,'Deluxe Room',1,0),(204,'Deluxe Room',1,0),(205,'Deluxe Room',1,0),(206,'Family Room',3,0),(207,'Deluxe Room',1,0),(208,'Family Room',3,0),(209,'Twin Bed Room',4,0),(210,'Deluxe Room',1,0),(301,'Deluxe Room',1,0),(302,'Family Room',3,0),(303,'Twin Bed Room',4,0),(304,'Single Room',2,0),(305,'Twin Bed Room',4,0),(306,'Family Room',3,0),(307,'Twin Bed Room',4,0),(308,'Family Room',3,0),(309,'Twin Bed Room',4,0),(310,'Family Room',3,0),(401,'Family Room',3,0),(402,'Twin Bed Room',4,0),(403,'Twin Bed Room',4,0),(404,'Twin Bed Room',4,0),(405,'Deluxe Room',1,0),(406,'Twin Bed Room',4,0),(407,'Family Room',3,0),(408,'Single Room',2,0),(409,'Twin Bed Room',4,0),(410,'Deluxe Room',1,0),(501,'Deluxe Room',1,0),(502,'Deluxe Room',1,0),(503,'Family Room',3,0),(504,'Twin Bed Room',4,0),(505,'Deluxe Room',1,0),(506,'Single Room',2,0),(507,'Twin Bed Room',4,0),(508,'Twin Bed Room',4,0),(509,'Family Room',3,0),(510,'Twin Bed Room',4,0),(601,'Family Room',3,0),(602,'Twin Bed Room',4,0),(603,'Twin Bed Room',4,0),(604,'Twin Bed Room',4,0),(605,'Deluxe Room',1,0),(606,'Family Room',3,0),(607,'Deluxe Room',1,0),(608,'Single Room',2,0),(609,'Single Room',2,0),(610,'Single Room',2,0),(701,'Deluxe Room',1,0),(702,'Twin Bed Room',4,0),(703,'Family Room',3,0),(704,'Family Room',3,0),(705,'Deluxe Room',1,0),(706,'Single Room',2,0),(707,'Family Room',3,0),(708,'Deluxe Room',1,0),(709,'Twin Bed Room',4,0),(710,'Twin Bed Room',4,0),(801,'Twin Bed Room',4,0),(802,'Single Room',2,0),(803,'Deluxe Room',1,0),(804,'Single Room',2,0),(805,'Deluxe Room',1,0),(806,'Twin Bed Room',4,0),(807,'Family Room',3,0),(808,'Deluxe Room',1,0),(809,'Single Room',2,0),(810,'Single Room',2,0),(901,'Single Room',2,0),(902,'Single Room',2,0),(903,'Single Room',2,0),(904,'Single Room',2,0),(905,'Twin Bed Room',4,0),(906,'Family Room',3,0),(907,'Single Room',2,0),(908,'Twin Bed Room',4,0),(909,'Deluxe Room',1,0),(910,'Twin Bed Room',4,0);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
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
