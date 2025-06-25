# More complicated password cracker

import hashlib
user_hash_dict = {}

with open('common_passwords.txt', 'r') as f:
    # common_passwords.append(f.read().splitlines())
    common_passwords = f.read().splitlines()

with open('username_hashes.txt', 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash_password = user_hash.split(":")[1]
        user_hash_dict[username] = hash_password

# for user, hashed_password in user_hash_dict.items():
#     print(user, hash_password)

for password in common_passwords:
    hashing_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for user, hash in user_hash_dict.items():
        if hashing_password == hash:
            print(f"HASH FOUND\n{username} : {password}\n")

