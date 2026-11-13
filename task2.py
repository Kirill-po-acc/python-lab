inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}


def update_inventory(data: dict, category: str, discount: float) -> None:
    for sku in data:
        item = data[sku]                    # read

        # UPDATE (Flash Sale)
        if item["category"] == category:
            item["price"] = item["price"] * (1 - discount)   # write

        # LOGIC (Restock Alert)
        if item["stock_count"] == 0:
            item["restock_urgent"] = True   # write

        # SAFE ACCESS (Data Integrity)
        item.setdefault("last_sold", "Never")

    return None


update_inventory(inventory, "Electronics", 0.15)

# VIEW
for sku in inventory:
    print(sku, inventory[sku])


# UPDATE (Flash Sale):  #    Apply a 15% discount to the 'price' of every item in the "Electronics" category.
# LOGIC (Restock Alert):  #    Loop through the inventory. If 'stock_count' is 0, add a new key  #    called 'restock_urgent' with the value True.
# SAFE ACCESS (Data Integrity):  #    Check for a 'last_sold' key. If it doesn't exist, use .setdefault()  #    to set it to "Never".
# VIEW: Print the final updated inventory.