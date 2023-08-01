from googlesearch import search

query = input("search : ")
for j in search(query, num=10, stop=10):
    print(j)
