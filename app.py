from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/prediction_result_DBS",methods=["GET, "POST"])
def prediction_result_DBS():
return(render_template("prediction_DBS.html"))

                                    
                                      


if __name__ == "__main__":
    app.run()
    


