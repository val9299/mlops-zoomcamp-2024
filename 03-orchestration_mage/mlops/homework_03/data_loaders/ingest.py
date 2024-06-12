import requests
from io import BytesIO
from typing import List

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:
    dfs: List[pd.DataFrame] = []

    parquet_file_url = 'https://github.com/val9299/mlops-zoomcamp-2024/blob/main/03-orchestration_mage/data/yellow_tripdata_2023-03.parquet'
    response = requests.get(parquet_file_url)

    if response.status_code != 200:
        raise Exception(response.text)

    df = pd.read_parquet(parquet_file_url)
    dfs.append(df)

    return pd.concat(dfs)