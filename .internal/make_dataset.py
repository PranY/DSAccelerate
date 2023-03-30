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

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif, f_regression

class FeatureEngineering:
    """
    A class for feature engineering in machine learning.
    """

    def __init__(self, df: pd.DataFrame, problem_type: str):
        """
        Initializes the FeatureEngineering class with a pandas DataFrame and a problem type.
        """
        self.df = df
        self.problem_type = problem_type

    def impute_missing(self, method: str = 'mean') -> pd.DataFrame:
        """
        Imputes missing values in the DataFrame.

        Parameters:
        - method (str): The method to use for imputing missing values. Default is 'mean'.
        
        Returns:
        - pd.DataFrame: The updated DataFrame with imputed missing values.
        """
        if method == 'mean':
            return self.df.fillna(self.df.mean())
        elif method == 'median':
            return self.df.fillna(self.df.median())
        else:
            raise ValueError("Invalid imputation method. Valid options are 'mean' and 'median'.")

    def scale(self) -> pd.DataFrame:
        """
        Scales the DataFrame using StandardScaler.

        Returns:
        - pd.DataFrame: The updated DataFrame with scaled features.
        """
        scaler = StandardScaler()
        return pd.DataFrame(scaler.fit_transform(self.df), columns=self.df.columns)

    def select_k_best(self, k: int = 10) -> pd.DataFrame:
        """
        Performs feature selection using SelectKBest.

        Parameters:
        - k (int): The number of top features to select. Default is 10.

        Returns:
        - pd.DataFrame: The updated DataFrame with selected features.
        """
        if self.problem_type == 'classification':
            selector = SelectKBest(score_func=f_classif, k=k)
        elif self.problem_type == 'regression':
            selector = SelectKBest(score_func=f_regression, k=k)
        else:
            raise ValueError("Invalid problem type. Valid options are 'classification' and 'regression'.")

        return pd.DataFrame(selector.fit_transform(self.df), columns=self.df.columns[selector.get_support()])

    def encode_categorical(self, columns: list) -> pd.DataFrame:
        """
        Encodes categorical variables using one-hot encoding.

        Parameters:
        - columns (list): A list of column names to encode.

        Returns:
        - pd.DataFrame: The updated DataFrame with encoded categorical variables.
        """
        return pd.get_dummies(self.df, columns=columns)

    def apply_log_transform(self, columns: list) -> pd.DataFrame:
        """
        Applies a log transform to specified columns in the DataFrame.

        Parameters:
        - columns (list): A list of column names to apply the log transform to.

        Returns:
        - pd.DataFrame: The updated DataFrame with log-transformed columns.
        """
        return self.df[columns].apply(lambda x: np.log(x + 1))

    def execute_feature_engineering(self, methods: list) -> pd.DataFrame:
        """
        Executes the specified feature engineering methods in the given order.

        Parameters:
        - methods (list): A list of method names to execute.

        Returns:
        - pd.DataFrame: The updated DataFrame after executing the specified feature engineering methods.
        """
        for method in methods:
            self.df = getattr(self, method)()

        return self.df
