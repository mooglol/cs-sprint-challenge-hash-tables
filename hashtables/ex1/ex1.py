def get_indices_of_item_weights(weights, length, limit):
    """
    get_indices_of_item_weights
    """
    cache = {}

    for i in range(length):
        weight = weights[i]
        target = limit - weight

        if target in cache:
            j = cache[target]
            return [i,j]
        else:
            cache[weight] = i

    return None