import pandas as pd

def get_events():
    """Carga el csv en un dataframe, asigna los tipos básicos y lo devuelve"""
    events = pd.read_csv("events_up_to_01062018.csv", low_memory=False, dtype={'sku' : 'object'})
    events['timestamp'] = pd.to_datetime(events['timestamp'], errors = 'coerce', format= '%Y-%m-%d')
    events['event'] = pd.Categorical(events['event'])
    events['url'] = pd.Categorical(events['url'])
    events['model'] = pd.Categorical(events['model'])
    events['condition'] = pd.Categorical(events['condition'])
    events['storage'] = pd.Categorical(events['storage'])
    events['color'] = pd.Categorical(events['color'])
    events['staticpage'] = pd.Categorical(events['staticpage'])
    events['campaign_source'] = pd.Categorical(events['campaign_source'])
    events['search_engine'] = pd.Categorical(events['search_engine'])
    events['channel'] = pd.Categorical(events['channel'])
    events['new_vs_returning'] = pd.Categorical(events['new_vs_returning'])
    events['city'] = pd.Categorical(events['city'])
    events['region'] = pd.Categorical(events['region'])
    events['country'] = pd.Categorical(events['country'])
    events['device_type'] = pd.Categorical(events['device_type'])
    events['screen_resolution'] = pd.Categorical(events['screen_resolution'])
    events['operating_system_version'] = pd.Categorical(events['operating_system_version'])
    events['browser_version'] = pd.Categorical(events['browser_version'])
    events['month'] = events['timestamp'].dt.month
    events['day'] = events['timestamp'].dt.day
    events['hora'] = events['timestamp'].dt.hour
    events['sku'] = events['sku'].fillna(0)
    events['sku'] = events['sku'].map(lambda x: float(x))
    return events

def get_features_iniciales(events,pivot):
    """Recibe todos los eventos y devuelve un dataframe con los features iniciales"""
    features_iniciales = events.pivot_table(index='person', columns=pivot, values='timestamp', aggfunc='count', fill_value=0)
    features_iniciales.columns = features_iniciales.columns.astype('object')
    features_iniciales.reset_index(inplace=True)
    return features_iniciales

def add_features(events, features, on= 'person', how = 'left'):
    """Hace un merge de features a events"""
    return pd.merge(events, features, on=on, how = how)

def merge_features(events, list):
    feature_final = events
    for features in list:
        feature_final = add_features(feature_final,features)
    return feature_final