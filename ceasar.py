array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

val = input("Plz Enter String to be Ciphercated: ")

val = val.lower()

def normaltocipher():
    iia = array.index(i)
    iia1 = (iia + 3) % 26
    return iia1

for i in val:
    if i==" ":
        print(" ",end="")
    else:
        print(array[normaltocipher()],end="")
