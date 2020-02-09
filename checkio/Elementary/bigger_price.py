def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    cp_data = data[:]
    top = []

    while len(top) < limit:
        num_good = 0
        for i in range(len(cp_data)):
            if cp_data[i]['price'] > cp_data[num_good]['price']:
                num_good = i
        for_top = cp_data.pop(num_good)
        top.append(for_top)
    return top

    '''for i in range(len(data)):
        if data[i]['price'] > price_good:
            price_good = data[i]['price']
            num_good = i
    top
        
    return None'''


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
