from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "rb") as inp_file:
    encrypted_data = inp_file.read()
    passwords = [line.rstrip() for line in open("password.txt")]
    for password in passwords:
        try:
            result = decrypt(password, encrypted_data).decode('utf8')
        except DecryptionException:
            continue
        print(result)
