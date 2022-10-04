from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
#app.config['MAIL_SERVER']='smtp.correo.yahoo.es'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'flask052022@gmail.com'
app.config['MAIL_PASSWORD'] = '3147981025'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# ruta de la pagina principal
@app.route("/")
def index():
	return render_template("index.html")

# ruta de la pagina de contacto
@app.route("/contact", methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		try:
			msg = Message(request.form["asunto"], sender=request.form["email"], recipients=["flask052022@gmail.com"])
			# msg.body = """
			# De: {} <{}>
			# {}
			# """.format(request.form["nombre"], request.form["email"], request.form["mensaje"])
			msg.body = request.form["texto"]
			mail.send(msg)
			print("Mensaje enviado")
			return redirect(url_for("contact"))
		except Exception as e:
			print(e)
			return "Error al enviar el mensaje"
	# msg = Message("hola", sender=request.form["email"], recipients=["flask052022@gmail.com"])
	# 	# msg.body = """
	# 		# De: {} <{}>
	# 		# {}
	# 		# """.format(request.form["nombre"], request.form["email"], request.form["mensaje"])
	# msg.body = request.form["texto"]
	# mail.send(msg)
	# print("Mensaje enviado")
	# return redirect(url_for("index"))
	print("Mensaje no enviado")
	return redirect(url_for("index"))

@app.route("/contacta" , methods=["POST"])
def hola():
	print("Hola mundo")
	try:
		msg = Message(request.form["asunto"], sender=request.form["email"], recipients=["flask052022@gmail.com"])
			# msg.body = """
			# De: {} <{}>
			# {}
			# """.format(request.form["nombre"], request.form["email"], request.form["mensaje"])
		msg.body = request.form["texto"]
		mail.send(msg)
		return redirect(url_for("contact"))
	except:
		return "Error al enviar el mensaje"
	# msg = Message("saludo", sender="juankruiz27@gmail.com", recipients=["flask052022@gmail.com"])
	# 	# msg.body = """
	# 		# De: {} <{}>
	# 		# {}
	# 		# """.format(request.form["nombre"], request.form["email"], request.form["mensaje"])
	# msg.body = "Hola te hablo desde Flask"
	# mail.send(msg)
	return redirect(url_for("contact"))

if __name__ == "__main__":
	app.run(debug=True , port=5000)