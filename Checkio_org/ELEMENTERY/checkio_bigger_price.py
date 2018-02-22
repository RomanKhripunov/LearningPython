

# def bigger_price(limit, data):
#     result_data = []
#     tmp_dict = {item["name"]: item["price"] for item in data}
#     sorted_prices_list = sorted(tmp_dict, key=tmp_dict.get, reverse=True)
#     for i in range(limit):
#         for item in data:
#             if item.get("name") == sorted_prices_list[i]:
#                 result_data.append(item)
#                 break
#     return result_data

def bigger_price(limit, data):
    return sorted(data, key=lambda x: x["price"], reverse=True)[:limit]


bigger_price2 = lambda limit, data: sorted(data, reverse=True, key=lambda x: x['price'])[:limit]


if __name__ == '__main__':
    from pprint import pprint
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
