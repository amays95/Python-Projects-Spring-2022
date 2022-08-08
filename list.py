def get_input(prompt='Please enter your birth year, HS graduation year, and College graduation year: '):
    ui=input(prompt)
    print(ui)


def make_list(num):
    num_list=input(num)
    print(num_list)
    try:
        user_input = get_input(prompt='Please enter your birth year, HS graduation year, and College grad year')
        if user_input is not int:
            raise TypeError('Only Numbers Allowed')
    except TypeError('Only Numbers Allowed'):
        print('Only Numbers Allowed')
    else:
        print(user_input)
    finally:
        print('Saved')

    user_list=[]
    user_list_input = 2000
    num = 1900
    while user_list_input >= num:
        user_list.append(user_list_input)
    user_list_input = input("Enter birth year, HS grad year, and College grad year:")
    if user_list_input is str:
        raise TypeError
    print('Here is your completed list!')
    print(user_list)
