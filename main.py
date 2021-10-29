from lxml import etree

def parsearXML(xmlName, csvName):
    doc = etree.parse(xmlName)
    raiz = doc.getroot()
    for i in raiz:
        for x in i:
            if x.find("name") is not None:
                print(x.find("name").text)
def leerXml():
    print("Trabajando Restaurantes")
    parsearXML('restaurantes_v1_es.xml', 'csv_restaurantes')
    print("Trabajando Alojamientos")
    parsearXML('alojamientos_v1_es.xml', 'csv_alojamientos')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    leerXml()
