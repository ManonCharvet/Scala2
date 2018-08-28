from xml.etree.ElementTree import iterparse
import json
import pandas as pd

columns = ["idMemo", "libelle", "adresseVoieNumero", "pays"]
final = pd.DataFrame()
with open ('./Agenda24072015.xml', 'r') as f:
    xml_file = iterparse(f, events=['start', 'end'])
    dt = {}
    for event, elem in xml_file:
        print(event)
        print(elem.tag)
        print(elem.text)
        if (event == 'end') and (elem.tag in columns):
            dt[elem.tag] = [elem.text]
        elif (event == 'end') and (elem.tag == 'organisme'):
            #with open('./test.csv', 'a') as w:
                #w.write(json.dumps(dt) + '\n')
                #inter = pd.DataFrame.from_dict(dt)
                final = final.append(pd.DataFrame.from_dict(dt), ignore_index=True)
                dt = {}

final.to_csv('./test2.csv')

        #print(' ')