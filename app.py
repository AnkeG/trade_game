from flask import Flask, flash, session, redirect, url_for, request, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
	session['total_value'] = 1000
	session['numofgold'] = 0
	session['rounds'] = 0
	return redirect(url_for('game'))

@app.route("/game", methods=['GET','POST'])
def game():
	total_value = session.get('total_value')
	numofgold = session.get('numofgold')
	rounds = session.get('rounds')
	error = None
	
	if total_value < 30 and numofgold == 0:
		return render_template("over.html")
	if total_value >1000000:
		return render_template("win.html")
	
	if request.method == 'GET':
		goldprice = random.randint(30,70)
		rounds += 1
		session['goldprice'] = goldprice
		session['rounds'] = rounds
		return render_template("trade.html", goldprice = goldprice, total_value = total_value, numofgold = numofgold, rounds = rounds)
	else:
		goldprice = session['goldprice']
		numofgold_buy = request.form['numofgold_buy']
		numofgold_sell = request.form['numofgold_sell']
		
		if not numofgold_buy:
			numofgold_buy = 0
		else:
			numofgold_buy = int(numofgold_buy)
			if numofgold_buy*goldprice > total_value:
				error = 'Not enough money.'
		
		if not numofgold_sell:
			numofgold_sell = 0
		else:
			numofgold_sell = int(numofgold_sell)
			if numofgold_sell > numofgold:
				error = "Not enough gold."
				
		if not error:	
			session['total_value'] = total_value- numofgold_buy * goldprice + numofgold_sell * goldprice
			session['numofgold'] = numofgold + numofgold_buy - numofgold_sell		
		else:
			flash(error)
			return render_template("trade.html", goldprice = goldprice, total_value = total_value, numofgold = numofgold, rounds = rounds)
		
		return redirect(url_for('game'))

app.secret_key = 'FUDHAUGFHSDJKIUH'
		
if __name__ == '__main__':
	app.run()