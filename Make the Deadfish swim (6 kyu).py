def parse(data):
    output_list = []
    output_element = 0
    for i in data:
        if i == 'i':
            output_element += 1
        elif i == 'd':
            output_element -= 1
        elif i == 's':
            output_element **= 2
        elif i == 'o':
            output_list.append(output_element)
    return output_list
