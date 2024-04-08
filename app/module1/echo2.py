from module1 import PI, square_area

def echo2_test():
    print("PI:", PI)
    # 使用函数 square_area
    side_length = 5
    area = square_area(side_length)
    print("Square area with side length", side_length, ":", area)