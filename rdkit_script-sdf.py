from rdkit import Chem
from rdkit.Chem import Crippen
import os
import pandas as pd

input_dir = 'input'
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

data=[]
for file in os.listdir(input_dir):
    if os.stat(os.path.join(input_dir,file)).st_size > 0:
        suppl = Chem.SDMolSupplier(os.path.join(input_dir, file))

        for mol in suppl:
            if mol is not None:
                name = mol.GetProp("_Name") if mol.HasProp("_Name") else "unknown"
                smiles = Chem.MolToSmiles(mol)
                logp = Crippen.MolLogP(mol)
                data.append({"name": file, "logP": logp})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv(os.path.join(output_dir, "logp_results.csv"), index=False)

print("LogP calculation complete. Results saved to output/logp_results.csv")
        
