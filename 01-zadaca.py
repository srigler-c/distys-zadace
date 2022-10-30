def f1(l):
    lista = [x for x in l if type(x) == str]
    print([x for x in lista if len(x) > 4])

print(f1([1,2,'Pas', 'Macka', 'Stol']))


def f3(x):
    return{y for d in x for _,y in d.items()}
print(f3([{"ip":"192.168.3.1"}, {"ip":"10.0.0.0"}, {"ip":"127.0.0.0"},{"ip":"192.168.3.1"}]))
