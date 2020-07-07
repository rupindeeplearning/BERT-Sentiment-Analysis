#!python3
#orca
from flask import Flask, render_template, request
import ktrain
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    op_sent=''
    if request.method=='POST' and 'sentiment' in request.form:
        sentiment = request.form.get('sentiment')
        op_sent = sentiment_analyse(sentiment)
    return render_template("index.html",op_sent=op_sent)

def sentiment_analyse(sentiment):
    predictor = ktrain.load_predictor('sentiment_predictor')
    op = predictor.predict(sentiment)
    if op[0]=='pos':
        return 'positive'
    else:
        return 'negative'
    
app.run()    