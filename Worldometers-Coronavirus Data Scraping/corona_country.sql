CREATE TABLE `corona_country` (
  `data_time` datetime NOT NULL,
  `country_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `total_case` int DEFAULT NULL,
  `new_case` int DEFAULT NULL,
  `total_deaths` int DEFAULT NULL,
  `new_deaths` int DEFAULT NULL,
  `total_recovered` int DEFAULT NULL,
  `active_cases` int DEFAULT NULL,
  `serious` int DEFAULT NULL,
  `total_cases_1M_pop` decimal(8,2) DEFAULT NULL,
  `deaths_1M_pop` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`data_time`,`country_name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;
