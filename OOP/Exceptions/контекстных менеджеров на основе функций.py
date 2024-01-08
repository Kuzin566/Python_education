from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Начало контекстного менеджера ...")
    yield "Ух ты как круто!"
    print("Конец контекстного менеджера...")


with my_context_manager() as phrase:
    print(phrase)


@contextmanager
def get_mysql_conn(db):
    """
    Context manager to automatically close DB connection.
    We retrieve credentials from Environment variables
    """
    conn = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PWD'),
        database=db
    )

    try:
        yield conn
    finally:
        conn.close()
