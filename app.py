from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Climat & Cultures - Le back-end Flask fonctionne !"

if __name__ == "__main__":
    app.run(debug=True)