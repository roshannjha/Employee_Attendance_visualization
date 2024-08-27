import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def visualize(self):
        numerical_cols = self.df.select_dtypes(include=['number']).columns
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        datetime_cols = self.df.select_dtypes(include=['datetime64']).columns

        self.visualize_numerical(numerical_cols)
        self.visualize_categorical(categorical_cols)
        self.visualize_datetime(datetime_cols)

    def visualize_numerical(self, columns):
        for col in columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df[col].dropna(), kde=True)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()

    def visualize_categorical(self, columns):
        for col in columns:
            plt.figure(figsize=(10, 6))
            sns.countplot(x=col, data=self.df)
            plt.title(f'Count of {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.show()

    def visualize_datetime(self, columns):
        for col in columns:
            plt.figure(figsize=(10, 6))
            self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
            sns.lineplot(x=self.df[col], y=self.df.index)
            plt.title(f'Time Series of {col}')
            plt.xlabel(col)
            plt.ylabel('Index')
            plt.show()
