color_dict = {
    'black' : {'value' : 0, 'multiply': 1},
    'brown' : {'value' : 1, 'multiply': 10},
    'red' : {'value' : 2, 'multiply': 100},
    'orange' : {'value' : 3, 'multiply': 1000},
    'yellow' : {'value' : 4, 'multiply': 10000},
    'green' : {'value' : 5, 'multiply': 100000},
    'blue' : {'value' : 6, 'multiply': 1000000},
    'violet' : {'value' : 7, 'multiply': 10000000},
    'grey' : {'value' : 8, 'multiply': 100000000},
    'white' : {'value' : 9, 'multiply': 1000000000},
}

def get_first_two_digits(color_dict, A, B):
    value_A = color_dict[A]['value']
    value_B = color_dict[B]['value']

    return value_A * 10 + value_B

def calculate_resistance(color_dict, A, B, C):
    first_two = get_first_two_digits(color_dict, A, B)

    multiply = color_dict[C]['multiply']

    return first_two * multiply

A = input()
B = input()
C = input()

result = calculate_resistance(color_dict, A, B, C)

print(result)