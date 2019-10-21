import math


def circle():
    radius = float(input("Enter a circle radius : "))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print('Perimeter : %.2f' % perimeter)
    print('Area : %.2f' % area)


def main():
    try:
        circle()
    except ValueError:
        print('Invalid number. Try again')
        main()
    except:
        print('Unknown error')
        main()


main()
