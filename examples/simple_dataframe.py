from pandas import DataFrame

candi = [[56.4, 62.1], [62.5,63.8],[64.1, 64.5]]

df = DataFrame(candi, columns=['Valores', 'test'])
print(df)