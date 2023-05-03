import psycopg2
import psycopg2.extras

class DBPG:

    def __init__(self, IP, user, password, db):
        self.IP = IP
        self.user = user
        self.password = password
        self.db = db
        """
        self.lines = []
        self.sql_list = []
        self.table_index = {}
        self.i = 0
        """

    def select(self, sql) -> object:
        # Connect to your postgres DB
        conn = psycopg2.connect(host=self.IP, database=self.db, user=self.user, password=self.password, port="5432")
        # Open a cursor to perform database operations
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        # cur = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # Execute a query
        cur.execute(sql)
        # Retrieve query results
        records = cur.fetchall()
        # print(f"Records >>> {records}")
        return records

    def insert(self, sql):
        # Connect to your postgres DB
        conn = psycopg2.connect(host=self.IP, database=self.db, user=self.user, password=self.password, port="5432")
        # Open a cursor to perform database operations
        cur = conn.cursor()
        # Execute a query
        cur.execute(sql)
        conn.commit()
        return

    def execute_sql(self, sql):
        # Connect to your postgres DB
        conn = psycopg2.connect(host=self.IP, database=self.db, user=self.user, password=self.password, port="5432")
        # Open a cursor to perform database operations
        cur = conn.cursor()
        # Execute a query
        cur.execute(sql)
        conn.commit()
        return

    def execute_sql_lines(self, sql_lines):
        if len(sql_lines) == 0: return
        sqls = ""
        for sql in sql_lines:
            sqls = sqls + sql + ";"
        # Connect to your postgres DB
        conn = psycopg2.connect(host=self.IP, database=self.db, user=self.user, password=self.password, port="5432")
        # Open a cursor to perform database operations
        cur = conn.cursor()
        # Execute a query
        cur.execute(sqls)
        conn.commit()
        return


    def update(self, **kwargs):
        table = kwargs.get('table')
        where = kwargs.get('where')
        if table is None:
            print("Erro: Tabela não definida")
            return True, "Erro: Tabela não definida"
        if where is None:
            print("Erro: Tabela não definida")
            return True, "Erro: WHERE não definido"

        set = ""
        for key, value in kwargs.items():
            if key == "table" or key == "where":
                pass
            else:
                set += f"{key} = '{value}', "
        set = set[:-2]
        sql = f"UPDATE {table} SET {set} WHERE {where};"
        print(sql)
        self.execute_sql(sql)
        return False, "ok"




    def insert_into_line(self, table, line):
        fields = "("
        values = "("
        i = 0
        for key, value in line.items():
            i += 1
            if i ==1 :
                fields = fields + f"{str(key)}"
                values = values + f"'{str(value)}'"
            else:
                fields = fields + f", {str(key)}"
                values = values + f", '{str(value)}'"
        fields = fields + ")"
        values = values + ")"

        # print(fields)
        # print(values)

        sql = f"insert into {table} {fields} values {values};"
        print(sql)
        self.insert(sql=sql)

    def insert_into_lines(self, table, lines):
        fields = "("
        values = ""
        i = 0
        if len(lines) == 0: return
        line1 = lines[0]

        for key, value in line1.items():
            i += 1
            if i ==1 :
                fields = fields + f"{str(key)}"
            else:
                fields = fields + f", {str(key)}"
        fields = fields + ")"

        for line in lines:
            i = 0
            values = values + "("
            for key, value in line.items():
                i += 1
                if i == 1:
                    values = values + f"'{str(value)}'"
                else:
                    values = values + f", '{str(value)}'"
            values = values + "),"
        values = values[:-1] + ";"

        sql = f"insert into {table} {fields} values {values}"
        # print(sql)
        self.insert(sql=sql)


    def insert_into_lines_on_conflit_do_nothing(self, table, lines, conflit_field):
        fields = "("
        values = ""
        i = 0
        if len(lines) == 0: return
        line1 = lines[0]

        for key, value in line1.items():
            i += 1
            if i ==1 :
                fields = fields + f"{str(key)}"
            else:
                fields = fields + f", {str(key)}"
        fields = fields + ")"

        for line in lines:
            i = 0
            values = values + "("
            for key, value in line.items():
                i += 1
                if i == 1:
                    values = values + f"'{str(value)}'"
                else:
                    values = values + f", '{str(value)}'"
            values = values + "),"
        values = values[:-1]

        sql = f"insert into {table} {fields} values {values} ON CONFLICT ({conflit_field}) DO NOTHING;"
        # print(sql)
        self.insert(sql=sql)
