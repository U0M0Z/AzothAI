from urllib.request import urlopen
from urllib.parse import quote
from rdkit import Chem
import pandas as pd
import pubchempy as pcp

def canon_smiles(smi):
    return Chem.MolToSmiles(Chem.MolFromSmiles(smi), isomericSmiles=True, canonical=True)

def verify_smiles(smile):
    return (smile != '') and pd.notnull(smile) and (Chem.MolFromSmiles(smile) is not None)

def good_smiles(smile):
    if verify_smiles(smile):
        return canon_smiles(smile)
    else:
        return None

def text2smiles(name):

    c = pcp.get_compounds(name, 'name')

    for compound in c:
        smi = compound.canonical_smiles
        smi = good_smiles(smi)
    
    return smi
