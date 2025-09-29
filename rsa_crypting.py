from rsagestion import RsaGestion

rsa_obj = RsaGestion()

rsa_obj.chargement_clef_publique("public.pem")

rsa_obj.chiffre_dans_fichier("test message rsa", "test_chiffre.txt")

