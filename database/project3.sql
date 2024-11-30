CREATE DATABASE  IF NOT EXISTS `project3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project3`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project3
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `country_id` int NOT NULL AUTO_INCREMENT,
  `country_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (33,'United States'),(34,'United Kingdom'),(35,'France'),(36,'Germany'),(37,'Italy'),(38,'Spain'),(39,'Japan'),(40,'China'),(41,'Australia'),(42,'Canada'),(43,'Brazil'),(44,'India'),(45,'Russia'),(46,'South Korea'),(47,'Mexico'),(48,'Netherlands'),(49,'Switzerland'),(50,'Sweden'),(51,'Israel'),(52,'Singapore');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `user_id` int NOT NULL,
  `vacation_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (95,134),(95,126);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin'),(2,'User');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(512) DEFAULT NULL,
  `role_id` int NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `fk_users_roles_idx` (`role_id`),
  CONSTRAINT `fk_users_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (84,'John','Smith','john.smith@email.com','123456',2),(85,'Emma','Johnson','emma.j@email.com','123456',2),(86,'Michael','Davis','michael.d@email.com','123456',2),(87,'Sarah','Wilson','sarah.w@email.com','123456',2),(88,'David','Brown','david.b@email.com','123456',2),(89,'Lisa','Anderson','lisa.a@email.com','123456',2),(90,'James','Taylor','james.t@email.com','123456',2),(91,'Rachel','Martinez','rachel.m@email.com','123456',2),(92,'Daniel','Garcia','daniel.g@email.com','123456',2),(93,'Emily','Miller','emily.m@email.com','123456',2),(94,'Uri ','shamir','urisham@gmail.com','f0d7f417ab3f56c628a589269b7ac295c5e518f88aeb2dc9547c587f4bb9aba14f3fc182074f16ca30b2994f881214a3a92a83aee41dea152225d676b6582b17',1),(95,'אורי','שמיר','shan@gmail.com','f0d7f417ab3f56c628a589269b7ac295c5e518f88aeb2dc9547c587f4bb9aba14f3fc182074f16ca30b2994f881214a3a92a83aee41dea152225d676b6582b17',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacations`
--

DROP TABLE IF EXISTS `vacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacations` (
  `vacation_id` int NOT NULL AUTO_INCREMENT,
  `vacation_name` varchar(100) DEFAULT NULL,
  `vacation_description` varchar(2000) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `vacation_img` varchar(255) DEFAULT NULL,
  `country_id` int NOT NULL,
  `likes` int DEFAULT NULL,
  `vacation_days` int DEFAULT NULL,
  PRIMARY KEY (`vacation_id`),
  KEY `fk_Vacations_Countries1_idx` (`country_id`),
  CONSTRAINT `fk_Vacations_Countries1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacations`
--

LOCK TABLES `vacations` WRITE;
/*!40000 ALTER TABLE `vacations` DISABLE KEYS */;
INSERT INTO `vacations` VALUES (125,'Paris Romance','Experience the magic of Paris with this romantic getaway including Eiffel Tower dinner and Seine River cruise','2024-12-10','2024-12-17',2499.99,'aa9279d9-3f3f-47fb-a4fb-84a6fd548d59.jpg',35,124,8),(126,'Tokyo Adventure','Explore the vibrant streets of Tokyo, visit temples, and experience modern Japanese culture','2024-12-15','2024-12-23',3299.99,'3cc45840-d23c-458f-90b4-281b201e9eb0.jpg',39,90,9),(127,'Swiss Alps Ski Resort','Premium ski vacation in the heart of the Swiss Alps with luxury accommodation and ski passes included','2025-01-05','2025-01-12',4199.99,'2d48a343-0006-4ff9-baab-b290da91ff7b.jpg',49,167,8),(128,'Australian Outback Safari','Discover the Australian wilderness, meet native wildlife, and camp under the stars','2025-02-10','2025-02-18',3799.99,'e161c7a2-8584-4aa8-a908-6c8946795d85.jpg',41,145,9),(129,'Italian Culinary Journey','Tour through Italy\'s finest culinary regions, including cooking classes and wine tasting','2025-03-15','2025-03-22',2899.99,'f1b0bf5e-850a-4fcf-b8a6-7f809a578826.jpg',37,198,8),(130,'Spanish Costa del Sol','Relax on Spain\'s sunny beaches with luxury resort stay and Mediterranean cuisine','2025-04-01','2025-04-08',1999.99,'d0fc27ae-71fc-4dfb-acee-3a9fadab1da4.jpg',38,156,8),(131,'Brazilian Carnival Experience','Join the world\'s biggest party in Rio de Janeiro with VIP carnival access','2025-02-15','2025-02-22',3499.99,'d97938cb-a2ce-4693-9f5d-eb7911b5c4ce.jpg',43,234,8),(132,'Korean Cultural Discovery','Immerse yourself in Korean culture, from traditional temples to K-pop','2025-05-01','2025-05-10',2799.99,'5aa5fcaf-9f10-47b4-9ef3-bf3fe3045947.jpg',46,167,10),(133,'Mexico Beach Resort','All-inclusive luxury resort stay in Cancun with water activities and spa treatments','2025-06-10','2025-06-17',2299.99,'265aeef6-14ab-4161-8c67-d58b8746f659.jpg',47,178,8),(134,'German Christmas Markets','Experience the magic of traditional German Christmas markets and winter festivities','2024-12-20','2024-12-27',1899.99,'11f1f5c3-8116-4a55-9390-785390f04b96.jpg',36,145,8),(135,'Israel Heritage Tour','Explore historical sites and experience the rich cultural heritage of Israel','2025-03-20','2025-03-28',2699.99,'acbf5a55-45a0-4d11-a506-4de0abb0a4b7.jpg',51,132,9),(136,'English Countryside','Tour through picturesque villages, historic castles, and traditional tea rooms','2025-05-15','2025-05-22',2399.99,'94553459-47bd-44fc-a871-849e86cc07a8.jpg',34,112,8);
/*!40000 ALTER TABLE `vacations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-26 23:01:09
