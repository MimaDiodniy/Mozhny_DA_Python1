# TODO Найдите количество книг, которое можно разместить на дискете
size_book=100*50*25*4
size_disk=1.44*1024*1024
n=int(size_disk)//(size_book)
print("Количество книг, помещающихся на дискету:", n)
