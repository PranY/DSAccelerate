import pandas as pd
import pyodbc
import redis


def read_csv_file(csv_path):
    """
    Reads a CSV file using the pandas library.

    Args:
        csv_path (str): The path to the CSV file to read.

    Returns:
        pandas.DataFrame: A pandas DataFrame object containing the data from the CSV file.

    Raises:
        FileNotFoundError: If the CSV file cannot be found at the specified path.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If there is an error parsing the CSV file.

    Examples:
        >>> df = read_csv_file('my_data.csv')
        >>> print(df.head())

    """
    try:
        # Use pandas to read the CSV file
        df = pd.read_csv(csv_path)
        return df

    except FileNotFoundError as e:
        print(f"Error: {e}. Please verify the file path and try again.")

    except pd.errors.EmptyDataError as e:
        print(f"Error: {e}. The CSV file is empty.")

    except pd.errors.ParserError as e:
        print(f"Error: {e}. There was an error parsing the CSV file.")


def read_csv_url(url):
    """
    Reads a CSV file from a URL using the pandas library.

    Args:
        url (str): The URL path to the CSV file to read.

    Returns:
        pandas.DataFrame: A pandas DataFrame object containing the data from the CSV file.

    Raises:
        ValueError: If the URL path is invalid or if the CSV file cannot be read.
        pd.errors.EmptyDataError: If the CSV file is empty.
        pd.errors.ParserError: If there is an error parsing the CSV file.

    Examples:
        >>> df = read_csv_url('https://example.com/my_data.csv')
        >>> print(df.head())

    """
    try:
        # Use pandas to read the CSV file from the URL
        df = pd.read_csv(url)
        return df

    except ValueError as e:
        print(f"Error: {e}. Please verify the URL path and try again.")

    except pd.errors.EmptyDataError as e:
        print(f"Error: {e}. The CSV file is empty.")

    except pd.errors.ParserError as e:
        print(f"Error: {e}. There was an error parsing the CSV file.")


def read_sql_query(query_str, **kwargs):
    """
    Reads data using a SQL query provided as a string.

    Args:
        query_str (str): The SQL query to execute.

    Keyword Args:
        server (str): The name or IP address of the server to connect to.
        database (str): The name of the database to connect to.
        username (str): The username to use for authentication.
        password (str): The password to use for authentication.
        driver (str): The name of the ODBC driver to use for the connection.

    Returns:
        pandas.DataFrame: A pandas DataFrame object containing the data from the SQL query.

    Raises:
        ValueError: If the SQL query is empty.
        pyodbc.Error: If there is an error connecting to the SQL server or executing the query.

    Examples:
        >>> query = "SELECT * FROM my_table WHERE id = '123'"
        >>> df = read_sql_query(query, server='my_server', database='my_db', username='my_user', password='my_password', driver='{ODBC Driver 17 for SQL Server}')
        >>> print(df.head())

    """
    # Check if the query string is empty
    if not query_str:
        raise ValueError("Error: the SQL query string is empty.")

    # Check if any connection parameters are provided
    if not kwargs:
        raise ValueError("Error: no SQL connector parameters were provided.")

    # Set the default ODBC driver if not specified
    driver = kwargs.get("driver", "{ODBC Driver 17 for SQL Server}")

    try:
        # Connect to the SQL server using the provided parameters
        conn = pyodbc.connect(
            f"DRIVER={driver};SERVER={kwargs['server']};DATABASE={kwargs['database']};UID={kwargs['username']};PWD={kwargs['password']}"
        )

        # Use pandas to execute the SQL query and return the result as a DataFrame
        df = pd.read_sql_query(query_str, conn)
        return df

    except pyodbc.Error as e:
        print(
            f"Error: {e}. There was an error connecting to the SQL server or executing the query."
        )


def read_redis_data(redis_url: str, redis_key: str, redis_db: int = 0) -> pd.DataFrame:
    """
    Reads data from Redis and loads it into a Pandas dataframe.

    Parameters:
        redis_url (str): The URL of the Redis server to connect to.
        redis_key (str): The key of the Redis hash to read from.
        redis_db (int, optional): The index of the Redis database to connect to (default: 0).

    Returns:
        pd.DataFrame: A Pandas dataframe containing the data from the Redis hash.

    Raises:
        redis.exceptions.ConnectionError: If a connection to the Redis server cannot be established.
        redis.exceptions.ResponseError: If the Redis hash does not exist or is empty.
    """
    # Create a Redis client and connect to the specified Redis server and database
    r = redis.Redis.from_url(redis_url, db=redis_db)

    # Read the data from the specified Redis hash key as a dictionary
    data_dict = r.hgetall(redis_key)

    # Check if the Redis hash is empty
    if not data_dict:
        raise redis.exceptions.ResponseError(
            f"Redis hash '{redis_key}' is empty or does not exist."
        )

    # Convert the dictionary to a Pandas dataframe
    df = pd.DataFrame.from_dict(data_dict, orient="index", columns=["value"])

    return df
