import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta
import utils

def generar_csv():
    try:
        events = utils.get_events()
        con_city = events.loc[events.city != 'Unknown']
        agrupadas = con_city.groupby(['person']).city.value_counts()
        unstacked = agrupadas.unstack(fill_value=0)
        feature_city = unstacked.idxmax(axis=1)
        person_con_location = feature_city.count()
        person_totales = events.person.nunique()
        print("Hay {} de {} personas con location asignado".format(person_con_location,person_totales))
        events.city = events.person.map(feature_city)
        conversion = events.loc[events.event == 'conversion']
        conversions_per_city = conversion.groupby(['city']).agg({'person':'nunique'})
        unique_person_per_city = events.groupby(['city']).agg({'person':'nunique'})
        unique_person_per_city['conversion'] = unique_person_per_city.index.map(conversions_per_city.person).fillna(value=0).astype(int)
        unique_person_per_city['relacion'] = unique_person_per_city.conversion / unique_person_per_city.person
        features_location = pd.DataFrame(feature_city.copy())
        features_location.columns=['city']
        features_location['city_ranking'] = features_location.city.map(unique_person_per_city.relacion)
        features_location.to_csv('features_location.csv')
        return True
    except Exception, ex:
        print(ex)
        return False
    