-- MySQL dump 10.13  Distrib 5.7.17, for osx10.11 (x86_64)
--
-- Host: localhost    Database: proteomics
-- ------------------------------------------------------
-- Server version	5.7.17

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
-- Table structure for table `cancer`
--

DROP TABLE IF EXISTS `cancer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cancer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entryname` char(200) DEFAULT NULL,
  `length` int(30) DEFAULT NULL,
  `description` text,
  `GO` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancer`
--

LOCK TABLES `cancer` WRITE;
/*!40000 ALTER TABLE `cancer` DISABLE KEYS */;
INSERT INTO `cancer` VALUES (1,'P53',393,'RecName: Full=Cellular tumor antigen p53; AltName: Full=Antigen NY-CO-13; AltName: Full=Phosphoprotein p53; AltName: Full=Tumor suppressor p53;','GO:0000785, C:chromatin, IBA:GO_Central GO:0005524, F:ATP binding,                                             IDA:UniProtKB GO:0006915,                                             P:apoptotic process, TAS:Reactome'),(2,'MYC',439,'RecName: Full=Receptor tyrosine-protein kinase erbB-2; EC=2.7.10.1; AltName: Full=Metastatic lymph node gene 19 protein; Short=MLN 19; AltName: Full=Proto-oncogene Neu; AltName: Full=Proto-oncogene c-ErbB-2; AltName: Full=Tyrosine kinase-type cell surface receptor HER2; AltName: Full=p185erbB2; AltName: CD_antigen=CD340; Flags: Precursor;','GO:0005829, C:cytosol, TAS:Reactome                                              GO:0003677, F:DNA binding, ISS:UniProtKB)                                              GO:1904837, P:beta-catenin-TCF complex assembly, TAS:Reactome'),(3,'ERRB2',1255,'RecName: Full=Receptor tyrosine-protein kinase erbB-2; EC=2.7.10.1; AltName: Full=Metastatic lymph node gene 19 protein; Short=MLN 19; AltName: Full=Proto-oncogene Neu; AltName: Full=Proto-oncogene c-ErbB-2; AltName: Full=Tyrosine kinase-type cell surface receptor HER2; AltName: Full=p185erbB2; AltName: CD_antigen=CD340; Flags: Precursor;','GO:0016324, C:apical plasma membrane, IEA:Ensembl                                                GO:0005524, F:ATP binding\', IEA:UniProtKB-KW                                                GO:0008283, P:cell proliferation, TAS:ProtInc'),(4,'EGFR',1210,'RecName: Full=C-type lectin domain family 14 member A; AltName: Full=Epidermal growth factor receptor 5; Short=EGFR-5; Flags: Precursor;','GO:0009897, C:external side of plasma membrane, IDA:MGI                                                 GO:0030246, F:carbohydrate binding\', \'IEA:UniProtKB-KW'),(5,'PTEN',403,'RecName: Full=Phosphatidylinositol 3,4,5-trisphosphate 3-phosphatase and dual-specificity protein phosphatase PTEN; EC=3.1.3.16; EC=3.1.3.48; EC=3.1.3.67; AltName: Full=Mutated in multiple advanced cancers 1; AltName: Full=Phosphatase and tensin homolog;','GO:0016324, C:apical plasma membrane, IMP:UniProtKB                                               GO:0010997\', F:anaphase-promoting complex binding, IPI:BHF-UCL                                               GO:0030534, P:adult behavior, IEA:Ensembl');
/*!40000 ALTER TABLE `cancer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pdb`
--

DROP TABLE IF EXISTS `pdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pdb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(16) NOT NULL,
  `chains` text,
  `residues` text,
  `atoms` text,
  `protein_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `protein_id` (`protein_id`),
  CONSTRAINT `pdb_ibfk_1` FOREIGN KEY (`protein_id`) REFERENCES `cancer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pdb`
--

LOCK TABLES `pdb` WRITE;
/*!40000 ALTER TABLE `pdb` DISABLE KEYS */;
INSERT INTO `pdb` VALUES (1,'P53 1UTP Model','Chain: E. Number of residues: 43. Number of atoms: 442,                                    Chain: F. Number of residues: 35. Number of atoms: 449,                                    Chain: A. Number of residues: 395. Number of atoms: 1734,                                    Chain: B. Number of residues: 265. Number of atoms: 1593,                                    Chain: C. Number of residues: 276. Number of atoms: 1610','H_ZN=951 H_ZN=952H_ZN=953','Residue SER het=  resseq=94 icode=',1),(2,'MYC 1NKP Model','Chain: F. Number of residues: 81. Number of atoms: 447,                                     Chain: G. Number of residues: 86. Number of atoms: 452,                                    Chain: H. Number of residues: 79. Number of atoms: 445,                                    Chain: J. Number of residues: 84. Number of atoms: 450,                                    Chain: A. Number of residues: 179. Number of atoms: 824,                                    Chain: B. Number of residues: 158. Number of atoms: 761,                                    Chain: D. Number of residues: 165. Number of atoms: 787,                                    Chain: E. Number of residues: 160. Number of atoms: 740','Most of the residues are HOH: 992','Residue DC het=  resseq=101 icode=',2),(3,'ERRB2 1N8Z MODEL','Chain: A. Number of residues: 233. Number of atoms: 1664,                                      Chain: B. Number of residues: 233. Number of atoms: 1655,                                     Chain: C. Number of residues: 631. Number of atoms: 4571','H_NAG=766, H_NAG=738, H_SO4=1001','Residue ASP het=  resseq=1 icode=',3),(4,'EGFR 1JL9 MODEL','Chain: A. Number of residues: 47. Number of atoms: 335,                                     Chain: B. Number of residues: 47. Number of atoms: 369','Most of the residues are HOH: 1','Residue CYS he resseq=6 icode',4),(5,'PTEN 1D5R MODEL','Chain: A. Number of residues: 690. Number of atoms: 2968','H_TLA=352','Residue ARG het  resseq=14 icode',5);
/*!40000 ALTER TABLE `pdb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-30 23:35:42
