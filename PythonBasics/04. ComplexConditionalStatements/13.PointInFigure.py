h = int(input())
x = int(input())
y = int(input())

is_Inside_On_Top_Figure = (x > h and x < 2 * h) and (y > h and y < 4 * h)
is_Inside_On_Bottom_Figure = (x > 0 and x < 3 * h) and (y > 0 and y < h)
is_On_The_Special_Place = y == h and (x > h and x < 2 * h)

is_Inside_The_Whole_Figure = is_Inside_On_Top_Figure or is_Inside_On_Bottom_Figure or is_On_The_Special_Place

if is_Inside_The_Whole_Figure:
    print("inside")
else:
    is_On_TopLeft_Side = x == h and (y >= h and y <= 4 * h)
    is_On_TopTop_Side = y == 4 * h and (x >= h and x <= 2 * h)
    is_On_TopRight_Side = x == 2 * h and (y >= h and y <= 4 * h)

    is_On_Top_Figure_Side = is_On_TopLeft_Side or is_On_TopTop_Side or is_On_TopRight_Side

    is_On_BottomBottom_Side = y == 0 and (x >= 0 and x <= 3 * h)
    is_On_BottomLeft_Side = x == 0 and (y >= 0 and y <= h)
    is_On_BottomRight_Side = x == 3 * h and (y >= 0 and y <= h)
    is_On_BottomTopLeft_Side = y == h and (x >= 0 and x <= h)
    is_On_BottomTopRight_Side = y == h and (x >= 2 * h and x <= 3 * h)

    is_On_Bottom_Figure = is_On_BottomBottom_Side or is_On_BottomLeft_Side or is_On_BottomRight_Side or \
                            is_On_BottomTopLeft_Side or is_On_BottomTopRight_Side

    is_OnBorder_Figure = is_On_Top_Figure_Side or is_On_Bottom_Figure

    if is_OnBorder_Figure:
        print("border")
    else:
        print("outside")
