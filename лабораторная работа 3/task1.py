# TODO Напишите функцию для поиска индекса товара
def search_index(products,n):
    if n in products:
        return products.index(n)
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_product in ['банан', 'груша', 'персик']:
    index_of_product = search_index(items_list, find_product)
    if index_of_product is not None:
        print(f"Первое вхождение товара '{find_product}' имеет индекс {index_of_product}.")
    else:
        print(f"Товар '{find_product}' не найден в списке.")








