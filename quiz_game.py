def main():
    score = 0

    def read_title():
        title = f.readline()
        return title
    def read_category():
        category=f.readline()
        return category
    def read_question():
        question=[]
        for i in range(0,1):
            a= f.readline()
            a = a.replace('/','\n')
            question.append(a)
        return question
    def read_answers():
        answers = []
        for i in range(0,4):
            answers.append(f.readline())
        return answers
    def right_answer():
        correct=f.readline()
        return correct
    def user():
        while 0 == 0:
            try:
                user_answer =int(input("Podaj swoją odpowiedź 1-4 : \n"))
            except:
                print('to nie jest odpowiedź')
            else:
                return user_answer
    def next_block(score):
        category=read_category()
        question = read_question()
        answers = read_answers()
        print(category)
        for i in question:
            print(i)
        for i in range(0,4):
            print(i+1,') ',answers[i])
        correct=int(right_answer())
        user_answer=int(user())
        if correct == user_answer:
            print('\nPoprawna dodpowiedź\n')
            score+=1
        else:
            print('\nNiepoprawna odpowiedź\n')
            print('Poprawna Odpowiedź to :', answers[int(correct)-1],'\n')
        print('Wyjaśnienie:\n')
        a=f.readline()
        a=a.replace('/','\n')
        print(a)
        return score
    title = read_title()
    print((title))

    for i in range(0,5):
       score=next_block(score)
    print('Ilość twoich punktów to: ',score)
    input('Enter zeby zkaończyc program')




    f.close()

try:
    c=0
    f = open('kwiz.txt','r')

except:
    print('error')
else:
    main()

