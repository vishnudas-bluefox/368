# 368
A platform for common people to connect with law professionals

### Developing on going 
______________________________________________

* for run the program
## install dependencies
____

###### clone the git repo by the below command or download zip 

```
git clone https://github.com/vishnudas-bluefox/368.git
```

get in to cloned directory or extracted directory
_____

terminal users can use
```
cd 368/firstTestCase/
```
###### you need python3 and pip to run the program handle the req

create a env to run the program [Not mandatory]

```
pip install virtualenv
```
create and get in to the env

```
virtualenv venv && source venv/bin/activate
```
install all the dependencies 
```
pip install -r requirements.txt
```
## Run the backend first
____
now you have to run the backend for pyclient or js client 
so run the backend first
```
cd backend/
```
##### windows users can just use python insted of python3
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```

## Run py client
___________
go for pyclient adjust user details in [create.py](https://github.com/vishnudas-bluefox/368/blob/master/firstTestCase/pyclient/create.py) file
create as much as datas you want

```
python3 pyclient/create.py
```

for listing all the datas from our database 
```
python3 pyclient/list.py
```
for retriving specific data 
```
python3 pyclient/detail.py
```
for update the data update the wanted datas from [update.py](https://github.com/vishnudas-bluefox/368/blob/master/firstTestCase/pyclient/update.py)
you can update 
* title
* content
* if you have media you can update that too
```
python3 pyclient/update.py
```
delete the content
```
python3 pyclient/delete.py
```

## for running jsclient
_____

after runnig the backend go for the jsclient folder and open the index.html page 
you see the outputs on console 
thats it :)
