from PySimpleDB import DataBase
users = DataBase("database/users.bd", unique="user")


# ADD
def add():
	users.add(  user=request.json['user_name'],
				password=request.json['password'],
				registration_time=time.time(),
				role="admin")


# GET
def get():
	user = users.get(request.json['user_name'])
	return user


# Find
def find():
	user_id = users.find(role="admin")
	user = users.get(user_id)


# Find ALL
def find():
	array = users.find_all(role="admin")
	for i in array:
		user = users.get(i)


# GET ALL DATA
def get_all_data():
	return users.data


# DELETE
def delete():
	users.delete(request.json['user_name'])


# EDIT
def edit():
	user = users.get(request.json['user_name'])
	user['role'] = 'admin'
	users.save()


# Check if already exists
if users.get(request.json['user_name']):
	return "user already exists"
