import mysql.connector

from src.utils.app_config import AppConfig


class DAL:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=AppConfig.mysql_host,
                user=AppConfig.mysql_user,
                password=AppConfig.mysql_password,
                database=AppConfig.mysql_database,
            )
            self.connection.autocommit = True
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            self.connection = None

    def _validate_query_params(self, query, params):
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")
        if params is not None and not isinstance(params, tuple):
            raise ValueError("Params must be a tuple or None.")

    def _execute_query(self, query, params=None, fetchall=False, fetchone=False):
        self._validate_query_params(query, params)
        if self.connection:
            try:
                with self.connection.cursor(dictionary=True) as cursor:
                    cursor.execute(query, params)
                    if fetchall:
                        return cursor.fetchall()
                    elif fetchone:
                        return cursor.fetchone()
                    else:
                        self.connection.commit()
                        return cursor
            except mysql.connector.Error as err:
                print(f"Error executing query: {err}")
        return None

    def get_table(self, query, params=None):
        return self._execute_query(query, params, fetchall=True)

    def get_scalar(self, query, params=None):
        return self._execute_query(query, params, fetchone=True)

    def insert(self, query, params=None):
        return self._execute_query(query, params)

    def update(self, query, params=None):
        return self._execute_query(query, params)

    def delete(self, query, params=None):
        return self._execute_query(query, params)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
        else:
            raise ValueError("Connection not established.")
