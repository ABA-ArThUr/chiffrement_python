from rsagestion import RsaGestion

rsa_obj = RsaGestion()

rsa_obj.generation_clef("public.pem", "prive.pem", 2048)

rsa_obj.chargement_clefs("public.pem", "prive.pem")

message = "test"

encrypted = rsa_obj.chiffrement_rsa(message)
print(f"Message chiffre : {encrypted}")

decrypted = rsa_obj.dechiffrement_rsa(encrypted)
print(f"Message dechiffre : {decrypted}")
