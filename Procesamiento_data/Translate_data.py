#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Leemos el dataset
import pandas as pd
import csv
from googletrans import Translator
import re
import os
Data_entrenamiento=pd.read_csv("/home/ec2-user/git/Bag-of-Words-Meets-Bags-of-Popcorn/Input/labeledTrainData.tsv",sep="\t")
### Vamos a filtrar, para seleccionar solo una parte del dataset:
renglones=os.getenv('renglones')
n=int(re.split("-",renglones)[0])
u=int(re.split("-",renglones)[1])
## Filtramos el dataset
Data_entrenamiento=Data_entrenamiento.iloc[n:u,]
translator=Translator()
# Comenzamos a tarducir a español
reviews=list()
for i in Data_entrenamiento["review"].values:
    #translator=Translator()
    reviews.append(translator.translate(i,dest="es").text)
    
Data_entrenamiento["review_español"]=reviews
# Lo guardamos como csv
Data_entrenamiento.to_csv("/home/ec2-user/git/Analisis-Opinion-Publica/data/Data entrenamiento-"+renglones+".csv",sep=",",quotechar='"',index=False,
            quoting=csv.QUOTE_ALL,encoding="utf-8")
