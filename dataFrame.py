import pandas as pd
from pymongo import MongoClient

# Criar DataFrames
car_data = {
    'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
    'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
}

montadora_data = {
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão']
}

car_df = pd.DataFrame(car_data)
montadora_df = pd.DataFrame(montadora_data)

client = MongoClient('Coloque_aqui_sua_url_de_conexão_para_o_bando_de_dados')
db = client['Nome_do_banco'] 

car_json = car_df.to_dict(orient='records')
montadora_json = montadora_df.to_dict(orient='records')

db.Carros.insert_many(car_json)
db.Montadoras.insert_many(montadora_json)

pipeline = [
    {
        '$lookup': {
            'from': 'Montadoras',
            'localField': 'Montadora',
            'foreignField': 'Montadora',
            'as': 'MontadoraInfo'
        }
    },
    {
        '$unwind': '$MontadoraInfo'
    },
    {
        '$group': {
            '_id': '$MontadoraInfo.País',
            'Carros': {
                '$push': {
                    'Carro': '$Carro',
                    'cor': '$cor'
                }
            }
        }
    }
]

result = list(db.Carros.aggregate(pipeline))

client.close()

print("DataFrames salvos no MongoDB")