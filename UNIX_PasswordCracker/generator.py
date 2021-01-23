import crypt
print("salt needs to be two values. valid entries are [Alphanumerics, '.', '/']")
with open("hash.txt","w+") as f:
	f.write(str(crypt.crypt(str(raw_input("password")), str(raw_input("salt")))))
