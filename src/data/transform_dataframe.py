import pandas as pd
import numpy as np

def transform_data(dataframe):
    dataframe["NPS interno"] = dataframe["NPS interno"].str.replace(",", ".").astype("float")
    dataframe["Setor"] = dataframe["Setor"].replace({"Engenheiro de Software": "Engenharia de Software"})
    return dataframe