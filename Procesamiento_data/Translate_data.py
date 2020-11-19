#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Leemos el dataset
import pandas as pd
import csv
from deep_translator import GoogleTranslator
import re
Data_entrenamiento=pd.read_csv("/home/ec2-user/git/Bag-of-Words-Meets-Bags-of-Popcorn/Input/labeledTrainData.tsv",sep="\t")
### Vamos a filtrar, para seleccionar solo una parte del dataset:
renglones=str(input("Seleccina los renglones a traducir:"))
n=int(re.split("-",renglones)[0])
u=int(re.split("-",renglones)[1])
## Filtramos el dataset
Data_entrenamiento=Data_entrenamiento.iloc[n:u,]
translator=Translator()
# Comenzamos a tarducir a español
reviews=list()
for i in Data_entrenamiento["review"].values:
    #translator=Translator()
    reviews.append(GoogleTranslator(source="en",target="es").translate(i))
    
Data_entrenamiento["review_español"]=reviews
# Lo guardamos como csv
Data_entrenamiento.to_csv("Data entrenamiento-"+renglones+".csv",sep=",",quotechar='"',index=False,
            quoting=csv.QUOTE_ALL)
