import random

# Define 50 questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 11", "B. 12", "C. 13", "D. 14"],
        "answer": "B"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {"question": "What is the capital of France?", "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"], "answer": "A"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "answer": "B"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "answer": "C"},
    {"question": "Who invented the lightbulb?", "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Thomas Edison", "D. Galileo"], "answer": "C"},
    {"question": "Which continent is the largest?", "options": ["A. Africa", "B. Asia", "C. North America", "D. Europe"], "answer": "B"},
    {"question": "What is the boiling point of water?", "options": ["A. 50°C", "B. 75°C", "C. 100°C", "D. 125°C"], "answer": "C"},
    {"question": "Which language is primarily spoken in Brazil?", "options": ["A. Spanish", "B. French", "C. Portuguese", "D. English"], "answer": "C"},
    {"question": "How many continents are there?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "C"},
    {"question": "Which is the longest river in the world?", "options": ["A. Amazon", "B. Nile", "C. Mississippi", "D. Yangtze"], "answer": "B"},
    {"question": "What is the chemical symbol for gold?", "options": ["A. Au", "B. Ag", "C. Gd", "D. Go"], "answer": "A"},

    {"question": "Which organ pumps blood in the human body?", "options": ["A. Brain", "B. Liver", "C. Heart", "D. Lungs"], "answer": "C"},
    {"question": "What is the capital of India?", "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"], "answer": "B"},
    {"question": "Which is the smallest planet in the solar system?", "options": ["A. Earth", "B. Mars", "C. Mercury", "D. Pluto"], "answer": "C"},
    {"question": "How many sides does a hexagon have?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "B"},
    {"question": "Which ocean is the largest?", "options": ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"], "answer": "B"},
    {"question": "Which country gifted the Statue of Liberty to the USA?", "options": ["A. Germany", "B. France", "C. Italy", "D. Spain"], "answer": "B"},
    {"question": "How many bones are there in the adult human body?", "options": ["A. 206", "B. 201", "C. 210", "D. 250"], "answer": "A"},
    {"question": "Which gas is most abundant in Earth's atmosphere?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "answer": "B"},
    {"question": "What is the fastest land animal?", "options": ["A. Lion", "B. Tiger", "C. Cheetah", "D. Leopard"], "answer": "C"},
    {"question": "What does DNA stand for?", "options": ["A. Data Node Array", "B. Deoxyribonucleic Acid", "C. Digital Network Algorithm", "D. Dynamic Number Access"], "answer": "B"},

    {"question": "What is the currency of Japan?", "options": ["A. Yuan", "B. Won", "C. Yen", "D. Dollar"], "answer": "C"},
    {"question": "Which instrument has 88 keys?", "options": ["A. Violin", "B. Guitar", "C. Piano", "D. Flute"], "answer": "C"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Leo Tolstoy"], "answer": "C"},
    {"question": "Which blood type is the universal donor?", "options": ["A. A", "B. B", "C. AB", "D. O-"], "answer": "D"},
    {"question": "What is the square root of 81?", "options": ["A. 7", "B. 8", "C. 9", "D. 10"], "answer": "C"},
    {"question": "Which country has the most population?", "options": ["A. India", "B. China", "C. USA", "D. Russia"], "answer": "A"},
    {"question": "Which festival is known as the Festival of Lights?", "options": ["A. Holi", "B. Eid", "C. Christmas", "D. Diwali"], "answer": "D"},
    {"question": "Which part of the plant conducts photosynthesis?", "options": ["A. Roots", "B. Stem", "C. Leaves", "D. Flowers"], "answer": "C"},
    {"question": "What is H2O commonly known as?", "options": ["A. Hydrogen", "B. Salt", "C. Water", "D. Oxygen"], "answer": "C"},
    {"question": "How many players are there in a football team?", "options": ["A. 9", "B. 10", "C. 11", "D. 12"], "answer": "C"},

    {"question": "Which is the largest mammal?", "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"], "answer": "B"},
    {"question": "Which planet has rings?", "options": ["A. Earth", "B. Mars", "C. Venus", "D. Saturn"], "answer": "D"},
    {"question": "What does CPU stand for?", "options": ["A. Central Processing Unit", "B. Control Panel Unit", "C. Central Power Unit", "D. Core Processing Unit"], "answer": "A"},
    {"question": "Which vitamin is provided by sunlight?", "options": ["A. A", "B. B", "C. C", "D. D"], "answer": "D"},
    {"question": "Which bird is the national bird of India?", "options": ["A. Parrot", "B. Peacock", "C. Eagle", "D. Swan"], "answer": "B"},
    {"question": "How many hours are there in a day?", "options": ["A. 12", "B. 24", "C. 36", "D. 48"], "answer": "B"},
    {"question": "Who painted the Mona Lisa?", "options": ["A. Picasso", "B. Van Gogh", "C. Da Vinci", "D. Michelangelo"], "answer": "C"},
    {"question": "Which state is known as the 'Land of Five Rivers'?", "options": ["A. Gujarat", "B. Punjab", "C. Kerala", "D. Assam"], "answer": "B"},
    {"question": "Which animal is known as the ship of the desert?", "options": ["A. Camel", "B. Horse", "C. Donkey", "D. Elephant"], "answer": "A"},
    {"question": "What color do you get when you mix red and yellow?", "options": ["A. Green", "B. Orange", "C. Purple", "D. Blue"], "answer": "B"},

    {"question": "Which metal is liquid at room temperature?", "options": ["A. Mercury", "B. Iron", "C. Silver", "D. Copper"], "answer": "A"},
    {"question": "What is the national flower of India?", "options": ["A. Rose", "B. Lotus", "C. Jasmine", "D. Lily"], "answer": "B"},
    {"question": "Which is the tallest mountain in the world?", "options": ["A. K2", "B. Mount Everest", "C. Kangchenjunga", "D. Lhotse"], "answer": "B"},
    {"question": "Who is known as the father of computers?", "options": ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"]
}
    # Add more questions up to 50
]

# Add dummy questions to make the count 50 (you can customize these)
for i in range(6, 51):
    questions.append({
        "question": f"Sample Question {i}: What is {i} + {i}?",
        "options": [f"A. {i+i-1}", f"B. {i+i}", f"C. {i+i+1}", f"D. {i+i+2}"],
        "answer": "B"
    })

# Randomly select 10 questions
selected_questions = random.sample(questions, 10)

# Initialize score
score = 0

# Start the quiz
print("📘 Welcome to the Python Quiz!\nAnswer the following 10 questions:\n")

# Loop through the selected questions
for i, q in enumerate(selected_questions, start=1):
    print(f"Question {i}: {q['question']}")
    for option in q['options']:
        print(option)
    
    # Input validation loop
    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            break
        print("⚠️ Invalid input. Please enter A, B, C, or D.")

    if user_answer == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong!correct answer is:{q['answer']}\n")

# Final score
print("🎉 Quiz Completed!")
print(f"Your Score: {score} / 10")
