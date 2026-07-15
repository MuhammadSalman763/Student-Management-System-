from student_manager import StudentManager

manager = StudentManager()

while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Total Students")
    print("7. Topper")
    print("8. Average CGPA")
    print("9. Generate 1000 Fake Students")
    print("10. Department Wise Students")
    print("0. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        manager.add_student()

    elif choice == "2":
        
        manager.view_students()

    elif choice == "3":

        manager.search_student()

    elif choice == "4":

        manager.delete_student()

    elif choice == "5":

        manager.update_student()

    elif choice == "6":

        manager.total_students()

    elif choice == "7":

        manager.topper()

    elif choice == "8":

        manager.average()

    elif choice == "9":

        manager.generate_fake_students()

    elif choice == "10":

        manager.department_students()

    elif choice == "0":
        
        print("Thank You!")

        break

    else:

        print("Invalid Choice.")
