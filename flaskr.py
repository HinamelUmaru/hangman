from flask import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/",methods=["GET","POST"])
def odd_even():
    if request.method == "GET":
        return """
        please input integer.
        <form action="/" method = "POST"> 
        <input name="num"></input>
        </form> """
    else:
        try:
            return """
            {}　is　{}!
            <form action='/'method= "POST">
            <input name="num"></input>
            </form>""".format(str(request.form['num']),["even","odd"][int(request.form["num"])%2])
        except:
            return """
                不正な入力が行われました。
            """

@app.route("/<name>",methods=["GET","POST"])
def userpage(name):
    return render_template("userpage.html",username = name)

@app.route("/jsontest")
def index():
    return jsonify({"language":"パイソン"}),418

if __name__ == "__main__":
    app.run(debug = True,host = '0.0.0.0')

