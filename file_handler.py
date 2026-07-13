import pandas as pd
import os

from config import FILE_NAME, COLUMNS


class FileHandler:

    def __init__(self):

        if not os.path.exists(FILE_NAME):

            df = pd.DataFrame(columns=COLUMNS)

            df.to_csv(FILE_NAME, index=False)

    def read_file(self):
        
        return pd.read_csv(FILE_NAME)

    def save_file(self, df):

        df.to_csv(FILE_NAME, index=False)