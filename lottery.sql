/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-12-15 22:54:44
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lottery_dyj
-- ----------------------------
DROP TABLE IF EXISTS `lottery_dyj`;
CREATE TABLE `lottery_dyj` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lottery_time` varchar(11) NOT NULL,
  `lottery_no` int(11) NOT NULL,
  `first_no` varchar(4) DEFAULT NULL,
  `second_no` varchar(4) DEFAULT NULL,
  `three_no` varchar(4) DEFAULT NULL,
  `four_no` varchar(4) DEFAULT NULL,
  `five_no` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=274 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for lottery_phoenix_tree
-- ----------------------------
DROP TABLE IF EXISTS `lottery_phoenix_tree`;
CREATE TABLE `lottery_phoenix_tree` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for lottery_phoenix_tree_ssq
-- ----------------------------
DROP TABLE IF EXISTS `lottery_phoenix_tree_ssq`;
CREATE TABLE `lottery_phoenix_tree_ssq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `open_time` text,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
