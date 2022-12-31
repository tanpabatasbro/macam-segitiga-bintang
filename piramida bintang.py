a = int(input("masukkan tinggi piramida : "))
for i in range(1,a+1):
    print(((a-i+1)*" ") + (i*"*") + ((i-1)*"*"))