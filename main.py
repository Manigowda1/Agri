from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/success')
def success():
    Number_of_bags=int(request.args.get('Bnum'))
    Rate_per_quintal=int(request.args.get('Qrate'))
    Rate_of_emty_bag=int(request.args.get('Erate'))
    Cost_of_each_bag=(Rate_per_quintal*68)/100
    Total_cost_without_emtybags=Number_of_bags*Cost_of_each_bag
    Total_cost_with_emtybags=Total_cost_without_emtybags-(Number_of_bags*Rate_of_emty_bag)
    Final_total=Total_cost_with_emtybags
    return render_template("Result.html",Num_of_bags=Number_of_bags,Final_cost=Final_total)

if __name__=='__main__':
    app.run(debug=True)
