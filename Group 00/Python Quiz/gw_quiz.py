def quiz_game():
    print("                Welcome To Python Quiz Game")
    print("     Answer Questions And Find Out How Smart You Are! :D ")

    score = 0
    total_questions = 10

    # Question 1 & 2

    print("------------------------------------------------------------------")

    print("Questions Are From Geograpy! <3")
    N1_question_answer = input("1.რომელია დედამიწის ყველაზე დიდი ოკეანე? \n A) ატლანტის ოკეანე \n B) ინდოეთის ოკეანე \n C) წყნარი ოკეანე \n თქვენი პასუხი: ")

    if N1_question_answer.upper() == "C":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is C")

    print("--------------------------------------------------------------------------")

    N2_question_answer = input("2.რომელი ქვეყანა იყენებს იენს (yen) ვალუტად? \n A) ჩინეთი \n B) იაპონია \n C) სამხრეთ კორეა\n თქვენი პასუხი: ")

    if N2_question_answer.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is B")

    print("--------------------------------------------------------------------------")

    # Question 3 & 4

    print("Questions Are From Literature! <3")
    N3_question_answer = input('3.ვინ არის "ჰარი პოტერის" ავტორი? \n A) ჯეინ ოსტინი \n B) ჯ.კ. როულინგი \n C) სტივენ კინგი \n თქვენი პასუხი: ')

    if N3_question_answer.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is B")

    print("--------------------------------------------------------------------------")

    N4_question_answer = input('4.რომელი მწერალი დაწერა “მატილდა”? \n A) როალდ დალი \n B) ლუის კეროლი \n C) მარკ ტვენი \n თქვენი პასუხი: ')

    if N4_question_answer.upper() == "A":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is A")

    print("--------------------------------------------------------------------------")

    # Question 5 & 6

    print("Questions Are From Science! <3")
    N5_question_answer = input("5.რა ქიმიური სიმბოლო აქვს ოქროს? \n A) Ag \n B) Au \n C) Go \n თქვენი პასუხი: ")

    if N5_question_answer.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is B")

    print("--------------------------------------------------------------------------")

    N6_question_answer = input("6.რამდენი პლანეტაა მზის სისტემაში? \n A) 8 \n B) 9 \n C) 7 \n თქვენი პასუხი: ")

    if N6_question_answer.upper() == "A":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is A")

    print("--------------------------------------------------------------------------")

    # Question 7 & 8

    print("Questions Are From Sports! <3")
    N7_question_answer = input("7.რომელ ქვეყანაში ჩატარდა 2022 წლის ფეხბურთის მსოფლიო ჩემპიონატი? \n A) ბრაზილია \n B) კატარი \n C) საფრანგეთი \n თქვენი პასუხი: ")

    if N7_question_answer.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is B")

    print("--------------------------------------------------------------------------")

    N8_question_answer = input("8.რომელ გუნდში დაიწყო პროფესიული კარიერა კრიშტიანუ რონალდუმ? \n A) რეალი \n B) მანჩესტერ იუნაიტედი \n C) სპორტინგი \n თქვენი პასუხი: ")

    if N8_question_answer.upper() == "C":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is C")

    print("--------------------------------------------------------------------------")

    # Question 9 & 10

    print("Questions Are From Intresting Fun Facts! <3")
    N9_question_answer = input("9.რომელ ფრინველს შეუძლია იცნოს საკუთარი თავი სარკეში? \n A) კაჭკაჭი \n B) მტრედი \n C) ქათამი \n თქვენი პასუხი: ")

    if N9_question_answer.upper() == "A":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is A")

    print("--------------------------------------------------------------------------")

    N10_question_answer = input("10.რამდენი ინფორმაცია შეუძლია ადამიანის ტვინს დაახლოებით დაიმახსოვროს? \n A) 100 გიგაბაიტი \n B) 100 ტერაბაიტი \n C) 1 პეტაბაიტი \n თქვენი პასუხი: ")

    if N10_question_answer.upper() == "C":
        print("Correct!")
        score += 1
    else:
        print("Wrong :( Correct answer is C")

    print("--------------------------------------------------------------------------")

    # ქულების დათვლა

    if score == 0:
        print(f"Your Score Is {total_questions}/{score} Bad You Need To Learn More Things About General Education! <3 ")
    elif score <= 6:
        print(f"Your Score Is {total_questions}/{score} Good Thats Normal Score Not Best But Also Not Worst <3 ")
    elif score <= 9:
        print(f"Your Score Is {total_questions}/{score} Well Done Almost {total_questions}/{total_questions}!")
    elif score == 10:
        print(f"Your Score Is {total_questions}/{score} Congratulation You Are Genius! <3 ")

quiz_game()