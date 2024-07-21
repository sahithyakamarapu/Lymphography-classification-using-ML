from flask import Flask, render_template, request
app = Flask(__name__)
import pickle
import joblib

model = pickle.load(open('lymph.pkl', 'rb'))
print()
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
       if request.method=="POST":
           set1=int(float(request.form["set1"]))
           set2=int(float(request.form["set2"]))
           set3=int(float(request.form["set3"]))
           sen1=int(float(request. form["sen1"]))
           sen2=int(float(request.form["sen2"]))
           sen3=int(float(request. form["sen3"]))
           sen4=int(float(request. form["sen4"]))
           sen5=int(float(request. form["sen5"]))
           sen6=int(float(request. form["sen6"]))
           sen7=int(float(request.form["sen7"]))
           sen8=int(float(request. form["sen8"]))
           sen9=int(float(request.form["sen9"]))
           sen10=int(float(request.form["sen10"]))
           set11=int(float(request.form["set11"]))
           set12=int(float(request. form["set12"]))
           set13=int(float(request.form["set13"]))
           set14=int(float(request.form["set14"]))
           set15=int(float(request.form["set15"]))
           
           x_test = [[set1,set2,set3,sen1,sen2,sen3,sen4,sen5,sen6,sen7,sen8,sen9,sen10,set11,set12,set13,set14,set15]]
           print(x_test)
           prediction = model.predict(x_test)
           print(prediction) 

           if prediction == 1:
               return render_template("predict.html",y="Normal Find")
           elif prediction == 2:
               return render_template("predict.html",y="Metastases")
           elif prediction == 3:
               return render_template("predict.html",y="Malign Lymph")
           elif prediction == 4:
               return render_template("predict.html",y='Fibrosis')
if __name__=='__main__':
    app.run(debug=True)