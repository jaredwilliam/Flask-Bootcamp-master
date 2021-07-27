from flask import Flask, render_template

# Create the flask application
app = Flask(__name__)

@app.route('/')
def index():

    user_logged_in = True

    name = "Jared"
    letters = list(name)
    pup_dict = {'pup_name':'Stella'}

    my_list = [1,2,3,4,5]

    puppies = ['Stella', 'Daisy', 'Judas']

    return render_template('basic.html', name=name, letters=letters, pup_dict=pup_dict,
    my_list=my_list, puppies=puppies, user_logged_in=user_logged_in)
    # Flask is going to automatically look for the templates folder
    # And then in that folder look for basic.html

if __name__ == '__main__':
    app.run(debug=True)
