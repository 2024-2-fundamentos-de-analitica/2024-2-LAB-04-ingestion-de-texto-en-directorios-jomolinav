# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os 
import pandas as pd

rutatrain1 = "files/input/train/negative"
rutatrain2 = "files/input/train/neutral"
rutatrain3 = "files/input/train/positive"

lista1 = os.listdir(rutatrain1)
lista2 = os.listdir(rutatrain2)
lista3 = os.listdir(rutatrain3)

listf1frase = []
listf1moods = []



for a in lista1:
    dir = rutatrain1 + "/" + a
    with open(dir, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    listf1frase.append(texto)
    listf1moods.append("negative")


for a in lista2:
    dir = rutatrain2 + "/" + a
    with open(dir, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    listf1frase.append(texto)
    listf1moods.append("neutral")

for a in lista3:
    dir = rutatrain3 + "/" + a
    with open(dir, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    listf1frase.append(texto)
    listf1moods.append("positive")



data1 = {"phrase" : listf1frase, "target" : listf1moods}

dataf1 = pd.DataFrame(data1)

pathcsv1 = "files/output/train_dataset.csv"
dataf1.to_csv(pathcsv1, index=False)





#test_dataset.csv

rutatrain1 = "files/input/test/negative"
rutatrain2 = "files/input/test/neutral"
rutatrain3 = "files/input/test/positive"

lista1 = os.listdir(rutatrain1)
lista2 = os.listdir(rutatrain2)
lista3 = os.listdir(rutatrain3)

listf1frase = []
listf1moods = []



for a in lista1:
    dir = rutatrain1 + "/" + a
    with open(dir, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    listf1frase.append(texto)
    listf1moods.append("negative")


for a in lista2:
    dir = rutatrain2 + "/" + a
    with open(dir, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    listf1frase.append(texto)
    listf1moods.append("neutral")

for a in lista3:
    dir = rutatrain3 + "/" + a
    with open(dir, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    listf1frase.append(texto)
    listf1moods.append("positive")



data1 = {"phrase" : listf1frase, "target" : listf1moods}

dataf1 = pd.DataFrame(data1)

pathcsv1 = "files/output/test_dataset.csv"
dataf1.to_csv(pathcsv1, index=False)









def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
