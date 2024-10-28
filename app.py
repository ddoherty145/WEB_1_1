from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, David!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'This is going to sound crazy, but I also love {users_dessert}!'

@app.route('/madlib/<adjective_entry>/<noun_entry>')
def madlib_entry(adjective_entry, noun_entry):
    """Display a funny madlib"""
    return f'This world of {noun_entry} is doomed, the only thing that can save it is a {adjective_entry} Sword of {noun_entry}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiplies two numbers"""
    if number1.isdigit() and number2.isdigit():
        total = int(number1) * int(number2)
        return f'{number1} multiplied by {number2} is {total}'
    else:
        return 'Please provide valid intergers for multiplication.'
    
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Repeates a word a given number if times"""
    if n.isdigit():
        times = int(n)
        repeated_string = ' '.join([word] * times)
        return repeated_string
    else:
        return 'Invalid input. First enter a word then a number!'

@app.route('/dicegame')
def dicegame():
    """Rolls a dice where rolling 6 means you win"""
    roll = random.randint(1, 6)
    if roll == 6:
        return f'You rolled a {roll}. You won!'
    else:
        return f'You rolled a {roll}. You lost!'
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)


if __name__=='__main__':
    app.run(debug=True)