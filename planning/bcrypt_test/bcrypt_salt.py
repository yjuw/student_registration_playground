import bcrypt

password = b'hithere'
#this is random and can't be used in the database
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
print(salt)
print(hashed)

