# Header level 1
## Header level 2
### Header level 3


the following code does this....
``` python
plt.figure(figsize=(12,5))
plt.title('top categories based on annual sales')
plt.bar(df['categoryname'].values,height=df['TotalSales'].values)

for i in range(len(df['categoryname'])):
    plt.annotate(xy=(i,df['TotalSales'].values[i]),
                 text = df['TotalSales'].values[i],
                 horizontalalignment='center')


plt.xticks(rotation=90)
plt.savefig('annualsales-categories.jpeg')
plt.show()
```
