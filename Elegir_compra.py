#Función en Python que recibe una lista de precios, una lista de cantidades, un valor de restricción y una lista de nombres.
# Devuelve una lista que contiene los nombres de los productos que se pueden comprar y el número total de productos que no se pueden comprar.
def whatToBuy(prices, quantities, restriction, names):
    
    if len(prices) == 0:
        return [[], 0]

    semifinal_lst = []
    final_lst = []
    total_price = 0
    average_quantity = sum(quantities) / len(quantities)
    average_price = sum(prices) / len(prices)
    total_items = 0

    for i in range(len(names)):
        total_price = (prices[i] * quantities [i]) / (average_price * average_quantity) 
        if total_price < restriction:
            semifinal_lst.append(names[i])
        else:
            total_items += 1

    final_lst = [semifinal_lst, total_items]

    print(final_lst)