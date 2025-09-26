from hashgestion import HashGestion

if __name__ == "__main__":
    
    hash_gestion = HashGestion()

    message = "test"

    hash_message = hash_gestion.calculate_sha256(message)

    if hash_message:
        print(f"Le hash SHA-256 du message '{message}' est :\n{hash_message}")

