stuff = {'rope': 1, 'torch': 6, 'gold_coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in sorted(inventory.items()):
        print(str(v) + ' ' + k)
        item_total += v
    print()
    print('Total number of items: ' + str(item_total))

display_inventory(stuff)
