-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: blog
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('8ae3c7df6af6');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `content` varchar(10000) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `hits` int(11) DEFAULT NULL,
  `comments` int(11) DEFAULT NULL,
  `picture` varchar(300) DEFAULT NULL,
  `full_content` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`aid`),
  KEY `cid` (`cid`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `category` (`cid`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'政府出实招 企业谋创新 各地有序复工复产劲头足','关系到实现全年经济社会发展目标任务，关系到全面建成小康社会和完成‘十三五’规划，关系到我国对外开放和世界经济稳定','2020-02-29 22:00:00',1,600,10,'image/feature-pic-1.jpeg',NULL),(2,'国务院联防联控机制介绍新冠肺炎防控和治疗有关情况','关系到实现全年经济社会发展目标任务，关系到全面建成小康社会和完成‘十三五’规划，关系到我国对外开放和世界经济稳定','2020-02-29 22:00:00',3,600,15,'image/feature-pic-2.jpeg',NULL),(3,'脱贫攻坚加把劲，不破楼兰终不还','关系到实现全年经济社会发展目标任务，关系到全面建成小康社会和完成‘十三五’规划，关系到我国对外开放和世界经济稳定','2020-02-29 22:00:00',3,600,12,'image/feature-pic-3.jpeg',NULL),(4,'微盟“删库”144小时，痛的不是股价，是信任','很多人认为SaaS市场会因为疫情而火爆的时候，微盟删库事件也让大家更加认识到云上数据安全的问题更需要引起足够的重视','2020-02-29 22:00:00',3,600,7,'image/blog-post-1.jpeg',NULL),(5,'关键时刻，苹果再失血？','据知情人士透露，制造设计副总裁尼克·弗伦扎（Nick Forlenza）已从退休，离开了原岗位，而另一位运营副总裁杜科·帕斯穆瓦（Duco Pasmooij）也在考虑未来离开苹果。','2020-02-29 22:00:00',1,600,12,'image/blog-post-3.jpeg',NULL),(6,'飞书遭微信全面封禁 申诉后三小时微信单方面修改封禁提示','2月29日，字节跳动旗下办公套件飞书发布官方公告称，飞书相关域名无故被微信全面封禁，并且被单方面关闭微信分享API接口','2020-02-29 22:00:00',2,600,13,'image/blog-post-4.jpeg',NULL),(7,'进一步指导各地落实分区分级差异化防控策略','就进一步指导各地准确分析把握疫情和经济社会发展形势，落实分区分级差异化防控策略，统筹推进疫情防控和经济社会发展工作，作出部署安排。','2020-02-29 22:00:00',1,600,1,'image/blog-2.jpg',NULL),(8,'《马哈迪时代的终结》','政治分分钟在变，在国阵、伊斯兰党及希盟拒绝支持马哈迪后，他终于在自己的布局下，终结了任相之路。','2020-02-29 22:00:00',4,600,NULL,'image/gallery-2.jpg',NULL),(9,'一个字节都得省的年代，人们是如何创造游戏人声的？','这台机器具备分析语音音调和共振的能力，原理是将声音编码后再进行传输。因为从本质来看，人声大体上可以解构成周期性的波形和谐波，声带、鼻子和喉咙则是改变声音振幅、频率的系统','2020-02-29 22:00:00',2,600,NULL,'image/feature-pic-2.jpeg',NULL);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'世界',5),(2,'科技',2),(3,'财经',6),(4,'军事',7);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mark`
--

DROP TABLE IF EXISTS `mark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mark` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(1000) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `marker_name` varchar(20) DEFAULT NULL,
  `marker_portrait` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`mid`),
  KEY `uid` (`uid`),
  CONSTRAINT `mark_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mark`
--

LOCK TABLES `mark` WRITE;
/*!40000 ALTER TABLE `mark` DISABLE KEYS */;
INSERT INTO `mark` VALUES (1,'对待“新冠病毒”，我们应高度警惕、严阵以待；对待“新冠”字眼，则需保持平和理性心态，不宜望“字”生义，乱了分寸。\n实际上，这种平和理性恰恰能展现我们心理上的强大自信，而这也是我们最终战胜病毒的力量来源之一。','2020-02-29 22:30:00',1,'ross','image/avatar-1.jpg'),(2,'法治是疫情防控的最强大基石。防控疫情蔓延，依法是“从严”的前提，也是“从严”的保障。\n不久前召开的中央全面依法治国委员会第三次会议强调，“坚持依法防控，在法治轨道上统筹推进各项防控工作”','2020-02-29 22:30:00',1,'joey','image/avatar-2.jpg'),(3,'疫情防控正处于关键时期，越是到最吃劲的时候，越考验公职人员，尤其是基层干部的责任心。只有对怠政惰政干部及时、\n有效、严厉问责，才能让慵懒无处遁形，抓实抓细防控工作，最终打赢疫情防控阻击战','2020-03-01 09:00:00',1,'rachel','image/avatar-3.jpg');
/*!40000 ALTER TABLE `mark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `aid` int(11) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `aid` (`aid`),
  CONSTRAINT `tag_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `article` (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1,'financial',2),(2,'financial',2),(3,'technology',6),(4,'military',8),(5,'world',5),(6,'world',7),(7,'financial',3),(8,'financial',4),(9,'technology',9);
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `portrait` varchar(300) DEFAULT NULL,
  `regtime` datetime DEFAULT NULL,
  `isforbid` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'monica','123456','12345678901','123@qq.com','image/avatar-3.jpg','2020-02-29 08:00:00',0),(2,'max','a63d2f9ac1d341ae389920e6fe5712ca27768a72',NULL,NULL,NULL,NULL,0),(3,'sam','44dafff0a9d4aa238f9982e18dce7f3b95d0307e','17865922952',NULL,NULL,NULL,0),(4,'rache','12345678abc',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-06 20:24:18
