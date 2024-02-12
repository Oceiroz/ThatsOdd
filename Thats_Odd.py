import random
def main():
    random_list()

def random_list():
    number = random.randint(0, 999999999)
    number_list = []
    for char in str(number):
        number_list.append(int(char))
    format_number(number_list)    
    
def format_number(number_list):
    odd_found = 0
    for x in range(0, 9, 1):    
        occurence = number_list.count(x)
        if occurence%2 == 1:
            odd_found += 1
            found_value = x
           
    if odd_found != 1:
        random_list()
    elif odd_found == 1:
        print(number_list)
        print(found_value)
          
main()