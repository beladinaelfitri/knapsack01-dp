
# coding: utf-8


# Knapsack with Dynamic Programming - Kelompok 2

# Angela Marpaung
# Shindy Trimaria Laxmi
# Beladina Elfitri
# Kartiko Nurhada Wicaksono



def knapsack(c, d, p, n):
    n = n + 1
    c = c + 1
    v = [[0 for x in range(c)] for y in range(n)] #inisialisasi array dengan 0
    
    # mencari solusi optimal
    for i in range(1,n):
        for j in range(1,c):
            if (i == 0 or j == 0):
                v[i][j] = 0
            elif (j < d[i-1]):
                v[i][j] = v[i-1][j]
            else:
                v[i][j] = max(v[i-1][j],v[i-1][j-d[i-1]]+p[i-1])
    
    #print table
    print()
    print('Table :')
    for row in v:
        print('    '.join([str(elem) for elem in row]))
      
    #mencari item yang akan dimasukkan ke dalam knapsack
    take = [] #array untuk menampung berat yang diambil
    while (i != 0):
        if (v[i][j] != v[i-1][j]):
            take.append(i)
            j = j - d[i-1]
            i = i - 1
        else:
            i = i -1
    print('Barang yang diambil : ', take)
    idx = [0 for x in range(n-1)] #array untuk menampilkan knapsack
    for t in range(0, len(take)):
        idx[take[t]-1] = 1
    print('Knapsack : ',idx)
    
    #mengembalikan solusi terbaik
    return v[n-1][c-1]


#main program
items = int(input('Berapa banyak item yang ingin anda masukkan? '))
value = []
weight = []
for item in range(0,items):
    val = int(input('Value : '))
    value.append(val)
    wt = int(input('Weight : '))
    weight.append(wt)
print()
capacity = int(input('Capacity : '))
n = len(value)

print('Value = ',value)
print('Weight = ', weight)
print ('Best Value = ', knapsack(capacity , weight , value , n))

