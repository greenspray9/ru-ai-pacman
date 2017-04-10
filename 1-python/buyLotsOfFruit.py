fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):

    totalCost = 0;
    for tuple in orderList:
        quantity = tuple[1]
        name 	 = tuple[0]

        if quantity < 0:
            print('wrong quantity of', quantity)
        elif not(name in fruitPrices):
            print(name ,'not in list')
        else:
            perFruitPrice = fruitPrices[name]
            totalCost = totalCost + quantity * perFruitPrice

    return totalCost


orderList = [('apples', 2), ('pears', 3), ('limes', 4), ('apples', -10), ('pineapple', 10)]
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
