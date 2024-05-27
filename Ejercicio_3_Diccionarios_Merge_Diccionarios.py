def merge_diccionarios(dic1, dic2):
    dic_merged = dic1.copy()  
    dic_merged.update(dic2)  
    return dic_merged  

dic1 = {'X': 1, 'Y': 2, 'R': 3}
dic2 = {'X': 20, 'Y': 4}
resultado = merge_diccionarios(dic1, dic2)
print("Diccionario combinado:", resultado)

