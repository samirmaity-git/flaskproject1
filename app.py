#Flask application
from flask import Flask, render_template
#Create an instance of the Flask class
# __name__ is a special Python variable that represents the name of the current module
app =Flask(__name__)
#define a route for the root URL ('/') of the web application
@app.route('/')
def Index():
    #Render the HTML template named 'index.html'
    # this template will be rendered and returned as the response to the user's request
    return render_template('index.html')
#this block of code ensures that the Flask web application is only run when this script runs
#and not when it is imported as a module in another script.
if __name__ =="__main__":
    #This start a development server that listens for incoming request
    app.run()
