import pickle

with open('artifacts/preprocessor.pkl', 'rb') as file:
    preprocessor = pickle.load(file)

print(preprocessor)
