from cryptography.fernet import Fernet

# 1. Generate & save a new key
key=Fernet.generate_key()
with open('mykey.key','wb') as mykey:
    mykey.write(key)

# 2. Load & print that same key
with open('mykey.key','rb') as mykey:
    key=mykey.read()
print(key)

# 3. Encrypt grades.csv → encrypted_grades.csv
f=Fernet(key)
with open('grades.csv','rb') as original_file:
    original = original_file.read()
encrypted = f.encrypt(original)
with open('encrypted_grades.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# 4. Decrypt encrypted_grades.csv → decrypted_grades.csv
f=Fernet(key)
with open('encrypted_grades.csv','rb') as encrypted_file:
    encrypted = encrypted_file.read()
decrypted = f.decrypt(encrypted)
with open('decrypted_grades.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)