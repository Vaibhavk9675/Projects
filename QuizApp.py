print('Quiz_App')
print()

questions = [
    {
        "que": "What is the capital of France?",
        "opt": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
        "ans": "c"
    },
    {
        "que": "Who wrote the Harry Potter series?",
        "opt": ["a) J.K. Rowling", "b) Mark Twain", "c) William Shakespeare", "d) Charles Dickens"],
        "ans": "a"
    },
    {
        "que": "Which planet is known as the Red Planet?",
        "opt": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "ans": "b"
    },
    {
        "que": "What is the chemical symbol for Gold?",
        "opt": ["a) Au", "b) Ag", "c) Gd", "d) Go"],
        "ans": "a"
    },
    {
        "que": "Which is the longest river in the world?",
        "opt": ["a) Nile", "b) Amazon", "c) Ganga", "d) Mississippi"],
        "ans": "a"
    },
    {
        "que": "Who is known as the Father of the Nation in India?",
        "opt": ["a) Jawaharlal Nehru", "b) B. R. Ambedkar", "c) Mahatma Gandhi", "d) Subhas Chandra Bose"],
        "ans": "c"
    },
    {
        "que": "Which gas do plants absorb from the atmosphere?",
        "opt": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "ans": "b"
    },
    {
        "que": "What is the largest ocean on Earth?",
        "opt": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Pacific Ocean", "d) Arctic Ocean"],
        "ans": "c"
    },
    {
        "que": "Who invented the light bulb?",
        "opt": ["a) Alexander Graham Bell", "b) Nikola Tesla", "c) Isaac Newton", "d) Thomas Edison"],
        "ans": "d"
    },
    {
        "que": "What is the national animal of India?",
        "opt": ["a) Elephant", "b) Tiger", "c) Lion", "d) Peacock"],
        "ans": "b"
    }
]

print('Note: Be careful with your answer. You cannot change it after moving to the next question.')

user_input = input('If you want to start quiz, type "start", otherwise type "no":\n')

score = 0

if user_input.lower() == 'start':
    for q in questions:
        print(q['que'])  # show question
        for opt in q['opt']:  # show all options
            print(opt)
        user_ans = input('Your answer: ')
        if user_ans.lower() == q['ans']:
            print('Correct!\n')
            score += 1
        else:
            print('Wrong!\n')
        
        # Ask to continue to next question
        # input_next = input('Type "next" to move to the next question: ')
        # while input_next.lower() != 'next':
        #     input_next = input('Please type "next" to continue: ')

elif user_input.lower() == 'no':
    print('Thanks, Have a nice day!')
    exit()

else:
    print('Enter a valid input!')
    exit()

# After quiz ends
submission = input('Do you want to submit your answers? If yes, type "submit": ')
if submission.lower() == 'submit':
    print(f'Your score is {score} out of {len(questions)}')
    if score == 10:
        print("Wow !, You have scored full marks")

