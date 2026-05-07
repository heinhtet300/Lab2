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
def calc_average_temperature(num):
    return sum(num)/len(num)
def calc_min_max_temperature(alist):
    num = []
    num.append(min(alist))
    num.append(max(alist))
    return num

def calc_median_temperature(alist):
    num = sorted(alist)
    if len(num)%2 == 0:
        median = (num[len(num)//2-1]+ num[len(num)//2])/2
    else:
        median = num[len(num)//2]
        
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))
    print(calc_median_temperature(num_list))
    
    
if __name__=="__main__":
    main()