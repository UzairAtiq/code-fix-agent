def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

assert add_item("a") == ["a"]
assert add_item("b") == ["b"]
