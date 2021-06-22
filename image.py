def get_img(selenium_driver):
    img = selenium_driver.find_element_by_xpath('/html/body/div[22]/div/div/div[2]/div/div/form[2]/div/span/div[2]/p[1]/img')
    filename = "filename.png"
    with open(filename, 'wb') as file:
        file.write(img.screenshot_as_png)


def is_equal(picture):
    from PIL import Image
    import os

    def getGray(image_file):
        tmpls = []
        for h in range(0, image_file.size[1]):  # h
            for w in range(0, image_file.size[0]):  # w
                tmpls.append(image_file.getpixel((w, h)))

        return tmpls

    # Ermitteln Sie den durchschnittlichen Grauwert
    def getAvg(ls):
        return sum(ls) / len(ls)

        # Vergleichen Sie 100 Zeichen und wie viele Zeichen gleich sind

    def getMH(a, b):
        dist = 0
        for i in range(0, len(a)):
            if a[i] == b[i]:
                dist = dist + 1
        return dist

    def getImgHash(fne):
        image_file = Image.open(fne)  # open
        image_file = image_file.resize((20, 20))  # Setzen Sie die Bildgröße auf 12 x 12 Pixel zurück
        image_file = image_file.convert("L")  # auf 256 Graustufen umschalten
        Grayls = getGray(image_file)  # Graue Sammlung
        avg = getAvg(Grayls)  # Grauer Durchschnitt
        bitls = ''  # Empfangen, um 0 oder 1 zu erhalten
        # Entfernen Sie die variable Breite 1px und durchlaufen Sie die Pixel

        for h in range(1, image_file.size[1] - 1):  # h
            for w in range(1, image_file.size[0] - 1):  # w
                if image_file.getpixel((w, h)) >= avg:  # Der Durchschnittswert des Pixelwerts ist größer als 1 und kleiner als 0
                    bitls = bitls + '1'
                else:
                    bitls = bitls + '0'
        return bitls

    data = {}
    # Bildadresse selbst ersetzen
    bijiaotupian = picture
    openfile = ".//Beispiele"
    a = getImgHash(bijiaotupian)
    # Bilder im geöffneten Ordner
    files = os.listdir(openfile)  # Ersetzen Sie die Adresse des Bildordners selbst
    for file in files:
        b = getImgHash(".//Beispiele//" + str(file))
        compare = getMH(a, b)
        data[file[:len(file) - 4]] = compare
    for file in data:
        if data[file] > 315:
            return file
        else:
            pass
