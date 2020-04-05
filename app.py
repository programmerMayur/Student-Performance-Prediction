from flask import Flask, render_template, request
app = Flask(__name__)
import pickle

file = open('model.pkl','rb')
reg = pickle.load(file)
file.close()
@app.route('/',methods=['GET','POST']) #,methods=['GET','POST']
def mainPage():
    if request.method == "POST":
        allValueFromFORM = request.form
        print(allValueFromFORM)
        one = float(allValueFromFORM["one"])
        two = float(allValueFromFORM["two"])
        three = float(allValueFromFORM["three"])
        four = float(allValueFromFORM["four"])
        five = float(allValueFromFORM["five"])
        six = float(allValueFromFORM["six"])
        inputPara = [one,two,three,four,five,six]
        markProbability = reg.predict([inputPara])[0][0]
        print("probability:",markProbability)

        return render_template('show.html', mark=markProbability)
    return render_template('index.html')

@app.route('/aboutus')
def aboutUs():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug = True)