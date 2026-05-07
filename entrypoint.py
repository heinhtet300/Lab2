import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
    user_input = input()
    number = user_input.split("," )
    num = []
    for i in number:
        num.append(float(i))
    return num

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(statistics.mean(num_list))
    print(min(num_list))
    print(max(num_list))
    
    
    
if __name__=="__main__":
    main()