/*
Navicat MySQL Data Transfer

Source Server         : bjtu_cms
Source Server Version : 50559
Source Host           : localhost:3306
Source Database       : cms

Target Server Type    : MYSQL
Target Server Version : 50559
File Encoding         : 65001

Date: 2019-08-22 08:34:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cms_category
-- ----------------------------
DROP TABLE IF EXISTS `cms_category`;
CREATE TABLE `cms_category` (
  `id` varchar(32) NOT NULL,
  `type` varchar(32) DEFAULT NULL,
  `type_name` varchar(100) NOT NULL,
  `c_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of cms_category
-- ----------------------------
INSERT INTO `cms_category` VALUES ('1', '1', '招生信息', '2019-07-10 10:48:35');
INSERT INTO `cms_category` VALUES ('2', '2', '导师简介', '2019-07-11 15:44:04');
INSERT INTO `cms_category` VALUES ('3', '3', '学科简介', '2019-08-21 14:33:39');
INSERT INTO `cms_category` VALUES ('4', '4', '文件下载', '2019-08-21 14:33:42');
INSERT INTO `cms_category` VALUES ('5', '5', '学生论坛', '2019-08-21 14:33:44');

-- ----------------------------
-- Table structure for cms_item
-- ----------------------------
DROP TABLE IF EXISTS `cms_item`;
CREATE TABLE `cms_item` (
  `id` varchar(32) NOT NULL,
  `title` varchar(100) NOT NULL,
  `content` varchar(2000) DEFAULT NULL,
  `category_id` varchar(32) DEFAULT NULL,
  `c_time` datetime DEFAULT NULL,
  `u_time` datetime DEFAULT NULL,
  `status` char(1) DEFAULT NULL,
  `creator_id` varchar(32) DEFAULT NULL,
  `creator_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of cms_item
-- ----------------------------
INSERT INTO `cms_item` VALUES ('03bd8278ae0711e9a548005056c00008', '2019学生选课通知', '许多个人分部共同凤凰台', '2', '2019-07-24 17:57:31', '2019-07-25 09:04:45', '1', null, null);
INSERT INTO `cms_item` VALUES ('0a507750ab6c11e993e8d12735c73e86', '2020教职工评审通知', '    mmcbfv    ', '3', '2019-08-21 10:01:56', '2019-07-23 19:39:18', '1', '1', null);
INSERT INTO `cms_item` VALUES ('1', '2019招生简章', '点击回复过不少南方聚不耐烦ghytthjyr6yhy一盒一盒一盒能源一塌糊涂还要很讨厌同行业还要好凧u简答题好也还要胡就u就有很多通过谈话一年后也你一年一天天集合也好一会也好u金鱼你也哪一年也润滑油就途径士的 图二谈话已经换一台就也好有机会也 同行业好一天静候佳音就也金鱼就一天就已经人已经也即将于回家也加好友集合一会金鱼就也集合同一家u已解决也', '1', '2019-07-16 08:32:15', '2019-07-16 08:32:08', '1', '1', '张三');
INSERT INTO `cms_item` VALUES ('12348', '交大诺贝尔奖征集启动通知', 'v b', '2', '2019-08-21 10:01:52', '2019-07-22 10:35:51', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('1d9d78e4ab7511e98f77d12735c73e86', '计算机学院成立人工智能研究室', 'hgjyhj', '2', '2019-07-21 13:04:19', null, '1', '1', '1');
INSERT INTO `cms_item` VALUES ('2', '2019招生专业', '二夫人个体户共同话题你还木易', '1', '2019-07-15 15:22:20', '2019-07-24 15:22:27', '1', '2', 'lisi');
INSERT INTO `cms_item` VALUES ('268ddc74ab7311e990a2d12735c73e86', '2020考研一志愿上线名单', 'jhvb ljbiobpoi', '2', '2019-07-21 12:50:29', null, '1', '1', '1');
INSERT INTO `cms_item` VALUES ('3', '2020考研考研调剂第一批', 'rgfrgfgfgtggtgetg', '1', '2019-07-18 10:20:45', '2019-07-18 10:20:50', '1', '1', 'rd');
INSERT INTO `cms_item` VALUES ('4', '2020招生简章', 'ggthbtg', '1', '2019-07-18 10:21:13', '2019-07-18 10:21:17', '1', '2', 'ef');
INSERT INTO `cms_item` VALUES ('52667442adef11e9bc9c005056c00008', '2020招生专业简介', 'bb', '', '2019-07-24 15:49:34', '2019-07-24 19:18:51', '0', '1', '1');
INSERT INTO `cms_item` VALUES ('8be285f6ab7311e9ab03d12735c73e86', '2020专业参考书', 'dbvfbf', '2', '2019-07-21 12:52:53', '2019-07-24 19:18:54', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('a56078c2ae0311e99843005056c00008', '测试数据', 'bb', '', '2019-07-24 17:57:31', '2019-07-24 19:18:57', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('a617d468ade711e9a35f005056c00008', '测试数据', 'bb', '', '2019-07-24 15:49:34', '2019-07-24 19:19:00', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('b539f94aae7811e98e7c005056c00008', '测试数据', '奇偶奇偶就没了狂怒', '5', '2019-07-25 09:04:45', null, '1', null, null);
INSERT INTO `cms_item` VALUES ('bfdbfgb', '测试数据', 'fbfb', '1', '2019-07-24 19:19:44', '2019-07-24 19:19:03', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('cbf5caa6ab6b11e99941d12735c73e86', '测试数据', '非官方个回复后果', '1', '2019-07-24 19:19:46', '2019-07-24 19:19:06', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('d2fea0b8ade711e981d4005056c00008', '测试数据', 'nnnn', '', '2019-07-24 15:49:34', '2019-07-24 19:19:16', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('dg5tuuolil', '测试数据', 'regr', '1', '2019-07-24 19:19:49', '2019-07-24 19:19:14', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('et5y6i7i8yg', '测试数据', 'jyj', '1', '2019-08-01 19:19:37', '2019-07-24 19:19:19', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('f000a6c0ab7311e9ae5cd12735c73e86', '测试数据', 'fvbfgbn', '2', '2019-07-21 12:56:20', '2019-07-24 19:19:22', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('qwr325t5', '测试数据', '', '1', '2019-07-24 19:19:40', '2019-07-24 19:19:25', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('rtg', '测试数据', 'yjytr', '1', '2019-07-18 15:43:41', '2019-07-18 15:43:43', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('vb vb vgvd', '测试数据', 'fbgdb', '1', '2019-08-01 19:19:33', '2019-08-06 19:19:28', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('vngng', '测试数据', 'gbsfbsf', '1', '2019-07-23 15:28:40', '2019-07-24 15:28:44', '1', '1', '1');
INSERT INTO `cms_item` VALUES ('发给', '测试数据', null, '4', '2019-08-21 10:08:49', null, null, null, null);

-- ----------------------------
-- Table structure for cms_user
-- ----------------------------
DROP TABLE IF EXISTS `cms_user`;
CREATE TABLE `cms_user` (
  `id` varchar(32) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 NOT NULL,
  `role` varchar(20) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  `pwd` varchar(32) NOT NULL,
  PRIMARY KEY (`id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of cms_user
-- ----------------------------
INSERT INTO `cms_user` VALUES ('1', '张三', '管理员', '2019-07-22 13:27:03', '123456');
INSERT INTO `cms_user` VALUES ('2', '王鹏程', '管理员', '2019-07-15 14:21:19', '123456');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'zhangsan', '123456');
INSERT INTO `user` VALUES ('2', 'lisi', '123456');
INSERT INTO `user` VALUES ('3', 'zhangsan22', '123456');
INSERT INTO `user` VALUES ('4', 'zhangsan22', '123456');
INSERT INTO `user` VALUES ('5', 'zhangsan22', '123456');
INSERT INTO `user` VALUES ('6', 'zhangsan66', '123456');
INSERT INTO `user` VALUES ('7', 'zhangsan77', '123456');
