import csv

from lxml import etree


def crear_csv(name):
    with open(name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['ID', 'Name', 'Latitude', 'Longitude', 'Phone', 'Email', 'Address', 'Web', 'Categoria'])


def escribir_csv(valores, name):
    with open(name, 'a', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(valores)


def parsear_xml(xml_name, csv_name, category):
    latitude = ""
    longitude = ""
    phone = ""
    email = ""
    address = ""
    name = ""
    web = ""

    doc = etree.parse(xml_name)
    raiz = doc.getroot()
    for i in raiz:
        iden = i.get("id")
        for x in i:
            if x.find("name") is not None:
                name = x.find("name").text
            if x.find("latitude") is not None:
                latitude = x.find("latitude").text
            if x.find("longitude") is not None:
                longitude = x.find("longitude").text
            if x.find("phone") is not None:
                phone = x.find("phone").text
            if x.find("email") is not None:
                email = x.find("email").text
            if x.find("address") is not None:
                address = x.find("address").text
            if x.find("web") is not None:
                web = x.find("web").text

        valores = [iden, name, latitude, longitude, phone, email, address, web, category]
        escribir_csv(valores, csv_name)


def leer_csv():
    with open('206577-0-oficinas-turismo.csv', encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cont = 0
        for row in reader:
            if cont != 0 and len(row) > 28:
                valores = [row[0], row[1], row[24], row[25], row[26], row[28], row[21], row[8], 'oficinas-turismo']
                escribir_csv(valores, 'datos.csv')
            cont += 1


def leer_xml():
    name = 'datos.csv'
    crear_csv(name)
    print("Trabajando Restaurantes")
    parsear_xml('restaurantes_v1_es.xml', name, 'restaurantes')
    print("Trabajando Alojamientos")
    parsear_xml('alojamientos_v1_es.xml', name, 'alojamientos')
    print("Trabajando en Agenda")
    parsear_xml('agenda_v1_es.xml', name, 'agenda')
    print("Trabajando en turismo")
    parsear_xml('turismo_v1_es.xml', name, 'turismo')
    print("Trabajando en oficina de turismo")
    leer_csv()


if __name__ == '__main__':
    leer_xml()