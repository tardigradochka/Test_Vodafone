# Import and creation database and table with columns. Data filling. Checking the file

import psycopg2
import pandas as pd


# Connection to DB
hostname = 'localhost'
database = 'KPI_inet'
username = 'postgres'
pwd = '1107'
port_id = 5432


conn = None
cur = None


try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor()

# Creation the table with columns
    cur.execute('DROP TABLE IF EXISTS i_kpis')

    create_script = ''' CREATE TABLE IF NOT EXISTS i_kpis (
                            id  int PRIMARY KEY,
                            speed_u_mbps   float(24), 
                            speed_d_mbps    float(24),
                            latency_ms  float(24), 
                            packet_loss_proc    float(24),
                            bandwidth_proc  float(24), 
                            response_time_ms    float(24))'''
    cur.execute(create_script)

#Adding the data to db
    insert_script = 'INSERT INTO i_kpis (id, speed_u_mbps, speed_d_mbps, latency_ms, \
    packet_loss_proc, bandwidth_proc, response_time_ms) VALUES(%s, %s, %s, %s, %s, %s, %s)'

    list_values = [(1, 19.93475, 42.39537, 21.85430, 0.99934, 0.675, 56.55854),
                   (2, 17.97978, 49.97638, 47.78214, 1.49349, 0.645, 58.78246),
                   (3, 10.45538, 86.18200, 37.93972, 1.12533, 0.278, 46.54882),
                   (4, 31.14880, 37.30041, 31.93963, 0.16660, 0.371, 37.79468),
                   (5, 24.87795, 87.61672, 12.02083, 0.37116, 0.202, 23.87547),
                   (6, 43.55364, 13.37277, 12.01975, 0.43865, 0.780, 24.67897),
                   (7, 3.54125, 78.79585, 7.61376, 0.51572, 0.514, 18.78630),
                   (8, 32.90566, 85.51702, 43.97792, 1.13080, 0.320, 49.87603),
                   (9, 38.62154, 22.27267, 32.05017, 1.00793, 0.448, 41.38690)]


    for i in list_values:
        cur.execute(insert_script, i)


#Showing the data and close db after that
    cur.execute('SELECT * FROM i_kpis')
    for record in cur.fetchall():
        record_str = str(record)
        print(record_str)


    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


#File was previously saved by using PostgresSQL
#Pandas. Read and display csv.file
df = pd.read_csv('kpis_for_internet.csv')
print(df)



