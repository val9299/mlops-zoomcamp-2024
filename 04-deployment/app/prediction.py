import pickle
import pandas as pd

CATEGORICAL = ['PULocationID', 'DOLocationID']

def read_data(filepath):
    df = pd.read_parquet(filepath)
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[CATEGORICAL] = df[CATEGORICAL].fillna(-1).astype('int').astype('str')
    return df

def run_prediction(month, year):

    filepath = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_' + year + '-' + month + '.parquet'
    
    with open('app/model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)

    df = read_data(filepath)

    dicts = df[CATEGORICAL].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    # prediction mean and standard deviation
    pred_mean = float(y_pred.mean())
    pred_std = float(y_pred.std())

    # save predictions to output file
    df['ride_id'] = year + '/' + month + '_' + df.index.astype('str')
    df_output = df[['ride_id', 'duration']]
    output_filepath = 'app/output/' + 'yellow_trip_duration_pred_' + year + '-' + month + '.parquet'
    df_output.to_parquet(output_filepath, engine='pyarrow', compression=None,index=False)

    return pred_mean, pred_std

