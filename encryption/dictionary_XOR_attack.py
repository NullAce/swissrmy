from sys import argv

cipher_text = argv[1]
cipher_bytes = bytes.fromhex(cipher_text)

with open(f"{argv[2]}", "r") as file:
    for line in file:
        key = line.strip().encode()
        decrypted = bytearray()

        for i in range(len(cipher_bytes)):
            decrypted.append(cipher_bytes[i] ^ key[i % len(key)])

        if all(32 <= byte <= 126 for byte in decrypted):
            print("Trying: " + line)
            print("Decrypted: ", decrypted.decode())