# Grade evaluation using match-case statement.

subject = input("Enter a subject: ")

score = int(input("Enter a score: "))

match subject:
    case 'Physics' | 'Chemistry' if score >= 80:
        print("Excellent in Science!")

    case 'English' | 'Grammar' if score >= 80:
        print("Excellent in English!")

    case 'Maths' if score >= 80:
        print("Excellent in Maths!")

    case _:
        print(f"Needs improvement in {subject}!")