USE hotel_db;

-- INSERT DATA INTO TABLE users

INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('1', 'Aniket Negi', 'sudoer0', 'root0', '1');
INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('2', 'Arjun Khanna', 'sudoer1', 'root1', '1');
INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('3', 'Linus', 'sudoer1', 'root2', '2');
INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('4', 'Anthony', 'sudoer2', 'root3', '2');
INSERT INTO `hotel_db`.`users` (`id`, `name`, `username`, `password`, `type`) VALUES ('5', 'SuperUser', 'sudo', 'root', '1');

-- INSERT DATA INTO TABLE services_categories

INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('1', 'Room Service');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('2', 'Laundry');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('3', 'Restaurant');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('4', 'Minibar');
INSERT INTO `hotel_db`.`services_categories` (`id`, `name`) VALUES ('5', 'Chauffeur');



