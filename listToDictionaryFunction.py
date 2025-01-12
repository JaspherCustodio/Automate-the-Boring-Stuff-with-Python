def add_to_inventory(inventory, added_items):
    for items in added_items:
        inventory.setdefault(items, 0)
        inventory[items] += 1
    return inventory

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print()
    print('Total number of items: ' + str(item_total))

inv = {'gold_coin': 42, 'rope': 1}
dragon_loot = ['gold_coin', 'dagger', 'gold_coin', 'gold_coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

