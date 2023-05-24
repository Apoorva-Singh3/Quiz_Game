quiz = {
    "Question 1" : {
        "question" : "What is the Capital of France ?",
        "answer" : "Paris"
    },
    "Question 2" : {
        "question" : "What is the Capital of Germany ?",
        "answer" : "Berlin"
    },
    "Question 3" : {
        "question" : "What is the Capital of Spain ?",
        "answer" : "Madrid"
    },
    "Question 4" : {
        "question" : "What is the Capital of Portugal ?",
        "answer" : "Lisbon"
    },
    "Question 5" : {
        "question" : "What is the Capital of Switzerland ?",
        "answer" : "Bern"
    },
    "Question 6" : {
        "question" : "What is the Capital of Italy ?",
        "answer" : "Rome"
    },
    "Question 7" : {
        "question" : "What is the Capital of Austria ?",
        "answer" : "Vienna"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer ?')
    
    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print('Your score is : ' + str(score))
        print('')
        print('')
    else:
        print('Wrong !')
        print('The answer is ' + value['answer'])
        print('Your score is ' + str(score))
        print('')
        print('')
        
print('You got '+ str(score) + ' correct out of 7 questions')
print('Your percentage is ' + str(int(score/7 * 100)) + '%' )