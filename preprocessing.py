import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, filepath):
        self.filepath = filepath

    def preprocess(self):
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(self.filepath)

        # Step 1: Handle missing data
        df = self.handle_missing_data(df)

        # Step 2: Standardize column names
        df.columns = self.standardize_columns(df.columns)

        # Step 3: Convert data types (including handling Timestamp conversion)
        df = self.convert_data_types(df)

        # Step 4: Perform basic data validation
        df = self.validate_data(df)

        # Step 5: Convert Timestamps to string (if still present)
        for column in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[column]):
                df[column] = df[column].apply(lambda x: x.strftime('%Y-%m-%d') if not pd.isnull(x) else None)

        # Return preprocessed data as a list of dictionaries
        return df.to_dict(orient='records')

    def handle_missing_data(self, df):
        # Example: Drop columns with more than 50% missing values
        df = df.dropna(axis=1, thresh=int(0.5 * len(df)))

        # Example: Fill remaining missing values with a placeholder
        df.fillna('N/A', inplace=True)

        return df

    def standardize_columns(self, columns):
        # Convert column names to lowercase and replace spaces with underscores
        standardized_columns = [col.lower().replace(' ', '_') for col in columns]
        return standardized_columns

    def convert_data_types(self, df):
        # Example: Convert date columns to datetime
        for col in df.columns:
            if 'date' in col:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Example: Convert numeric columns to appropriate types
        for col in df.select_dtypes(include=['object']).columns:
            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except ValueError:
                pass
        
        return df

    def validate_data(self, df):
        # Example: Ensure email columns contain valid email addresses
        if 'email' in df.columns:
            df['email_valid'] = df['email'].apply(lambda x: self.is_valid_email(x))
        
        # Add more validation rules as needed
        return df

    def is_valid_email(self, email):
        # Basic email validation logic (you can replace this with a more complex validation)
        return isinstance(email, str) and '@' in email and '.' in email

    # import re
    
    # def is_valid_email(email):
    #     # Basic regex for validating an email address
    #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     return re.match(pattern, email) is not None
