from aesgestion import AesGestion

aes_obj = AesGestion();

aes_obj.generate_aes_key();

aes_obj.save_aes_key_to_file("aes_keys.bin")

aes_obj.encrypt_file("test.txt", "test_crypting.txt");

aes_obj.load_aes_key_from_file("aes_key.bin");

aes_obj.decrypt_file("message_chiffre.txt", "message_dechiffre.txt");
