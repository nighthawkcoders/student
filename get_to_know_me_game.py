# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
questions = ["When is my birthday", "What is my favorite food","What is my favorite color","What is favorite food"]
responses = [["A. July 8th", "B. January 9th", "C. November 27th", "D. June 9th"],
            ["A. Pizza", "B. Salad", "C. Pasta", "D. Mac&Cheese"],
            ["A. Blue", "B. Green", "C. Red", "D. Black"],
            ["A. 12", "B. 11", "C. 19", "D. 13"]];
answer = ["A","D","B","D"]
print("Hello. Wellome to the Get To Know Me Game. This is a multiple choice test that will test your knowledge about me")
user_answer = ""
for i in range(len(questions)):
    print(questions[i])
    for j in range(4):
        print(response[i][j])   
    user_answer = input()

    if user_answer == answer[i]:
        print("Correct!")
    else:
        print("Incorrect")
        
print()
print("Thank for playing the game")