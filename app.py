from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import MySQLdb as mdb

app = Flask(__name__)

api = Api(app)

data = []


class AddHandler(Resource):
	def post(self):
		data = request.get_json()
		conn = mdb.connect('localhost','brunello','bonanni','sampledb')
		cur = conn.cursor()
		sql = "INSERT INTO `user`(`user_id`,`username`,`password`,`email`) VALUES ('%s','%s','%s','%s')" % (data['user_id'],data['username'],data['password'],data['email'])
		try:
			cur.execute(sql)
			conn.commit()


		finally:
			conn.close()

		return jsonify(data)


class GetHandler(Resource):
	def get(self):
	    return "Prova di trasmissione"
		#data = request.get_json()
		#conn = mdb.connect('localhost','brunello','bonanni','sampledb')
		#cur = conn.cursor()
		#try:
		###	sql = "SELECT * from `user` WHERE `user_id` = '%s'" % (data['user_id'])
		#	cur.execute(sql)
		##	user = cur.fetchone()
		#	return jsonify(user)
		#finally:
		#	conn.close()


class PutHandler(Resource):
	def put(self):
		data = request.get_json()
		conn = mdb.connect('localhost','root','1105boty','restfulApi')
		cur = conn.cursor()
		try:
			sql = "UPDATE user SET username = '%s' WHERE `user_id` = '%s'" % (data['username'],data['user_id'])
			cur.execute(sql)
			conn.commit()

		finally:
			conn.close()

		return jsonify(data)

class DelHandler(Resource):
	def delete(self):
		data = request.get_json()
		conn = mdb.connect('localhost','root','1105boty','restfulApi')
		cur = conn.cursor()
		try:
			sql = "DELETE FROM `user` WHERE `user_id` = '%s'" % (data['user_id'])
			cur.execute(sql)
			conn.commit()

		finally:
			conn.close()

		return "Success Delete "




api.add_resource(AddHandler, "/api/post")
api.add_resource(GetHandler, "/api/get")
api.add_resource(PutHandler, "/api/put")
api.add_resource(DelHandler, '/api/delete')


@app.route('/masks', methods=['GET'])
def get_masks():
    #return "Prova di trasmissione"
    data = request.get_json()
    conn = mdb.connect('localhost','brunello','bonanni','sampledb')
    cur = conn.cursor()

    try:
	sql = "SELECT * from `user` WHERE `user_id` = '%s'" % (data['user_id'])
	cur.execute(sql)
	user = cur.fetchone()
        return jsonify(user)

    finally:
	conn.close()




if __name__ == '__main__':
	app.run(debug=True)
