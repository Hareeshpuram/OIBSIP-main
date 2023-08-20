from flask import Flask,render_template,request
import pickle
model=pickle.load(open('irsis_Logistic regression classifier.pkl','rb'))
app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index1.html')

@app.route('/prediction',methods=['POST'])
def predict():
    if request.method=='POST':
        pl=request.form['pl']
        pw=request.form['pw']
        sl=request.form['sl']
        sw=request.form['sw']
        inp=[float(sl),float(sw),float(pl),float(pw)]
        n=0
        for i in range(4):
            if inp[i]<=0:
                n+=1
        
        if n==0:
            pred=model.predict([inp])
            return render_template('index1.html',prediction="predicted flower:  {}".format(pred[0]))
        else:
            return render_template('index1.html',prediction='please provide valid input')

    else:
        return render_template('index1.html')


if __name__=="__main__":
    app.run(debug=True)