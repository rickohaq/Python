# set mirip list tapi unordered dan isi nya harus unique
# sifatnya mutable (bisa di ubah)
#  adalah koleksi data tak berurutan (unordered), tidak memiliki indeks, dan tidak mengizinkan duplikat. Set mirip dengan himpunan dalam matematika.

route_spine1 = {"10.0.0.0/24", "192.168.0.0/24" , "172.16.0.0/24", "8.8.8.8","8.8.4.4"}
route_spine2 = {"114.5.5.5", "192.168.0.0/24" , "172.16.0.0/24", "8.8.8.8", "10.0.0.0/24"}

print(route_spine1 - route_spine2)

print(route_spine2 - route_spine1)


print(route_spine2.difference(route_spine1))

print(route_spine2.union(route_spine1))