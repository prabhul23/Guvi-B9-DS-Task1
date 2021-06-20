-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2021 at 04:47 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `learning`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_ID` int(11) NOT NULL,
  `Name` varchar(10) NOT NULL,
  `School` varchar(15) NOT NULL,
  `Eng` int(11) DEFAULT NULL,
  `Maths` int(11) DEFAULT NULL,
  `Malay` int(11) DEFAULT NULL,
  `Science` int(11) DEFAULT NULL,
  `Soc_Sci` int(11) DEFAULT NULL,
  `Grade` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_ID`, `Name`, `School`, `Eng`, `Maths`, `Malay`, `Science`, `Soc_Sci`, `Grade`) VALUES
(1, 'Raju', 'BVB', 79, 85, 88, 84, 75, 'A'),
(2, 'Ramu', 'BVB', 80, 75, 70, 72, 69, 'B'),
(3, 'Aswin', 'K V', 84, 80, 78, 79, 82, 'A'),
(4, 'Anjali', 'K V', 94, 88, 98, 99, 87, 'A'),
(5, 'Tony', 'St.Thomas', 64, 96, 58, 69, 52, 'B'),
(6, 'Tina', 'St.Thomas', 94, 80, 78, 89, 82, 'A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `Student_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
