from store import Store
from shop import Shop
from request import Request

if __name__ == "__main__":
    shop = Shop()
    store = Store()


    store.add("cookies", 15)
    store.add("waffles", 15)
    store.add("milk", 15)

    shop.add("cookies", 5)
    shop.add("waffles", 5)
    shop.add("milk", 5)


    shop.remove("milk", 3)

    user_input = input()

    if ("Доставить" not in user_input) or ("из" not in user_input) or ("в" not in user_input):
        print("Incorrect format, check for words 'Доставить', 'из', 'в'")
    else:
        req = Request(user_input)
        if req.product in store.items:
            print(f"{type(req.product)} : {type(req.amount)}")
            resp1 = store.remove(req.product, int(req.amount))
            print(resp1)
            if "Not enough" not in resp1:
                print(f"Items in storage: {store.items}")
                resp2 = shop.add(req.product, int(req.amount))
                print(resp2)
                if "Not enough" not in resp2:
                    print(f"Items in shop: {shop.items}")

