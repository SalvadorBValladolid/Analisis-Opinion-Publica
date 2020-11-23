#!/bin/bash
## Configuración de mi instancia EC2 de Amazon
echo -n "Selecciona los renglones  "
read renglones;
echo $renglones;
export renglones;


sudo yum install git-all -y;
sudo yum install python-pip -y;
sudo pip install pandas;
#sudo pip install xlrd;
#sudo pip install boto3;
#sudo pip install xlsxwriter;
# AHora vamos a clonar un repositorio para instalar google trans
mkdir git;
cd git;
git clone https://github.com/BoseCorp/py-googletrans.git;
cd py-googletrans;
sudo python setup.py install;
# Ahora regresamos a home
cd;
cd git;
# Clonamos un repositorio donde tenemos la data de entrenamiento
git clone https://github.com/ParveshDhawan/Bag-of-Words-Meets-Bags-of-Popcorn;

# Now, we are going to clone another repository.
git clone https://github.com/SalvadorBValladolid/Analisis-Opinion-Publica;
cd Analisis-Opinion-Publica/Procesamiento_data;
python Translate_data.py;

csv=".csv"
nueva_data="../data/Data entrenamiento-$renglones$csv"

git add $nueva_data;
git commit $nueva_data -m "Agrego mas data";
git push;

"/home/ec2-user/Data entrenamiento-2400-2700.csv"






