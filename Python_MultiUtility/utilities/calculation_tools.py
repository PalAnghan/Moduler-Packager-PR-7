import math


class MathOperations:

    def calculate_factorial(self, number):
        if number < 0:
            return "Factorial is not defined for negative numbers."
        return math.factorial(number)

    def compound_interest(self, principal, rate, time):
        return principal * (1 + rate / 100) ** time

    def trigonometric_functions(self, angle):
        radians = math.radians(angle)

        return {
            "sin": math.sin(radians),
            "cos": math.cos(radians),
            "tan": math.tan(radians)
        }

    def geometric_calculations(self, shape, dimensions):

        if shape == "circle":
            radius = dimensions["radius"]
            return math.pi * radius ** 2

        elif shape == "rectangle":
            length = dimensions["length"]
            width = dimensions["width"]
            return length * width

        elif shape == "triangle":
            base = dimensions["base"]
            height = dimensions["height"]
            return 0.5 * base * height

        return "Unsupported shape."


def math_menu():

    calc = MathOperations()

    while True:

        print("\n" + "=" * 30)
        print("Mathematical Operations")
        print("=" * 30)

        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Functions")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))

            match choice:

                case 1:
                    number = int(input("Enter a number: "))

                    result = calc.calculate_factorial(number)

                    print(f"Factorial of {number}: {result}")

                case 2:
                    principal = float(input("Enter principal amount: "))
                    rate = float(input("Enter interest rate (%): "))
                    time = float(input("Enter time (years): "))

                    result = calc.compound_interest(
                        principal, rate, time
                    )

                    print(f"Compound Amount: {result:.2f}")

                case 3:
                    angle = float(input("Enter angle in degrees: "))

                    result = calc.trigonometric_functions(angle)

                    print(f"sin({angle}) = {result['sin']:.4f}")
                    print(f"cos({angle}) = {result['cos']:.4f}")
                    print(f"tan({angle}) = {result['tan']:.4f}")

                case 4:
                    shape = input(
                        "Enter shape (circle, rectangle, triangle): "
                    ).lower()

                    if shape == "circle":
                        radius = float(input("Enter radius: "))

                        dimensions = {
                            "radius": radius
                        }

                    elif shape == "rectangle":
                        length = float(input("Enter length: "))
                        width = float(input("Enter width: "))

                        dimensions = {
                            "length": length,
                            "width": width
                        }

                    elif shape == "triangle":
                        base = float(input("Enter base: "))
                        height = float(input("Enter height: "))

                        dimensions = {
                            "base": base,
                            "height": height
                        }

                    else:
                        print("Unsupported shape.")
                        continue

                    result = calc.geometric_calculations(
                        shape, dimensions
                    )

                    print(f"Area of {shape}: {result:.2f}")

                case 5:
                    break

                case _:
                    print("Invalid choice. Please choose 1-5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")