import pandas as pd
import pkg_resources

def get_dataset():
    dataset_path = pkg_resources.resource_filename(__name__, 'data/danteshots.csv')
    df = pd.read_csv(dataset_path, encoding='utf-8')
    return df
