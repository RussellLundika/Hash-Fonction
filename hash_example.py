import hashlib

def hash_function(data):
    # Utilisation de l'algorithme de hachage SHA-256
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

# Exemple d'utilisation
data = "Hello, World!"
hashed_result = hash_function(data)
print(hashed_result
