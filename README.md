# restful-api-flask
Simple parsing data with api to database

**Usage**
```
	git clone https://github.com/robbyparlan/restful-api-flask.git
	
	cd restful-api-flask

	pip install -r requierment.txt

```

```
	import restfulApi.sql to Your Database

	mysql -u <username> -p <databasename> < <restfulApi.sql>

```

```
	change code conn = mdb.connect('HOST','USERNAME','PASSWORD','DATABASE') in restful-api-flask.py

```

**Run Program**

```
	python restful-api-flask.py

	end point 

	http://127.0.0.1:5000/api/post

		http://127.0.0.1:5000/api/get
	
			http://127.0.0.1:5000/api/put
	
				http://127.0.0.1:5000/api/delete
```