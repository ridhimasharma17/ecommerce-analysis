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


![Image](https://www.google.com/imgres?q=bookshop&imgurl=https%3A%2F%2Fimages.squarespace-cdn.com%2Fcontent%2Fv1%2F622e1d447366587b354dbc19%2Fbffb5df4-b3bf-46f6-8f03-f8d9ad434665%2FIMG_4592.jpg&imgrefurl=https%3A%2F%2Fwww.thefolkestonebookshop.co.uk%2F&docid=aCLEalHr8tgOeM&tbnid=EAF9YEdVlGO_VM&vet=12ahUKEwjeoqGjqbKGAxWqcWwGHRWgAcwQM3oECBcQAA..i&w=2500&h=1406&hcb=2&ved=2ahUKEwjeoqGjqbKGAxWqcWwGHRWgAcwQM3oECBcQAA)
