# Librerías necesarias para realizar este programa
import pandas as pd
import csv
from deep_translator import GoogleTranslator
Data_entrenamiento=pd.read_csv("labeledTrainData.tsv",sep="\t")
# Comenzamos a tarducir a español
reviews=list()
for index, row in Data_entrenamiento.iterrows():
    try:
      translated = GoogleTranslator(source='auto', target='es').translate(row['review']);
    except Exception as e:
        print(str(e))
        continue
    reviews.append(translated)
Data_entrenamiento["review_español"]=reviews
# Lo guardamos como csv
Data_entrenamiento.to_csv("Data entrenamiento.csv",sep=",",quotechar='"',index=False,
            quoting=csv.QUOTE_ALL)