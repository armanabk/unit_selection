from tamrin_majowl import *

lesson_list = []


while True:
    option = show_menu()

    match option:
        case 1:
            lesson = get_lesson()
            if validate_lesson(lesson):
                if calculate_total(lesson_list)+ lesson["unit"] <= 17:
                    lesson_list.append(lesson)
                    print("saved")
                else:
                    print("cant get more lesson")
            else:
                print("error !!!: invalid lesson unit , must be 1,2,3,5")

        case 2:
            show_lesson(lesson_list)
        case 3:
            teacher_name = input("inter teacher name:")
            if search_by_teacher(lesson_list , teacher_name):
                print("found")
            else:
                print("not found")

        case 0:
            print("exiting")
            break
        case _:
            print("invslid option")