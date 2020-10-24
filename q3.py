def main(int1, int2):
    if int1 > 0 and int2 > 0:
        while int1 % 2 == 0 and int1 % 2 == 0:
            int1 /= 2
            int2 /= 2
            int1 /= 3
            int2 /= 3
            print("The reduced fraction is: {}/{}".format(int1 , int2))

 #  return int1 , int2

if __name__ == "__main__":
    print(
        main(
            int(input("Enter numerator: ")),
            int(input("Enter denominator: "))
        )
    )