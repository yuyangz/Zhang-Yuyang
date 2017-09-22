'''
Yuyang Zhang
SoftDev1 pd07
HW04 -- Fill Up Yer Flask
2017-09-22
'''

from flask import Flask
app = Flask(__name__)

@app.route("/") #root route
def first_route(): 
    return "Root 1"

@app.route("/second") #second route
def second_route():
    return "Root 2"

@app.route("/third") #third route
def third_route():
    return "Root 3" 

if __name__ == "__main__": #allows code to be updated
    app.debug = True 
    app.run()
