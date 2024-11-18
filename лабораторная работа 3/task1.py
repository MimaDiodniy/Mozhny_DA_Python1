# TODO Напишите функцию для поиска индекса товара
def index(products,n):  # Объявили функцию с двумя аргументами
    if n in products:
        return products.index(n)  # возвращаем индекс первого вхождения
    else:
        return None  # если товар не найден, возвращаем None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_product in ['банан', 'груша', 'персик']:  # список искомых товаров
    index_of_product = index(items_list, find_product)  # находим индекс товара
    if index_of_product is not None:
        print(f"Первое вхождение товара '{find_product}' имеет индекс {index_of_product}.")
    else:
        print(f"Товар '{find_product}' не найден в списке.")








