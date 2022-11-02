from Order_Stas import OrderStatistics

u = OrderStatistics()
choice = int()
while True:
    print("\n Test heap and quick sorting:")
    print(" 1. Test (descending) heap sort .")
    print(" 2. Test random quick sort")
    print("\n Calculate order statistics:")
    print(" 3. Order statics using heap sort.")
    print(" 4. Order statics using random quick sort")
    print(" 0. Exit ")
    choice = int(input("Your selection (0 -> 4),: "))
    if choice == 0:
        break
    if choice == 1:
        u.test_heapSort()
    elif choice == 2:
        u.test_quickSort()
    elif choice == 3:
        u.test_OS_heap()
    elif choice == 4:
        u.test_OS_quick()
    print()
