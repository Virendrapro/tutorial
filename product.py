val = input("Plz Enter String to be Substituted: ").lower()
key = input("Plz Enter Key: ").lower()

array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Code for substitution Cipher
def substitution(val,key,array):
    substitutionCipher = []

    key = int(key)
    def substitutionusingkey(key):
        iia = array.index(i)
        iia1 = (iia + key) % 26
        return iia1

    for i in val:
        if i==" ":
            print(" ",end="")
        else:
            substitutionCipher.append(array[substitutionusingkey(key)])
    
    joint = ''.join(substitutionCipher)

    return joint

val = substitution(val,key,array)

def keycons(key):
    matrix = []
    matrixkey = []
    key = int(key)
    for i in str(key):
        matrixkey.append(int(i))
    
    matrix.append(matrixkey)
    return matrixkey,matrix

def matval(matrix,val,keylen):
    matrixval = []
    i = 0
    a = keylen
    for z in range(0,vallen,keylen):
        for j in val[i:keylen]:
            matrixval.append(j)
        i = keylen
        keylen += a
        matrix.append(matrixval)
        matrixval = [] 

def matrixprinter(matrix):
    for i in matrix:
        print(i)
def newkeycons(matrix):
    newkey = (matrix[0])
    newkey = sorted(newkey)
    return newkey
def printinrow(no,matrix):
    row = []
    for i in range(len(matrix)):
        for j in matrix[i]:
            index = matrix[i].index(j)
            if index == no:
                row.append(j)
    return row
def columnteller(key,newkey):
    cipherText = []
    for i in newkey:
        index = key.index(i)
        rows = printinrow(index,matrix)
        cipherText.append(rows)
        rows = []
    return cipherText
def cipher(cipherText,keylen):
    print("Transposition Cipher text is :",end="")
    cip = ''
    for i in range(keylen):
        for j in cipherText[i]:
            cip = cip + j
    print(cip)

if __name__ == '__main__':
    vallen = len(val)
    keylen = len(key)
    key,matrix = keycons(key)
    matval(matrix,val,keylen)
    matrixprinter(matrix)
    newkey = newkeycons(matrix)
    matrix.pop(0)
    cipherText = columnteller(key,newkey)
    cipher(cipherText,keylen)
