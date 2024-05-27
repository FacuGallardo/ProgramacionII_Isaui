def merge_diccionarios(dic1, dic2):
    dic_merged = dic1.copy()  
    dic_merged.update(dic2)  
    return dic_merged  

dic1 = {'p': 14, 'b': 8, 'cd': 30}
dic2 = {'b': 20, 'cd': 4}
resultado = merge_diccionarios(dic1, dic2)
print("Diccionario combinado:", resultado)
