from xml.dom import minidom
import pandas as pd

with open ('./Agenda24072015.xml') as f:
    xml_file = minidom.parse(f)

print('xml_file:', xml_file)

organismes = xml_file.getElementsByTagName('organisme')

print('organismes:', type(organismes))

columns = ["idMemo", "libelle", "typeOrganisme", "adresseVoieNumero",
           "adresseVoieTypeVoie",  "adresseVoieNomVoie", "adresseAcheminPostalLibelleCedex",
           "adresseCodePostal", "adresseCommune", "region", "moyenAcces"]
tot = pd.DataFrame(columns=columns)
for i, organisme in enumerate(organismes):
    print(organisme.getElementsByTagName('idMemo')[0].firstChild.nodeValue)

    inter = pd.DataFrame(columns=columns)

     #print('{}:{}'.format(i, organisme))
    #if i == 0:
    #print(organisme.toprettyxml())
    #inter["idMemo"] = organisme.getElementsByTagName('idMemo')[0].firstChild.nodeValue
    #print(idMemo.nodeType)
    #print(idMemo.nodeValue)

    #libelle, typeOrganisme, adresseVoieNumero adresseVoieTypeVoie  adresseVoieNomVoie
    #adresseAcheminPostalLibelleCedex adresseCodePostal adresseCommune region moyenAcces

    #print(organisme.getElementsByTagName('adresseVoieNumero'))
    #print(organisme.getElementsByTagName('adresseVoieNumero')[0])
    #print(organisme.getElementsByTagName('adresseVoieNumero')[0].firstChild)


    # inter_dict = {
    #     "idMemo": [organisme.getElementsByTagName('idMemo')[0].firstChild.nodeValue if organisme.getElementsByTagName('idMemo') else 'NaN'],
    #     "libelle": [organisme.getElementsByTagName('libelle')[0].firstChild.nodeValue if organisme.getElementsByTagName('libelle') else 'NaN'],
    #     "typeOrganisme": [organisme.getElementsByTagName('typeOrganisme')[0].firstChild.nodeValue if organisme.getElementsByTagName('typeOrganisme') else 'NaN'],
    #     "adresseVoieNumero": [organisme.getElementsByTagName('adresseVoieNumero')[0].firstChild.nodeValue if organisme.getElementsByTagName('adresseVoieNumero') is not None else 'NaN'],
    #     "adresseVoieTypeVoie": [organisme.getElementsByTagName('adresseVoieTypeVoie')[0].firstChild.nodeValue if organisme.getElementsByTagName('adresseVoieTypeVoie') else 'NaN'],
    #     "adresseVoieNomVoie": [organisme.getElementsByTagName('adresseVoieNomVoie')[0].firstChild.nodeValue if organisme.getElementsByTagName('adresseVoieNomVoie') else 'NaN'],
    #     "adresseAcheminPostalLibelleCedex": [organisme.getElementsByTagName('adresseAcheminPostalLibelleCedex')[0].firstChild.nodeValue if organisme.getElementsByTagName('adresseAcheminPostalLibelleCedex') else 'NaN'],
    #     "adresseCodePostal": [organisme.getElementsByTagName('adresseCodePostal')[0].firstChild.nodeValue if organisme.getElementsByTagName('adresseCodePostal') else 'NaN'],
    #     "adresseCommune": [organisme.getElementsByTagName('adresseCommune')[0].firstChild.nodeValue if organisme.getElementsByTagName('adresseCommune') else 'NaN'],
    #     "region": [organisme.getElementsByTagName('region')[0].firstChild.nodeValue if organisme.getElementsByTagName('region') else 'NaN'],
    #     "moyenAcces": [organisme.getElementsByTagName('moyenAcces')[0].firstChild.nodeValue if organisme.getElementsByTagName('moyenAcces') else 'NaN']
    #
    # }

    inter_dict = {}
    for variable in columns:
        print(variable)
        print(organisme.getElementsByTagName(variable) > 0)
        if len(organisme.getElementsByTagName(variable)) > 0:
            inter_dict[variable] = [organisme.getElementsByTagName(variable)[0].firstChild.nodeValue]
        else:
            inter_dict[variable] = ['NaN']

        #print("inter_dict:", inter_dict)

    inter = pd.DataFrame.from_dict(inter_dict)
    print(' ')

    tot = tot.append(inter, ignore_index=True)
print('tot:', tot)


