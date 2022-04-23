from flask import Flask, render_template,request, url_for, redirect
from scrapper import FaceBookBot
from detection_model import detection
app = Flask(__name__)

@app.route("/",methods = ['GET'])
def home():
    return render_template('user_page.html')

@app.route('/about_us', methods=['GET', 'POST'])
def about_us():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('about_us.html')

@app.route('/how_it_works', methods=['GET', 'POST'])    
def how_it_works():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('how_it_works.html')


@app.route("/send_data", methods = ['POST'])
def user():
    url = request.form['postID']
    final_url = url.replace('www', 'mbasic')
    #print(url)
    #print(final_url)
    #print(postID)
    scrapper_obj = FaceBookBot()
    #final = scrapper_obj.post_content("4948996235154195",final_url)
    final = "testing purpose. Fuck you"
    # print(final)
    detection_obj = detection()
    result = detection.profanity(final)
    print("res == ",result)
    if result == True:
        return render_template('result_page.html', result = "Profanity Found in the post!!", text = final)
    else:
        return render_template('result_page.html', result = "No Profanity Found in the post!!", text = final)    
    #return render_template('result_page.html', result=result)
    
# @app.route("/result")
# def result():
#     user_obj = user()
#     print(user_obj.url)
#     return render_template('result_page.html', result="Wheeeee!")


if __name__ == '__main__':
    app.run(debug=True)
