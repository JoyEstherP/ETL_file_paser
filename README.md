# ETL_file_paser
To read the file from soures where the file in encrypted and decompressed 
( read encrypted csv and uploading it to msql db)

**Pipeline Flow:**

Encrypted File
   ↓
Decrypt
   ↓
Decompress
   ↓
Parse CSV
   ↓
Load to MySQL
