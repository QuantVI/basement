import sqlite3

conn = sqlite3.connect('mydb.db')

# tcs means table creation strings
tcs = {
    'client_apps': [],
    'columns':[],
    'databases':[],
    'maintenance_windows':[],
    'raspberry_pis':[],
    'sql_configs':[],
    'sql_servers':[],
    'tables':[]
    }

a = '''
create table {}
(
'''
