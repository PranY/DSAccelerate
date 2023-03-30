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
