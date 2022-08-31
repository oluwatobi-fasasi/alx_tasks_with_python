stack = []

def push():
    print('Enter the element you want to push into the stack')
    num = input()
    stack.append(num)
    print(stack)

def pop():
    if len(stack) == 0:
        print('This is an empty Stack, would you like to add elements to the Stack. y/n?')
        choice = input()
        if choice == 'y':
            push()
        else:
            print('You are quiting this program')
    else:
        stack.pop()
        print(stack)

while True:
    print('Enter ONLY 1 0r 2 for the operation 1.Push 2.Pop')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    else:
        print('You are quiting this program......')
        break

        
