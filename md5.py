import hashlib

# Function to calculate MD5 hash
def calculate_md5(message):
    md5_hash = hashlib.md5(message.encode('utf-8'))
    return md5_hash.hexdigest()

# Sample message
original_message = input("Enter Text: ")

# Calculate the MD5 hash of the original message
md5_digest = calculate_md5(original_message)

print("Original Message: ", original_message)
print("MD5 Digest: ",md5_digest)
