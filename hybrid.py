#partie 4,5 et un bout de la 3 du a des bugs realisé avec l'aide de l'ia pour me guider car je ne voyer pas comment faire.
from aesgestion import AesGestion
from rsagestion import RsaGestion

# 1) Génération des clés RSA (si elles n'existent pas déjà)
rsa_obj = RsaGestion();
rsa_obj.generation_clef("public.pem", "prive.pem", 2048);

# 2) Génération d'une clé AES côté client
aes_obj = AesGestion();
aes_obj.generate_aes_key();
aes_obj.save_aes_key_to_file("aes_keys.bin");

# 3) Chiffrement de la clé AES avec la clé publique RSA
rsa_obj.chargement_clef_publique("public.pem");
cle_aes_hex = aes_obj.aes_key.hex();
cle_aes_chiffree = rsa_obj.chiffrement_rsa(cle_aes_hex);
with open("aes_key_encrypted.txt", "w", encoding="utf-8") as f:
    f.write(cle_aes_chiffree);

# 4) Déchiffrement de la clé AES côté serveur
rsa_obj.chargement_clefs("public.pem", "prive.pem");
with open("aes_key_encrypted.txt", "r", encoding="utf-8") as f:
    cle_aes_hex_dechiffree = rsa_obj.dechiffrement_rsa(f.read());

# Création d'un objet AES serveur avec la clé déchiffrée
aes_server = AesGestion();
aes_server.aes_key = bytes.fromhex(cle_aes_hex_dechiffree);

# 5) Chiffrement d’un fichier test avec AES (côté client)
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Ceci est un message secret de test.");
aes_obj.encrypt_file("test.txt", "test_crypting.txt");

# 6) Déchiffrement du fichier chiffré (côté serveur)
aes_server.decrypt_file("test_crypting.txt", "test_decrypted.txt");

print("Chiffrement hybride terminé :")
print("- test.txt            => fichier original")
print("- test_crypting.txt   => fichier chiffré avec AES")
print("- test_decrypted.txt  => fichier déchiffré avec AES (clé AES transmise via RSA)")

