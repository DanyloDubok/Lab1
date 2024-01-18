
def get_user_name():
    """
    Отримує ім'я користувача або залишає значення 'User', якщо аргумент не вказано.
    """
    if len(sys.argv) > 1:
        return sys.argv[1]
    return 'User'

def print_greeting(user):
    """
    Друкує привітання для користувача з використанням переданого імені.
    """
    msg = f'Hello, {user}!'
    print(msg)


def get_user_info():
    """
    Отримує вік та ім'я користувача.
    """
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    return name, age

def print_greeting_with_age(name, age):
    """
    Друкує привітання з іменем та віком користувача.
    """
    print(f"Привіт, {name}! Тобі вже {age} років.")
    if age >= 18:
        print("Треба вже чимось корисним зайнятись!")

if __name__ == "__main__":
    import sys

    #words = ('hello', 'python', 'world')
    #print(' '.join(words))
    #user_name = get_user_name()
    #print_greeting(user_name)
    user_name, user_age = get_user_info()
    print_greeting_with_age(user_name, user_age)

