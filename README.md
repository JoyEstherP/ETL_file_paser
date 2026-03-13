# ETL_file_paser
To read the file from soures where the file in encrypted and decompressed 



ITC Transactions Data Ingestion Pipeline
Overview

This project demonstrates a data ingestion pipeline that processes encrypted transaction files and loads the data into a MySQL database.

The pipeline performs the following steps:

Decrypts a .gpg encrypted file

Decompresses the .gz compressed file

Reads the CSV file using Pandas

Loads the transaction data into a MySQL table

This project simulates a real-world data engineering workflow where data arrives in encrypted and compressed formats before being processed and stored in a database.

Project Architecture
Encrypted File (.gpg)
        │
        ▼
Decryption (GPG)
        │
        ▼
Decompression (.gz)
        │
        ▼
CSV File
        │
        ▼
Pandas Data Processing
        │
        ▼
MySQL Database
Technologies Used

Python

Pandas

MySQL

PyMySQL

GnuPG

gzip

shutil
