import hashlib
import os
def get_file_hash(filename):
    hasher = hashlib.sha1()
    #Opening the file 
    with open(filename, 'rb') as f:
        while True:
            data = f.read(8192) ## The file is being read here in chunks of 8192 bytes
            if not data:
                break
            hasher.update(data)  # SHA1 hash object is being updated with each chunk of data
    return hasher.hexdigest()
def merkle_tree(files):
    #Computation of the hash value of a Merkle hash tree for a list of files
    hashes = [get_file_hash(file) for file in files]
    while len(hashes) > 1:
        hashes = [hashlib.sha1(hashes[i].encode('utf-8') + hashes[i+1].encode('utf-8')).hexdigest() for i in range(0, len(hashes), 2)]
    return hashes[0]
# Example usage
files = ['L1.txt', 'L2.txt', 'L3.txt', 'L4.txt']
top_hash = merkle_tree(files)
print('Top hash:', top_hash)
# Once one of the files has been Modified we compute the top hash again
os.system('echo "Modified content" >> L1.txt')
new_top_hash = merkle_tree(files)
print('New top hash:', new_top_hash)