import csv

from lxml import etree


def crearCsv(name):
    with open(name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['ID', 'Name', 'Latitude', 'Longitude', 'Phone', 'Email', 'Address', 'Web'])


def escribirCsv(valores, name):
    with open(name, 'a', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(valores)


def parsearXML(xmlName, csvName):
    latitude = ""
    longitude = ""
    phone = ""
    email = ""
    address = ""
    name = ""
    web = ""

    crearCsv(csvName)
    doc = etree.parse(xmlName)
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

        valores = [iden, name, latitude, longitude, phone, email, address, web]
        escribirCsv(valores, csvName)


def leerXml():
    print("Trabajando Restaurantes")
    parsearXML('restaurantes_v1_es.xml', 'restaurantes.csv')
    print("Trabajando Alojamientos")
    parsearXML('alojamientos_v1_es.xml', 'alojamientos.csv')


if __name__ == '__main__':
    leerXml()
