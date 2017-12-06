from flask import Flask, request
import spider, send_email

app = Flask(__name__)
html = '''
    <!DOCTYPE html>
    <title>Ezot</title>
    <h1>EZot register</h1>
    <h5>via Entropy Xu</h5>
    <form method=post enctype=multipart/form-data>
         <p>Email:<input type="text" name="email"/></p>
         <p>Course Number:<input type="text" name="course-number"/></p>
         <input type=submit value=Confirm>
    </form>
    '''


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form["email"]
        course_num = request.form["course-number"]
        status = spider.get_course_status(course_num)
        if status == "OPEN" or status == "Waitl":
            return "<h1>The status of the class is " + status + \
                   "<br>You can choose directly!</h1>"
        return "<h1>The status of the class is " + status + \
               "<br>We will send you a email if there is a position</h1>"

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
