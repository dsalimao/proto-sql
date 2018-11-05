from mysql.conn_pool import mysql_pool


def _init_meta():
    mysql_pool.execute('''
    CREATE TABLE IF NOT EXISTS proto_table_meta (
    table_name VARCHAR(200) NOT NULL,
    db_column VARCHAR(200) NOT NULL,
    py_column VARCHAR(200) NOT NULL,
    type INT NOT NULL,
    PRIMARY KEY (table_name, db_column)
    );
    ''')


def _get_table_meta(table):
    rows = mysql_pool.execute('''
    SELECT * FROM proto_table_meta WHERE table_name = %s
    ''', (table,), return_one=False)

    colums = []
    for row in rows:
        colums.append({'db_column': row['db_column'], 'py_column': row['py_column'], 'type': row['type']})

    return colums


def _replace_table_meta(table, columns, cursor=None):
    def execute(cursor):
        cursor.execute('''
                    DELETE FROM proto_table_meta where table_name = "%s"
                    ''', (table, ))
        for column in columns:
            cursor.execute('''
                    REPLACE INTO proto_table_meta (table_name, db_column, py_column, type) VALUES (%s, %s, %s, %s)
                    ''', (table, column['db_column'], column['py_column'], column['type']))

    if cursor:
        execute(cursor)
        return
    else:
        conn = mysql_pool.start_manual()
        try:
            with conn.cursor() as cursor:
                execute(cursor)
            conn.commit()
        except Exception as e:
            raise e
        finally:
            mysql_pool.end_manual(conn)
