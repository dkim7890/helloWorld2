from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/favourite-course')
def favourite_course():  # put application's code here
    course = request.args.get('course')
    course_number = request.args.get('course_number')
    return render_template(
'favourite-course.html',
                    course = course,
                    course_number = course_number)

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        class_year = request.form.get('class_year')

        return render_template(
            'contact.html',
            submitted = True,
            first_name = first_name,
            last_name = last_name,
            email = email,
            class_year = class_year
        )

    return render_template('contact.html', submitted=False)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('about-css.html')

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello2.html')

if __name__ == '__main__':
    app.run()
