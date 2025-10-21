import asyncio
import sys
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

notebooks = [
    "00_Data_Discovery.ipynb",
    "01_Data_Cleaning.ipynb",
    "02_Exploratory_Analysis.ipynb",
    "03_Forecasting.ipynb",
    "04_Optimization.ipynb"
]

for nb_file in notebooks:
    print(f"\n=== Exécution de {nb_file} ===")
    try:
        with open(nb_file, encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb, {'metadata': {'path': './'}})

        # ✅ On écrase le fichier existant au lieu d'en créer un nouveau
        with open(nb_file, 'w', encoding="utf-8") as f:
            nbformat.write(nb, f)

        print(f"✅ Terminé et enregistré dans {nb_file}")

    except Exception as e:
        print(f"❌ Erreur pendant l'exécution de {nb_file} : {e}")
        break
