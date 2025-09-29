from aesgestion import AesGestion

aes_obj = AesGestion();

aes_obj.generate_aes_key();

aes_obj.save_aes_key_to_file("aes_keys.bin")

aes_obj.encrypt_file("test.txt", "test_crypting.txt");

