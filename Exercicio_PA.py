import pandas as pd

dfnull = pd.read_csv(r"C:\Users\deadp\Downloads\funcionarios - Null.csv")

# print(dfnull)
# print("\n")

#Filtro1__________________________________________________________
# departamento_preenchidos = dfnull.fillna({"departamento":"terceirizado"})

# print("\n")
# print(departamento_preenchidos)

#filtro2______________________________________

lucro_removido = dfnull.dropna(subset=["lucro"])

print(lucro_removido)