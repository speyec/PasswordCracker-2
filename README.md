# Code explanation and walk through

1. Import hashlib for encryption(hashing) and created a dictionary to hold user:password pairs
2. common_passwords is created and reads each line in common_passwords.txt and puts each line into the array list
3. text is created to read the "stolen" hashed passwords with the username that will be used to try and find the unhashed password
4. We split the username:hashed_password into userhash[0] and userhash[1] and put those pairs into user_hash_dict
5. The for loop loops through each unhashed password in the common_passwords.txt file and hashes each password and then compares the newly created hash to the stolen hashed passwords
6. If the newly hashed password matches a hashed password in user_hash_dict, we print that we found a match and as well as the username and the unhashed password