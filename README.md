# Leisure travel planning
#### Video Demo: https://youtu.be/1fPlF3JK00M
#### Description:

###### My final project is a web-based application to plan trips

###### The languages that are used to make the project are python, html and sql to the db

###### the index.html contains cards of the trips that you have planned, and also a button to add a new trip, each card the trip title, the start date (the one that the user inputs when he adds the trip) and a button to see the trip "See trip"

###### the apology.html is when something has gone wrong, the login.html is for you to do your login and the register.html is for you to register they are like the finance pset

###### the trip.html is a table with the item/days planned to your trip, every trip has its own plan table, it is based on the user id, and has a button to add the an item, every item is required to have a date, and you can choose to add hotel, restaurant, place to vistit, and some notes that can be useful to the trip later, like price of the gasoline, or how many kilometeres or miles you are going to drive

###### when i try to add a trip that already exists with the same name and the same date, it shows me the apology image that the trip is already created, when i try to create a user that the username is already taken it also shows me the apology, also when i dont put the right passwords and etc

###### you can register as many users as you want, each user has its trips and he only can see them, when get does the log in

###### the helpers.py has some functions that are called into the app.py that are helpful like the login_required tha verifies if a user is logged, so no page in the app can be accessed by someone who is not logged except fot the login and register page

###### the app.py is what makes everything work, it has all the functions to add your items and to add your trips, to log you in, log you out, to see the index that has your trips and etc

###### there is the travel_planning.db that is the database that have all the informations, it has 3 tables in it the users, trips and plans they are linked at each other to know what trip belongs to what user and what item belongs to a trip

###### the user table has an id, username and hash to the password, the trip table has an id, an user_id, title and date fields, and the plan table has a trip_id an id, date, tourist_place, restaurant, hotel and note fields

###### you can run the application with flask run

###### This web-based application is useful for everyone that wants to have a safe trip and plan everything before, the ideia came because, before every trip that i make with my family, we always plan all the details and its always wonderful, but we use the Google Sheets to plan it, so i thought that a app would be a great ideia

