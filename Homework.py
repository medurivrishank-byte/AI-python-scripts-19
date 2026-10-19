import requests
def get_random_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    if response.status_code==200:
        print(f"Full JSON response: {response.json()}")
        joke_data=response.json()
        print( f"{joke_data['setup']}-{joke_data['punchline']}")
    else:
        print( "Failed to retrieve jokes")
def get_trivia():
    url="https://opentdb.com/api.php?amount=1&type=multiple"
    response=requests.get(url)
    if response.status_code==200:
        print(f"Full JSON response: {response.json()}")
    else:
        print( "Failed to retrieve trivia")
def get_cat_facts():
    url="https://catfact.ninja/fact"
    response=requests.get(url)
    if response.status_code==200:
        print(f"Full JSON response: {response.json()}")
    else:
        print( "Failed to retrieve cat facts")
print("Hi! Welcome to joke trivia and cat facts. What would you like to see today?(1/2/3) Type 'q' to quit")
while True:
    print("1.Jokes")
    print("2.Trivia")
    print("3.Cat facts\n")
    user_input=input()
    if user_input=='1':
        print("Here is a joke:\n")
        get_random_joke()
    elif user_input=='2':
            print("Here is a trivia question with the answer:\n")
            get_trivia()
    elif user_input=='3':
            print("Here is a cat fact:\n")
            get_cat_facts()
    elif user_input=='q':
            print("Goodbye!")
            break
    else:
        print("Please enter 1, 2, 3 or q")
        continue