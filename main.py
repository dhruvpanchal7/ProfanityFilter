from flask import Flask, render_template,request
from scrapper import FaceBookBot
app = Flask(__name__)

@app.route("/",methods = ['GET'])
def home():
    return render_template('user_page.html')


@app.route("/send_data", methods = ['POST'])
def user():
    url = request.form['postID']
    #print(postID)
    class_obj = FaceBookBot()
    class_obj.post_content("4948996235154195",url)
    return "completed"

@app.route("/result")
def result():
    return render_template('result_page.html', result="Wheeeee!")


if __name__ == '__main__':
    app.run(debug=True)