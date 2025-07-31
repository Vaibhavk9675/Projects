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


def ask_question(questions):
    print(questions['que'])
    for option in questions['opt']:
        print(option)
    answere = input("Your answer: ")
    return answere == questions['ans']

def run_quiz(questions):
    score = 0
    for question in questions:
        if ask_question(question): #== True:
            print('Correct!\n')
            score += 1
        else:
            print('Wrong!\n')
    return score 

def submit_quiz(score, total):
    confirm = input('Do you want to submit your answers? If yes, type "submit": ')
    if confirm.lower() == 'submit':
        print(f'Your final score is {score} out of {total}')

def main():
    print("Quiz App\n")
    print('Note: You can’t change your answer after submission.')

    user_input = input("Type 'start' to begin or 'no' to exit: ")
    if user_input.lower() == 'start':
        score = run_quiz(questions)
        submit_quiz(score, len(questions))
    elif user_input.lower() == 'no':
        print("Thanks! Have a nice day.")
    else:
        print("Invalid input.")

main()