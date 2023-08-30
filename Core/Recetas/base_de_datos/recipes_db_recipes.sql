CREATE DATABASE  IF NOT EXISTS `recipes_db` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `recipes_db`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: recipes_db
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `instructions` longtext,
  `under_30` tinyint DEFAULT NULL,
  `date_coocked` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_recipes_users_idx` (`user_id`),
  CONSTRAINT `fk_recipes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,' Creamy Garlic Parmesan Chicken','Tender chicken breasts cooked in a creamy garlic Parmesan sauce.','Season the chicken breasts with salt and pepper.\r\nIn a large skillet, heat olive oil over medium-high heat.\r\nAdd the chicken breasts to the skillet and cook for 6-7 minutes on each side, or until golden brown and cooked through.\r\nRemove the chicken from the skillet and set aside.\r\nIn the same skillet, melt butter over medium heat.\r\nAdd minced garlic and cook for 1-2 minutes, until fragrant.\r\nStir in flour and cook for an additional minute.\r\nGradually whisk in chicken broth, followed by heavy cream.\r\nBring the sauce to a simmer and cook for 3-4 minutes, until thickened.\r\nStir in grated Parmesan cheese until melted and smooth.\r\nReturn the chicken breasts to the skillet and spoon the sauce over them.\r\nSimmer for 2-3 minutes, allowing the chicken to absorb the flavors of the sauce.\r\nServe the creamy garlic Parmesan chicken hot, garnished with fresh parsley if desired.',1,'2023-08-26 00:00:00','2023-08-30 16:26:35',NULL,1),(2,'Chocolate Chip Cookies','Delicious homemade chocolate chip cookies that are perfect for any occasion.','Preheat the oven to 350°F (175°C).\r\nIn a large mixing bowl, cream together 1 cup of softened butter, 1 cup of granulated sugar, and 1 cup of packed brown sugar until light and fluffy.\r\nBeat in 2 eggs and 1 teaspoon of vanilla extract until well combined.\r\nIn a separate bowl, whisk together 3 cups of all-purpose flour, 1 teaspoon of baking soda, and 1/2 teaspoon of salt.\r\nGradually add the dry ingredients to the butter mixture, mixing well after each addition.\r\nStir in 2 cups of chocolate chips.\r\nDrop rounded tablespoonfuls of dough onto ungreased baking sheets.\r\nBake for 10-12 minutes or until golden brown.\r\nAllow the cookies to cool on the baking sheets for a few minutes, then transfer them to wire racks to cool completely.\r\nEnjoy these delicious homemade chocolate chip cookies with a glass of milk!',1,'2023-08-26 00:00:00','2023-08-30 16:27:34',NULL,2);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-30 16:33:56
