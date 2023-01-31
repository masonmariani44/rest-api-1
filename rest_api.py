#! /usr/bin/python3

import os
import sys
import json
import cgi


''' (this is the data dictionary, stored in the backing file as json)

{
	"students": [
		{
			"id": 1,
			"name": "name1",
			"courses": [
				"string1",
				"string2",
				...
			]
		},
		{
			"id": 2,
			"name": "name2",
			"courses": [
				"string1",
				"string2",
				...
			]
		},
		{
			...
		}
	],
	"courses": [
		{
			"id": 1234
		},
		{
			"id": 5678
		},
		{
			...
		}
	]
}

'''

def error_400():
	print("400 Bad Request")
	print()
	sys.exit(0)

def error_404():
	print("Status: 404 Not Found")
	print()
	sys.exit(0)

def get_all_students(data):
	#generate link TODO

	#print out students from data dictionary
	print("Status: 200 OK")
	print("Content-Type: text/html")
	print()
	students = data["students"]
	print(json.dumps(students, indent=2))

def post_new_student():
	return

def get_all_courses(data):
	#TODO generate link

	#print out courses from data dictionary
	print("Status: 200 OK")
	print("Content-Type: text/html")
	print()
	courses = data["courses"]
	print(json.dumps(courses, indent=2))

def post_new_course():
	return

def get_student_atID(data, stdID):
	#generate link TODO

	found = None
	for i in data["students"]:
		if i["id"] = stdID:
			found = i
			break

	if found = None:
		error_404()
	else:
	#print out student from data dictionary with this id
	print("Status: 200 OK")
	print("Content-Type: text/html")
	print()
	print(json.dumps(i, indent=2))

def put_update_student_atID():
	return

def delete_student_atID():
	return

def post_update_student_courses_atID():
	return

def main():
	#open backing storage file: "file"
	with open("/BACKING_STORE") as file:
		data = json.loads(file.read())

	#setup path info
	if "PATH_INFO" not in os.environ or os.environ["PATH_INFO"] == "/":
		path = []
		error_404()
	else:
		path = os.environ["PATH_INFO"].split("/")

	#sets the request method used
	method = os.environ["REQUEST_METHOD"]

	#conditions for each branch
	if len(path) == 1:
		if path[0] == "students":
			if method == "GET":
				get_all_students(data)
			if method == "POST":
				post_new_student()
			else:
				error_400()
		elif path[0] == "courses":
			if method == "GET":
				get_all_courses()
			if method == "POST":
				post_new_course()
		else:
			error_404()

		#add return or condition if not students or courses

	if len(path) == 2:
		if path[0] == "students":
			if method == "GET":
				get_student_atID(data, int(path[1]))
			if method == "PUT":
				put_update_student_atID()
			if method == "DELETE":
				delete_student_atID()
			else:
				error_400()
		elif path[0] == "courses":
			if method == "DELETE":
				delete_course_atID()
			else:
				error_400()
		else:
			error_404()

		#add return or condition if not students or courses

	if len(path) == 3:
		if path[0] == "students":
			if method == "POST":
				post_update_student_courses_atID()
			else:
				error_400()
		else:
			error_404()











def get():
	if "PATH_INFO" not in os.environ or os.environ["PATH_INFO"] == "/":
		print("Status: 200 OK")
		print("Content-Type: text/html")
		print()
		print(json.dumps(data, indent=2))
	else:
		key = os.environ["PATH_INFO"].split("/")[1]

		found = None
		for rec in data:
			if rec["id"] == key:
				found = rec
				break

		if found is None:
			print("Status: 404 Not Found")
			print()
		else:
			print("Status: 200 OK")
			print("Content-Type: text/html")
			print()
			print(json.dumps(found, indent=2))

def post():
	new_rec = json.loads(sys.stdin.read())

	if "id" not in new_rec or type(new_rec["id"]) != str or "name" not in new_rec or type(new_rec["name"]) != str or "credits" not in new_rec or type(new_rec["credits"]) != int or "prereqs" not in new_rec or type(new_rec["prereqs"]) != list:
		print("400 Bad Request")
		print()

	else:
		new_rec_filtered = {"id" : new_rec["id"], "name" : new_rec["name"], "credits" : new_rec["credits"], "prereqs" : new_rec["prereqs"]}
		data.append(new_rec_filtered)

		with open("/BACKING_STORE", "w") as file:
			file.write(json.dumps(data, indent=2))

			print("300 Redirect")
			print("Location: /cgi-bin/destination")###given destination for redirect###
			print()

def delete():
	#take backing file data, get associated collection, and delete the proper entry from it


if os.environ["REQUEST_METHOD"] == "GET":
	get()
if os.environ["REQUEST_METHOD"] == "POST":
	post()
else:
	delete()