# Import data from sql to html. Creation html.page
import pandas as pd
import psycopg2


# Connection with db
hostname = 'localhost'
database = 'KPI_inet'
username = 'postgres'
pwd = '1107'
port_id = 5432


my_db = None
cur = None


my_db = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)


#Getting the data
my_cursor = my_db.cursor()
my_cursor.execute('SELECT * FROM i_kpis')
db_result = my_cursor.fetchall()
print(db_result)


#Getting the name of columns
data = pd.read_csv('kpis_for_internet.csv')
data_top = data.keys()


#Import to html
df = pd.DataFrame(db_result, columns=data_top)
df.to_html('templates/sql_data.html', index=False)






#df = pd.DataFrame()
# for i in db_result:
#         df2 = pd.DataFrame(list(i)).T
#         df = pd.concat([df, df2])
#
#
# df.to_html('templates/sql_data.html')

