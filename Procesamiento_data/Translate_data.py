# Leemos el dataset
import pandas as pd
import csv
from googletrans import Translator
Data_entrenamiento=pd.read_csv("labeledTrainData.tsv",sep="\t")
translator=Translator()

# Comenzamos a tarducir a español
reviews=list()
for i in Data_entrenamiento["review"].values:
    reviews.append(translator.translate(i,dest="es").text)
    
Data_entrenamiento["review_español"]=reviews
# Lo guardamos como csv
Data_entrenamiento.to_csv("Data entrenamiento.csv",sep=",",quotechar='"',index=False,
            quoting=csv.QUOTE_ALL)
