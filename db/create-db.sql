SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
--
-- Database: `hotel_db`
--
CREATE DATABASE IF NOT EXISTS hotel_db;

USE hotel_db;

-- --------------------------------------------------------
--
-- Table structure for table `checked_in`
--

CREATE TABLE `checked_in` (
  `id` int(30)  NOT NULL,
  `room_id` int(30) NOT NULL,
  `name` text NOT NULL,
  `contact_no` varchar(20) NOT NULL,
  `address` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `id_proof_type` varchar(1) NOT NULL,
  `id_proof_no` varchar(20) NOT NULL,
  `date_in` datetime NOT NULL,
  `date_out` datetime NOT NULL,
  `no_adults` int(2) NOT NULL,
  `no_children` int(2) NOT NULL,
  `booked_cid` int(30) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
--
-- Table structure for table `booked
--

CREATE TABLE `booked` (
  `id` int(30) NOT NULL,
  `name` text NOT NULL,
  `contact_no` varchar(20) NOT NULL,
  `address` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `id_proof_type` varchar(1) NOT NULL,
  `id_proof_no` varchar(20) NOT NULL,
  `date_in` datetime NOT NULL,
  `date_out` datetime NOT NULL,
  `no_adults` int(2) NOT NULL,
  `no_children` int(2) NOT NULL,
  `room_preference` varchar(1) NOT NULL,
  `booked_cid` int(30) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` int(30) NOT NULL,
  `room` varchar(30) NOT NULL,
  `category_id` int(30) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 0 COMMENT '0 = Available , 1= Unvailable'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
--
-- Table structure for table `room_categories`
--

CREATE TABLE `room_categories` (
  `id` int(30) NOT NULL,
  `name` text NOT NULL,
  `price` float NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(30) NOT NULL,
  `name` varchar(200) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `type` tinyint(1) NOT NULL DEFAULT 2 COMMENT '1=admin , 2 = staff'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
--
-- Indexes for dumped tables
--

--
-- table `checked_in`
--
ALTER TABLE `checked`
  ADD PRIMARY KEY (`id`);

--
--  table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`);

--
--  table `room_categories`
--
ALTER TABLE `room_categories`
  ADD PRIMARY KEY (`id`);

--
--  table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

-- --------------------------------------------------------

--
-- AUTO_INCREMENT for dumped tables
--

--
-- table `checked`
--
ALTER TABLE `checked`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- table `room_categories`
--
ALTER TABLE `room_categories`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;


-- ---------------------------------------------------------

-- Commmit the changes
COMMIT;
