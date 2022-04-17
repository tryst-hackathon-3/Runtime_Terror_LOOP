#Initializing firestore

from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db= firestore.client()
app= Flask(__name__)

# tree= {'Details': {'Gender': 'F', 'Name': 'Aparna', 'DOB': '20/07/2001', 'Roll_No': 169, 'Email_ID': 'aparna@gmail.com', 'OverScore': 88, 'Photo': '169.png', 'AcadScore': 90, 'CoScore': 20}, 'Day': {'22/03/2022': {'Academics': {'PT3': '10', 'PT2': 9, 'PT1': 8, 'PT4': '7'}, 'Co curricular': {'Debate': 60, 'Arts': 80, 'Sports': 80, 'Singing': 10}}}, 'Courses': {'C1': {'CTR': '6', 'Time': '12000'}, 'C2': {'CTR': '7', 'Time': '8990'}},}


# db.collection('student').add(tree)
# db.collection('teacher').add({'name':'saurav', 'age':59})


# To count total number of documents
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = True))

docs = db.collection('teacher').stream()
docs= db.collection('student').get()
# doc= docs.get()
acad= {}
codb= {}
overdb= {}
for i in docs:
	temp=i.to_dict()
	acad[temp['Details']['Name']]= temp['Details']['AcadScore']
	overdb[temp['Details']['Name']]= temp['Details']['OverScore']
	codb[temp['Details']['Name']]= temp['Details']['CoScore']

    # dic[temp['Details']['AcadScore']]= temp['Details']['Name']
	# print(temp['Details']['Name'])
	# print(temp['Details']['AcadScore'])
	# print("")

# print(sort_dict_by_value(acad))
# print(sort_dict_by_value(codb))
# print(sort_dict_by_value(overdb))
# c= 0
# for doc in docs:
# 	c= c+1
# 	print(doc.to_dict())
# print(c)

@app.route('/')
def index():
    return render_template('Homepage.html')
@app.route('/Home')
def home():
    return render_template('Homepage.html')
@app.route('/leaderboard')
def lead():
	return render_template('/leaderboard/student.html')
@app.route('/studentprofile')
def StuProfile():
	return render_template('/StudentSection/profile.html')
@app.route('/student')
def stuSection():
	return render_template('/StudentSection/studentsection.html')
@app.route('/teacher')
def TeachSection():
	return render_template('/Teachersection/teacher.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/meet')
def meet():
    return render_template('meet.html')
if __name__== "__main__":
    app.run(debug=True)
