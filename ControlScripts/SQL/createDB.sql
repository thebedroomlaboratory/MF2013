-- Create script for The Bedroom Laboratory Maker Faire 2013 projects
-- mysql -u root --password -f  < "Script path"

DROP TABLE `tbl_mf2013`.`oven`;
DROP TABLE `tbl_mf2013`.`temp`;
DROP TABLE `tbl_mf2013`.`people`;
DROP DATABASE `tbl_mf2013`;

-- Database used for The Bedroom Laboratory maker faire 2013 projects
CREATE DATABASE `tbl_mf2013`;

-- Table used to store data retrieved from the oven project
CREATE TABLE `tbl_mf2013`.`oven` (
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
	`temp` INT NOT NULL,
	`status` BOOL NOT NULL
) ENGINE=InnoDB;

-- Table used to store data retrieved from the people counter project
CREATE TABLE `tbl_mf2013`.`people` (
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
	`counter` INT NOT NULL,
	`switch` BOOL NOT NULL
) ENGINE=InnoDB;

-- Table used to store data retrieved from the temp/light sensor project
CREATE TABLE `tbl_mf2013`.`temp` (
	`time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
	`override` BOOL NOT NULL,
	`lux` INT NOT NULL,
	`temp` INT NOT NULL,
	`status` BOOL NOT NULL
) ENGINE=InnoDB;

-- Pre-populate tables with some test data
INSERT INTO `tbl_mf2013`.`oven`(`temp`, `status`) VALUES (1, 0), (2, 1), (3, 0), (4, 1);
INSERT INTO `tbl_mf2013`.`people`(`counter`, `switch`) VALUES (1, 0), (2, 1), (3, 0), (4, 1);
INSERT INTO `tbl_mf2013`.`temp`(`override`, `lux`, `temp`, `status`) VALUES (0, 1, 2, 1), (1, 3, 4, 0), (0, 5, 6, 0), (1, 7, 8, 1);

-- View sample data in tables
SELECT * FROM `tbl_mf2013`.`oven`;
SELECT * FROM `tbl_mf2013`.`people`;
SELECT * FROM `tbl_mf2013`.`temp`;
