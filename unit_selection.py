

from majowl_unit_selection import *

lesson_list = []

while True:
    option = show_menu()
    match option:
        case 1:
            lesson = get_lesson()
            if validate_lesson(lesson):
                lesson_list.append(lesson)
                print("saved lesson")
            else:
                print("error")
        case 2:
            show_lesson(lesson_list)
        case 3:
            teacher_name = input("enter teacher name: ")
            if search_by_teacher(lesson_list , teacher_name):
                print("found")
            else:
                print("your lesson not found")
        case 0:
            print("exiting")
            break
        case _:
            print("invalid option")