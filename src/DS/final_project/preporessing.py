import pandas as pd

def check_types(data):
    n_uniq = data.nunique()
    return pd.DataFrame({'dtypes' :data.dtypes , 'num_uniq' : n_uniq}).T


def check_null(data):
    null = data.isnull().sum()
    ratio = (null / data.shape[0])*100
    return pd.DataFrame({"Null_sum": null, "Ratio %": ratio}).T

def av_age(age):
    return round(age.mean(), 2)

def hours_to_minutes(seconds):
    seconds['duration_sec'] = seconds['duration_sec'] * 60
    return round(seconds , 2)


