#ifndef CERT_H
#define CERT_H

#include <Arduino.h>

//2037.09.30 AC Camerfirma, S.A.:AC Camerfirma SA CIF A82743287:http://www.chambersign.org
//2038.07.31 AC Camerfirma, S.A.:AC Camerfirma S.A.:
//2038.07.31 AC Camerfirma, S.A.:AC Camerfirma S.A.:
//2030.09.22 Actalis:Actalis S.p.A./03358520967:
//2044.04.26 Agence Nationale de Certification Electronique:Agence Nationale de Certification Electronique:
//2038.01.17 Amazon Trust Services:Amazon:
//2040.05.26 Amazon Trust Services:Amazon:
//2040.05.26 Amazon Trust Services:Amazon:
//2040.05.26 Amazon Trust Services:Amazon:
//2037.12.31 Amazon Trust Services:Starfield Technologies, Inc.:
//2027.06.11 Asseco Data Systems S.A. (previously Unizeto Certum):Unizeto Sp. z o.o.:
//2043.03.26 Asseco Data Systems S.A. (previously Unizeto Certum):Asseco Data Systems S.A.:Certum Certification Authority
//2029.12.31 Asseco Data Systems S.A. (previously Unizeto Certum):Unizeto Technologies S.A.:Certum Certification Authority
//2046.10.06 Asseco Data Systems S.A. (previously Unizeto Certum):Unizeto Technologies S.A.:Certum Certification Authority
//2043.03.16 Asseco Data Systems S.A. (previously Unizeto Certum):Asseco Data Systems S.A.:Certum Certification Authority
//2030.12.31 Atos Trustcenter:Atos:
//2036.05.05 Autoridad de Certificacion Firmaprofesional::
//2030.12.31 Autoridad de Certificacion Firmaprofesional::
//2039.08.30 Autoridad de Certificación (ANF AC):ANF Autoridad de Certificacion:ANF CA Raiz
//2040.10.26 Buypass:Buypass AS-983163327:
//2040.10.26 Buypass:Buypass AS-983163327:
//2046.04.01 Certainly LLC:Certainly:
//2046.04.01 Certainly LLC:Certainly:
//2027.06.29 Certigna:Dhimyotis:
//2033.10.01 Certigna:Dhimyotis:0002 48146308100036
//2031.07.04 certSIGN:certSIGN:certSIGN ROOT CA
//2042.02.06 certSIGN:CERTSIGN SA:certSIGN ROOT CA G2
//2029.12.31 China Financial Certification Authority (CFCA):China Financial Certification Authority:
//2034.12.20 Chunghwa Telecom:Chunghwa Telecom Co., Ltd.:ePKI Root Certification Authority
//2037.12.31 Chunghwa Telecom:Chunghwa Telecom Co., Ltd.:
//2029.04.08 Cybertrust Japan / JCSI:Japan Certification Services, Inc.:
//2035.02.11 D-Trust:D-Trust GmbH:
//2035.02.11 D-Trust:D-Trust GmbH:
//2028.09.20 D-Trust:D-Trust GmbH:
//2029.11.05 D-Trust:D-Trust GmbH:
//2029.11.05 D-Trust:D-Trust GmbH:
//2033.10.01 Deutsche Telekom Security GmbH:T-Systems Enterprise Services GmbH:T-Systems Trust Center
//2033.10.01 Deutsche Telekom Security GmbH:T-Systems Enterprise Services GmbH:T-Systems Trust Center
//2025.05.12 DigiCert:Baltimore:CyberTrust
//2031.11.10 DigiCert:DigiCert Inc:www.digicert.com
//2038.01.15 DigiCert:DigiCert Inc:www.digicert.com
//2038.01.15 DigiCert:DigiCert Inc:www.digicert.com
//2031.11.10 DigiCert:DigiCert Inc:www.digicert.com
//2038.01.15 DigiCert:DigiCert Inc:www.digicert.com
//2038.01.15 DigiCert:DigiCert Inc:www.digicert.com
//2031.11.10 DigiCert:DigiCert Inc:www.digicert.com
//2046.01.14 DigiCert:DigiCert, Inc.:
//2046.01.14 DigiCert:DigiCert, Inc.:
//2046.01.14 DigiCert:DigiCert, Inc.:
//2046.01.14 DigiCert:DigiCert, Inc.:
//2038.01.15 DigiCert:DigiCert Inc:www.digicert.com
//2037.12.01 DigiCert:Symantec Corporation:Symantec Trust Network
//2037.12.01 DigiCert:Symantec Corporation:Symantec Trust Network
//2036.07.16 DigiCert:VeriSign, Inc.:VeriSign Trust Network, (c) 1999 VeriSign, Inc. - For authorized use only
//2036.07.16 DigiCert:VeriSign, Inc.:VeriSign Trust Network, (c) 1999 VeriSign, Inc. - For authorized use only
//2046.01.15 DigitalSign - Certificadora Digital, S.A:DigitalSign Certificadora Digital:
//2046.01.15 DigitalSign - Certificadora Digital, S.A:DigitalSign Certificadora Digital:
//2042.07.19 Disig, a.s.:Disig a.s.:
//2040.06.10 e-commerce monitoring GmbH:e-commerce monitoring GmbH:
//2023.03.03 E-Tugra:E-Tuğra EBG Bilişim Teknolojileri ve Hizmetleri A.Ş.:E-Tugra Sertifikasyon Merkezi
//2045.03.12 E-Tugra:E-Tugra EBG A.S.:E-Tugra Trust Center
//2045.03.12 E-Tugra:E-Tugra EBG A.S.:E-Tugra Trust Center
//2043.02.18 eMudhra Technologies Limited:eMudhra Inc:emSign PKI
//2043.02.18 eMudhra Technologies Limited:eMudhra Technologies Limited:emSign PKI
//2043.02.18 eMudhra Technologies Limited:eMudhra Inc:emSign PKI
//2043.02.18 eMudhra Technologies Limited:eMudhra Technologies Limited:emSign PKI
//2030.12.31 Entrust:AffirmTrust:
//2030.12.31 Entrust:AffirmTrust:
//2040.12.31 Entrust:AffirmTrust:
//2040.12.31 Entrust:AffirmTrust:
//2026.11.27 Entrust:Entrust, Inc.:www.entrust.net/CPS is incorporated by reference, (c) 2006 Entrust, Inc.
//2037.12.18 Entrust:Entrust, Inc.:See www.entrust.net/legal-terms, (c) 2012 Entrust, Inc. - for authorized use only
//2030.12.07 Entrust:Entrust, Inc.:See www.entrust.net/legal-terms, (c) 2009 Entrust, Inc. - for authorized use only
//2037.12.27 Entrust:Entrust, Inc.:See www.entrust.net/legal-terms, (c) 2015 Entrust, Inc. - for authorized use only
//2029.07.24 Entrust:Entrust.net:www.entrust.net/CPS_2048 incorp. by ref. (limits liab.), (c) 1999 Entrust.net Limited
//2040.12.31 Global Digital Cybersecurity Authority Co., Ltd. (Formerly Guang Dong Certificate Authority (GDCA)):GUANG DONG CERTIFICATE AUTHORITY CO.,LTD.:
//2029.03.18 GlobalSign nv-sa:GlobalSign:GlobalSign Root CA - R3
//2038.01.19 GlobalSign nv-sa:GlobalSign:GlobalSign ECC Root CA - R5
//2034.12.10 GlobalSign nv-sa:GlobalSign:GlobalSign Root CA - R6
//2028.01.28 GlobalSign nv-sa:GlobalSign nv-sa:Root CA
//2046.03.20 GlobalSign nv-sa:GlobalSign nv-sa:
//2046.03.20 GlobalSign nv-sa:GlobalSign nv-sa:
//2045.03.18 GlobalSign nv-sa:GlobalSign nv-sa:
//2045.03.18 GlobalSign nv-sa:GlobalSign nv-sa:
//2034.06.29 GoDaddy:The Go Daddy Group, Inc.:Go Daddy Class 2 Certification Authority
//2037.12.31 GoDaddy:GoDaddy.com, Inc.:
//2034.06.29 GoDaddy:Starfield Technologies, Inc.:Starfield Class 2 Certification Authority
//2037.12.31 GoDaddy:Starfield Technologies, Inc.:
//2038.01.19 Google Trust Services LLC:GlobalSign:GlobalSign ECC Root CA - R4
//2036.06.22 Google Trust Services LLC:Google Trust Services LLC:
//2036.06.22 Google Trust Services LLC:Google Trust Services LLC:
//2036.06.22 Google Trust Services LLC:Google Trust Services LLC:
//2036.06.22 Google Trust Services LLC:Google Trust Services LLC:
//2023.05.15 Government of Hong Kong (SAR), Hongkong Post, Certizen:Hongkong Post:
//2042.06.03 Government of Hong Kong (SAR), Hongkong Post, Certizen:Hongkong Post:
//2030.12.31 Government of Spain, Autoritat de Certificació de la Comunitat Valenciana (ACCV):ACCV:PKIACCV
//2043.12.20 Government of Spain, Fábrica Nacional de Moneda y Timbre (FNMT):FNMT-RCM:Ceres
//2030.01.01 Government of Spain, Fábrica Nacional de Moneda y Timbre (FNMT):FNMT-RCM:AC RAIZ FNMT-RCM
//2028.11.13 Government of The Netherlands, PKIoverheid (Logius):Staat der Nederlanden:
//2043.10.25 Government of Turkey, Kamu Sertifikasyon Merkezi (Kamu SM):Turkiye Bilimsel ve Teknolojik Arastirma Kurumu - TUBITAK:Kamu Sertifikasyon Merkezi - Kamu SM
//2045.02.13 HARICA:Hellenic Academic and Research Institutions CA:
//2045.02.13 HARICA:Hellenic Academic and Research Institutions CA:
//2045.02.13 HARICA:Hellenic Academic and Research Institutions CA:
//2045.02.13 HARICA:Hellenic Academic and Research Institutions CA:
//2040.06.30 HARICA:Hellenic Academic and Research Institutions Cert. Authority:
//2040.06.30 HARICA:Hellenic Academic and Research Institutions Cert. Authority:
//2034.01.16 IdenTrust Services, LLC:IdenTrust:
//2034.01.16 IdenTrust Services, LLC:IdenTrust:
//2035.06.04 Internet Security Research Group:Internet Security Research Group:
//2040.09.17 Internet Security Research Group:Internet Security Research Group:
//2043.07.31 iTrusChina Co., Ltd.:iTrusChina Co.,Ltd.:
//2043.07.31 iTrusChina Co., Ltd.:iTrusChina Co.,Ltd.:
//2037.12.13 Izenpe S.A.:IZENPE S.A.:
//2035.10.19 Krajowa Izba Rozliczeniowa S.A. (KIR):Krajowa Izba Rozliczeniowa S.A.:
//2042.08.22 Microsec Ltd.:Microsec Ltd.:
//2029.12.30 Microsec Ltd.:Microsec Ltd.:
//2042.07.18 Microsoft Corporation:Microsoft Corporation:
//2042.07.18 Microsoft Corporation:Microsoft Corporation:
//2037.08.18 NAVER Cloud:NAVER BUSINESS PLATFORM Corp.:
//2028.12.06 Netlock:NetLock Kft.:Tanúsítványkiadók (Certification Services)
//2037.12.11 OISTE:WISeKey:Copyright (c) 2005, OISTE Foundation Endorsed
//2039.12.01 OISTE:WISeKey:OISTE Foundation Endorsed
//2042.05.09 OISTE:WISeKey:OISTE Foundation Endorsed
//2042.01.12 QuoVadis:QuoVadis Limited:
//2031.11.24 QuoVadis:QuoVadis Limited:
//2042.01.12 QuoVadis:QuoVadis Limited:
//2031.11.24 QuoVadis:QuoVadis Limited:
//2042.01.12 QuoVadis:QuoVadis Limited:
//2023.09.30 SECOM Trust Systems CO., LTD.:SECOM Trust.net:Security Communication RootCA1
//2038.01.18 SECOM Trust Systems CO., LTD.:SECOM Trust Systems CO.,LTD.:
//2029.05.29 SECOM Trust Systems CO., LTD.:SECOM Trust Systems CO.,LTD.:Security Communication RootCA2
//2038.01.18 SECOM Trust Systems CO., LTD.:SECOM Trust Systems CO.,LTD.:
//2028.12.31 Sectigo:Comodo CA Limited:
//2029.12.31 Sectigo:COMODO CA Limited:
//2038.01.18 Sectigo:COMODO CA Limited:
//2038.01.18 Sectigo:COMODO CA Limited:
//2038.01.18 Sectigo:The USERTRUST Network:
//2038.01.18 Sectigo:The USERTRUST Network:
//2038.12.31 Shanghai Electronic Certification Authority Co., Ltd.:UniTrust:
//2040.12.31 Shanghai Electronic Certification Authority Co., Ltd.:UniTrust:
//2041.02.12 SSL.com:SSL Corporation:
//2042.05.30 SSL.com:SSL Corporation:
//2041.02.12 SSL.com:SSL Corporation:
//2041.02.12 SSL.com:SSL Corporation:
//2036.10.25 SwissSign AG:SwissSign AG:
//2036.10.25 SwissSign AG:SwissSign AG:
//2030.12.31 Taiwan-CA Inc. (TWCA):TAIWAN-CA:Root CA
//2030.12.31 Taiwan-CA Inc. (TWCA):TAIWAN-CA:Root CA
//2043.11.29 Telia Company:Telia Finland Oyj:
//2032.10.18 Telia Company:TeliaSonera:
//2029.12.31 TrustCor Systems:TrustCor Systems S. de R.L.:TrustCor Certificate Authority
//2029.12.31 TrustCor Systems:TrustCor Systems S. de R.L.:TrustCor Certificate Authority
//2034.12.31 TrustCor Systems:TrustCor Systems S. de R.L.:TrustCor Certificate Authority
//2029.12.31 Viking Cloud, Inc.:SecureTrust Corporation:
//2029.12.31 Viking Cloud, Inc.:SecureTrust Corporation:
//2042.08.23 Viking Cloud, Inc.:Trustwave Holdings, Inc.:
//2042.08.23 Viking Cloud, Inc.:Trustwave Holdings, Inc.:
//2042.08.23 Viking Cloud, Inc.:Trustwave Holdings, Inc.:
//2035.01.01 Viking Cloud, Inc.:XRamp Security Services Inc:www.xrampsecurity.com
//global variables for certificates using 0 bytes
const uint16_t numberOfCertificates PROGMEM = 0;

const uint16_t certSizes[] PROGMEM = {};

const uint8_t* const certificates[] PROGMEM = {};

const uint8_t* const indices[] PROGMEM = {};

#endif
