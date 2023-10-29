import pandas as pd
from enum import Enum
from ..models import Bar

class BarField(Enum):
    NOMBREBAR = 0
    DIRECCION = 1
    NUMEROCALLE = 2
    CIUDAD = 4
    TIPOBAR = 7

def initList(path="../static/data/llistat.xlsx",header=None):
    df = pd.read_excel(path,header=header)
    df.head()
    df.fillna("",inplace=True)
    for i in range(0,len(df)):
        nombre = df.iloc[i,BarField.NOMBREBAR.value]
        direccion = df.iloc[i,BarField.DIRECCION.value]
        numerocalle = df.iloc[i,BarField.NUMEROCALLE.value]
        ciudad = df.iloc[i,BarField.CIUDAD.value]
        tipoBar = df.iloc[i,BarField.TIPOBAR.value]
        Bar.objects.create(nombre=nombre,direccion=direccion,numeroCalle=numerocalle,ciudad=ciudad,tipoBar=tipoBar)

