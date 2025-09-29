from rsagestion import RsaGestion

rsa_obj = RsaGestion()

rsa_obj.chargement_clef_privee("prive.pem")

rsa_obj.dechiffrement_fichier("test_chiffre.txt", "test_dechiffre.txt")

