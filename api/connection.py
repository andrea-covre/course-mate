import textwrap
import pyodbc

class SQLConnectionObject:
    def __init__(self):
        self.driver = '{ODBC Driver 18 for SQL Server}'
        self.server_name = 'internationalserver'
        self.database_name = 'InternationalDB'
        self.server = '{server}.database.windows.net, 1433'.format(server=self.server_name)
        self.username = "theinternational"
        self.password = "dummy_password"

    def create_connection_string(self) -> str:
        connection_string = textwrap.dedent('''
            Driver={driver};
            Server={server};
            Database={database};
            Uid={username};
            Pwd={password};
            Encrypt=yes;
            TrustServerCertificate=no;
            Connection Timeout=30;
        '''.format(
            driver=self.driver,
            server=self.server,
            database=self.database_name,
            username=self.username,
            password=self.password
        ))

        return connection_string


    def open_connection(self):
        connection_string = self.create_connection_string()
        cnxn: pyodbc.Connection = pyodbc.connect(connection_string)
        crsr: pyodbc.Cursor = cnxn.cursor()
        return cnxn, crsr

        
    