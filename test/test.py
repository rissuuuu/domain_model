import pickle

with open('../database.pickle', 'rb') as handle:
    database = pickle.load(handle)
print(database)