class stack_class():

    def __init__(self):
        self.a_stack = []

    def view(self):
        for x in range(len(self.a_stack)):
            print(self.a_stack[x])

    def push(self):
        item = input("Please enter the item you wish to add to the stack: ")
        self.a_stack.append(item)

    def pop(self):
        item = self.a_stack.pop(-1)
        print("You just popped out: ", item)

def main():

    stack = stack_class()

    while True:
        print("Python Implementation of a stack\n" + "*" * 20)
        print("1. View Stack\n2. Push Into Stack\n3. Pop out of stack\n" + "*" * 20 + "\n")
        menu_choice = int(input("Please enter your menu choice: "))
        print("\n" * 2)    

        if menu_choice == 1: stack.view()
        elif menu_choice == 2: stack.push()
        elif menu_choice == 3: stack.pop()

if __name__ == "__main__":
    main()

