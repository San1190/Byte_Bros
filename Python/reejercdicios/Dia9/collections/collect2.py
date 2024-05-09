from collections import defaultdict

mi_dic = {'uno' : 'verde',
'dos': 'azul',
'tres': 'rojo'}

mi = defaultdict(lambda: 'nada')
mi['uno'] = 'verde'
print(mi_dic['dos'])

print(mi['dos'])


print(mi)