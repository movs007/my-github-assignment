# my_module.py

#Reverses the input text string.
def reverse_text(text):
    reversed_str = ''
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str

def calculator(operator, first_num, second_num):
    if operator == "add":
        output = first_num + second_num
    elif operator == "sub":
        output = first_num - second_num
    elif operator == "multi":
        output = first_num * second_num
    elif operator == "div":
        output = first_num / second_num
    else:
        print("your have not enter the right operator")
    return output

# Example usage
if __name__ == "__main__":
    print("Reversed Text:", reverse_text("Hello GitHub!"))
    print("Sum of 10 and 5:", calculator("add", 10, 5))
