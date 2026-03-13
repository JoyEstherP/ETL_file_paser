import gnupg
import gzip
import shutil
import pymysql
import pandas as pd

file_name = "ITC_transactions.csv"
decrypted_file_name = "ITC_transactions.csv.gz"
encrypted_file_name = "ITC_transactions.csv.gz.gpg"

# Decrypt
gpg = gnupg.GPG()

with open(encrypted_file_name,"rb") as file:
    status = gpg.decrypt_file(file, output=decrypted_file_name)

if status.ok:
    print("Decryption successful")
else:
    print("Decryption failed", status.stderr)

# Decompress
with gzip.open(decrypted_file_name,"rb") as f_in:
    with open(file_name,"wb") as f_out:
        shutil.copyfileobj(f_in,f_out)

print("Decompression completed")

def create_table_query():
    query = """CREATE TABLE IF NOT EXISTS itc_transactions (
        transaction_id VARCHAR(20),
        transaction_date DATE,
        customer_id VARCHAR(20),
        product_category VARCHAR(50),
        product_name VARCHAR(100),
        quantity INT,
        unit_price DECIMAL(10,2),
        total_amount DECIMAL(10,2),
        payment_method VARCHAR(20),
        region VARCHAR(50)
    );"""
    return query

def sql_connection(df):

    my_sql_config = {
        "host": "localhost",
        "password": "root@1998",
        "database": "itc",
        "user": "root"
    }

    connection = pymysql.connect(**my_sql_config)
    cursor = connection.cursor()

    cursor.execute(create_table_query())

    data = df.values.tolist()

    insert_query = """INSERT INTO itc_transactions(
        transaction_id,
        transaction_date,
        customer_id,
        product_category,
        product_name,
        quantity,
        unit_price,
        total_amount,
        payment_method,
        region
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    cursor.executemany(insert_query, data)

    connection.commit()
    cursor.close()
    connection.close()

def read_file_csv():
    df = pd.read_csv(file_name)
    sql_connection(df)

read_file_csv()
