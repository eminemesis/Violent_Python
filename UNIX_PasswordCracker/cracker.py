import crypt
from itertools import permutations
with open("dict.txt","r") as f:
    with open("hash.txt","r") as h:
         passes = f.read().split(" ")
         hsh = h.read()
passes[-1]=passes[-1].strip("\n")
hash_ref="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./"
hash_ref=[i for i in hash_ref]
hashes=permutations(hash_ref,2)
hashes=[str(i) for i in hashes]
hashes=["".join(j for j in i if j not in "(', )") for i in hashes]
def cracker(passes, hashes):
    print("cracking...")
    for i in passes:
        for j in hashes:
            hashed=crypt.crypt(i, j)
            if hashed==hsh:
                print("password found: "+str(i))
                return
cracker(passes, hashes)
