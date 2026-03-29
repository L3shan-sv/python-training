from flask import Flask
app =(__name__)

app.route("/")
def home():
    return"leshan is active tonight"

if __name__=="__main__":
    app.run(debug=True)

