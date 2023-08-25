raw_terms = open("terms.txt","r")
terms = []
for i in range(13):
    terms.append(raw_terms.readline().strip("\n").split("="))

search = ""
is_md = "on Markdown"
found = False
while True:
    search = input("Enter your search: ")
    for i in range(len(terms)):
        if search == terms[i][0]:
            found = True
            if is_md in search:
                print("Format: ", terms[i][1])

            else:
                print("Definition:", "\n", terms[i][1])

    if found == False:
        print("Sorry we can't find that term. Make sure you have spell your query correctly")


print(terms)