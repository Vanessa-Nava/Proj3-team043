
# main py file to run flask
from flask import Flask, render_template, request, redirect, url_for # imports libraries for flask web development
import os # library for system functions
import smtplib # library for email rendering

app = Flask(__name__) # initializes app

class User_info(): # globally saved variables
    email = ""
    website = []
    final = []
    message = ""

x = User_info() # sets the info class to the variable x

#Homepage#######################################
@app.route('/') # homepage route
def home():
    return render_template("home.html") # renders homepage
@app.route('/', methods=['POST'])
def home_process(): # function that processes POST method
    x.email = request.form['user_email'] # grabs inputted user email and saves it to class variable "email"
    return redirect(url_for('feature', user_email=x.email)) # passes email into following "feature" template

#Feature########################################
@app.route('/feature') # feature route
def feature(): # renders feature
    values = {'user_email': x.email} # creates a dictionary of variables
    return render_template("feature.html", values=values) # renders feature template with values passed

#Phone########################################
@app.route('/phone') # monitor phase
def phone(): # renders interface HTML
    return render_template("interface.html")

@app.route('/phone', methods=["POST"])
def saving(): # process POST method
    if 'website' in request.form: # if the request.form has name variable 'website'
        website = request.form['website'] # request website
        x.website.append(website) # append to website list
    return render_template("interface.html")

#Thank You######################################
@app.route('/thank_you') # thank you route
def thank_you(): # sets up thank you page
    website = "\n".join(x.website)
    saved = "****PAST EVENT(S)**** \n" + website
    endmessage = "\nThank you for using iCry!"
    final_message = saved + endmessage
    # email portion
    server = smtplib.SMTP('smtp.gmail.com', 587) # sets enail server
    server.starttls() # starts server access
    server.login("proj.team43@gmail.com", "Teamproject43") # inputs team created email
    msg = final_message # sets string message to a variable
    server.sendmail("proj.team43@gmail.com", x.email, msg) # sends to specified user email
    server.quit() # ends server access
    return render_template("thank_you.html", user_email=x.email) # renders thank you template
    
# @app.route('/twilio')
# def send_msg():
    # account_sid = "AC8a495350c7f9c0655ca72f93a70eae5b"
    # auth_token = "5cdf40662be1da758c675e5badde473f"
    # client = TwilioRestClient(account_sid, auth_token)
    # # replace "to" and "from_" with real numbers
    # rv = client.messages.create(to="+18319179997",
    # from_="+18312010701",
    # body="CSSIx is the best!")
    # self.response.write(str(rv))
    
#Checking if run from user######################
if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv("IP", "0.0.0.0"),
        debug=True
        )