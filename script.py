from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("homepage.html")
 
 
@app.route('/status', methods = ["POST"])
def success():
    if request.method =='POST':
        feet = request.form["feet"]
        inch = request.form["inch"]
        weight = request.form["weight"]
        gender = request.form["gender"]
        feet = int(feet)
        inch = int(inch)
        weight = float(weight)
        inch = feet*12 + inch
        height = (inch*2.54)/100
        bmi = (weight/height)/height
        bmi = round(bmi,1)
        if gender == "Male":
            min_weight = 18.5*height*height
            max_weight = 24.9*height*height
            min_weight = round(min_weight,1)
            max_weight = round(max_weight,1)
            if bmi<18.5:
                status = "Underweight"
                adv = "(Gain more "
                diff = min_weight - weight
                diff= round(diff,1)
                kg = "kg)"
            elif 18.5<= bmi <24.9:
                status = "Healthy"
                adv = ""
                diff = ""
                kg = ""
            elif 24.9<= bmi <29.9:
                status = "Overweight"
                adv = "(Reduce more"
                diff = weight - max_weight
                diff= round(diff,1)
                kg = "kg)"
            else:
                status = "Obese"
                adv = "(Reduce more"
                diff = weight - max_weight
                diff= round(diff,1)
                kg = "kg)"


        if gender == "Female":
            min_weight = 17.5*height*height
            max_weight = 24.9*height*height 
            min_weight = round(min_weight,1)
            max_weight = round(max_weight,1)           
            if bmi<17.5:
                status = "Underweight"
                adv = "(Gain more "
                diff = min_weight - weight
                diff= round(diff,1)
                kg = "kg)"
            elif 17.5<= bmi <24.9:
                status = "Healthy"
                adv = ""
                kg = ""
                diff = ""
            elif 24.9<= bmi <28.9:
                status = "Overweight"
                adv = "(Reduce more"
                diff = weight - max_weight
                diff= round(diff,1)
                kg = "kg)"
            else:
                status = "Obese"
                adv = "(Reduce more"
                diff = weight - max_weight
                diff= round(diff,1)
                kg = "kg)"

        return render_template("status.html", status = status, bmi= bmi, min_weight=min_weight, max_weight=max_weight, diff = diff, adv = adv, kg = kg)
if __name__ == "__main__":
    app.run(debug = True)