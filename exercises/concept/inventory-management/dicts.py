def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in list(dict.fromkeys(items))}


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        inventory[item] = 1 if item not in inventory.keys() else (inventory[item] + 1)

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in filter(lambda item: item in inventory, items):
        inventory[item] = 0 if not inventory[item] else (inventory[item] - 1)

    return inventory


def remove_item(inventory, item):
    """

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    # inventory.pop(item, None)
    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(item, quantity) for item, quantity in inventory.items() if quantity]
