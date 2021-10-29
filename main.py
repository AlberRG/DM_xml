from lxml import etree


def leerXml():
    doc = etree.parse('restaurantes_v1_es.xml')
    raiz = doc.getroot()
    for i in raiz:
        for x in i:
            if x.find("name") is not None:
                print(x.find("name").text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    leerXml()
