import json

def to_json(input_string):
    fields = input_string.split(', ')
    data_dict = {}

    for field in fields:
        #champ est au format 'clé: valeur'
        key, value = field.split(': ')
        #Nettoyage des espaces et des éventuels caractères spéciaux autour des clés et des valeurs
        key = key.strip('{} ')
        value = value.strip('{} ')
        data_dict[key] = value

    json_data = json.dumps(data_dict)

    return json_data