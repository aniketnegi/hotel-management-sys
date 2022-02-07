USE hotel_db;

-- DELETE DATA IF EXISTS

TRUNCATE TABLE `hotel_db`.`users`;
TRUNCATE TABLE `hotel_db`.`services_categories`;


-- INSERT DATA INTO TABLE users

INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('1', 'Aniket Negi', 'sudoer0', 'root0', '1');
INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('2', 'Arjun Khanna', 'sudoer1', 'root1', '1');
INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('3', 'Linus', 'sudoer2', 'root2', '2');
INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('4', 'Anthony', 'sudoer3', 'root3', '2');

-- INSERT DATA INTO TABLE services_categories

INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('1', 'Room Service');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('2', 'Laundry');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('3', 'Restaurant');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('4', 'Minibar');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('5', 'Chauffeur');



