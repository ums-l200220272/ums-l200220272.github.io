from metaflow import Flow

run = Flow('ManyKmeansFlow').latest_run
k3 = run.data.results[3]
k4 = run.data.results[4]
k5 = run.data.results[5]

print("3 Clusters:", k3)
print("4 Clusters:", k4)
print("5 Clusters:", k5)

# from metaflow import Flow
# run = Flow('ManyKmeansFlow').latest_run

# k3 = run.data.results[3] #mengambil hasil clustering menjadi 3 kluster
# k4 = run.data.results[4] 
# k5 = run.data.results[5] 

# print(k3[0][:3])    #untuk menampilkan 3 kata teratas di kluster pertama(index = 0)
# print(k3[1][:3])    #untuk menampilkan 3 kata teratas di kluster kedua(index = 1)
# print(k3[2][:3])     #untuk menampilkan 3 kata teratas di kluster ketiga(index = 2)

# print(k4[0][:3])     #untuk menampilkan 3 kata teratas di kluster pertama(index = 0)
# print(k4[1][:3] )    #untuk menampilkan 3 kata teratas di kluster kedua(index = 1)
# print(k4[2][:3] )    #untuk menampilkan 3 kata teratas di kluster ketiga(index = 2)
# print(k4[3][:3] )    #untuk menampilkan 3 kata teratas di kluster keempat(index = 3)