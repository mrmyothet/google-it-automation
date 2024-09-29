def sale_prices(item_and_price):
    item = ""
    price = ""

    item_or_price = item_and_price.split()

    for x in item_or_price:
        if x.isalpha():
            item += x + " "
        else:
            price = x

    item = item.strip()
    return "{} are on sale for ${}.".format(item, price)


print(sale_prices("Winter fleece jackets 49.99"))
# Should print "Winter fleece jackets are on sale for $49.99"


def count_words(data_field):
    split_data = data_field.split()

    return len(split_data)


print(count_words("Catalog item 3523: Organic raw pumpkin seeds in shell"))
# Output should be 9
