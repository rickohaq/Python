# set mirip list tapi unordered dan isi nya harus unique
# sifatnya mutable (bisa di ubah)
#  adalah koleksi data tak berurutan (unordered), tidak memiliki indeks, dan tidak mengizinkan duplikat. Set mirip dengan himpunan dalam matematika.

route_spine1 = {"10.0.0.0/24", "192.168.0.0/24" , "172.16.0.0/24", "8.8.8.8","8.8.4.4"}
route_spine2 = {"114.5.5.5", "192.168.0.0/24" , "172.16.0.0/24", "8.8.8.8", "10.0.0.0/24"}

route_spine1.add("1.1.1.1")

print(route_spine1) 

route_spine2.remove("114.5.5.5")

print(route_spine2)

# dalam set kita hanya bisa pop random elemnent

# route_spine2.pop()

