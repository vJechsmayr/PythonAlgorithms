def split_string(string):
    list_string = string.split(' ')
    return list_string



def join_string(list_string):
    string = '-'.join(list_string)
    return string



if __name__ == '__main__':
    input_str = 'coding is awesome'
    list_string = split_string(input_str)
    print(list_string)
    new_string = join_string(list_string)
    print(new_string)