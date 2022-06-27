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
	user = users.get_by_id(request.json['user_name'])
	return user


# Find
def find():
	user_id = users.get(role="admin")
	user = users.get_by_id(user_id)


# Find ALL
def find():
	array = users.get(role="admin", all=True)
	for i in array:
		user = users.get_by_id(i)


# GET ALL DATA
def get_all_data():
	return users.data


# DELETE
def delete():
	users.delete(request.json['user_name'])


# EDIT
def edit():
	user = users.get_by_id(request.json['user_name'])
	user['role'] = 'admin'
	users.save()


# Check if already exists
if users.get_by_id(request.json['user_name']):
	return "user already exists"
