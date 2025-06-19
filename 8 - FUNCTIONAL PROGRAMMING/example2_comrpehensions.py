ages = {"ricko":34, "Diah":31, "Mecca":3, "Aqsa":1}

create_ktp = {k:v for k,v in ages.items() if v>20}
list_ktp = [ ]
print(create_ktp)