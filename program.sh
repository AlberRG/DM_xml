echo Obtenemos archivos
wget -N https://www.esmadrid.com/opendata/turismo_v1_es.xml

wget -N https://datos.madrid.es/egob/catalogo/206577-0-oficinas-turismo.csv

wget -N https://www.esmadrid.com/opendata/agenda_v1_es.xml

wget -N https://www.esmadrid.com/opendata/alojamientos_v1_es.xml

wget -N https://www.esmadrid.com/opendata/restaurantes_v1_es.xml


pip install lxml

echo Creamos archivo CSV con los datos
python3 data_creator.py

pip install tweepy

python3 twitter.py
