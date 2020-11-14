def get_order(order):
    menu = "1. Burger\
            2. Fries\
            3. Chicken\
            4. Pizza\
            5. Sandwich\
            6. Onionrings\
            7. Milkshake\
            8. Coke"
    menu_list_num = menu.split()
    menu_list = [item for item in menu_list_num if item.isalpha()]
    word = ''
    new_order = []
    for letter in order:
        word += letter
        if word.capitalize() in menu_list:
            new_order.append(word.capitalize())
            word=''
    new_order_len = len(new_order)
    for i in range(new_order_len-1):
        for j in range(new_order_len-i-1):
            if menu_list.index(new_order[j])>menu_list.index(new_order[j+1]):
                new_order[j], new_order[j+1] = new_order[j+1], new_order[j]
    return ' '.join(new_order)