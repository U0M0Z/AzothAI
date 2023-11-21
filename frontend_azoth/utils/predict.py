import requests
import json

def predict_azothapp(server_url: str, list_of_smiles: list):

    header = {'Content-Type': 'application/json'}
    dict_of_smiles = {"inputs" : []}

    for smi in list_of_smiles:
        smi_dict = {"SMILES" : smi}
        dict_of_smiles["inputs"].append(smi_dict)

    smi_dict_json=json.dumps(dict_of_smiles)

    response = requests.post(
        server_url, data=smi_dict_json, headers = header, timeout=8000
    )

    return json.loads(response.text)