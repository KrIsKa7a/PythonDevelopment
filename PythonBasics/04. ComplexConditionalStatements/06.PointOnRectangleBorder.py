x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x = float(input())
y = float(input())

is_on_top_side = (x >= x1 and x <= x2) and y == y1
is_on_left_side = (y >= y1 and y <= y2) and x == x1
is_on_bottom_side = (x >= x1 and x <= x2) and y == y2
is_on_right_side = (y >= y1 and y <= y2) and x == x2

is_on_border = is_on_top_side or is_on_bottom_side or is_on_left_side or is_on_right_side

if is_on_border:
    print("Border")
else:
    print("Inside / Outside")
