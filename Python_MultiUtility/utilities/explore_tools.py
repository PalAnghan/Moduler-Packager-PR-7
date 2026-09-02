import importlib


def explore_module(module_name):
    try:
        module = importlib.import_module(module_name)

        print("\nAvailable Attributes:")
        print(dir(module))

    except ModuleNotFoundError:
        print("Module not found. Please enter a valid module name.")


if __name__ == "__main__":
    print("=" * 40)
    print("Explore Module Attributes")
    print("=" * 40)

    module_name = input("Enter module name to explore: ")

    explore_module(module_name)

    print("=" * 40)