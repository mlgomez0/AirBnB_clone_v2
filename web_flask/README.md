#0x04. AirBnB clone - Web framework

## Concepts

- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions)
- How to display in HTML data from a MySQL database

## Usage

Educational purposes

## Tasks

0. 0-hello_route.py:  script that starts a Flask web application: must be listening on 0.0.0.0, port 5000,  Routes: /: display Hello HBNB!, Use the option strict_slashes=False in definition.
1. 1-hbnb_route.py: Adding to the task 0 = /hbnb: display HBNB
2. 2-c_route.py: Adding to the task 1 = /c/<text>: display C  followed by the value of the text variable (replace underscore _ symbols with a space )
3. 3-python_route.py: Adding to the task 2 = /python/(<text>): display Python , followed by the value of the text variable (replace underscore _ symbols with a space ), the default value of text is is cool.
4. 4-number_route.py: Adding to the task 3 = /number/<n>: display n is a number only if n is an integer.
5. 5-number_template.py, templates/5-number.html : Adding to the task 4 = /number_template/<n>: display a HTML page only if n is an integer, H1 tag: Number: n inside the tag BODY.
6. 6-number_odd_or_even.py, templates/6-number_odd_or_even.html: Adding to the task 5 = /number_odd_or_even/<n>: display a HTML page only if n is an integer, H1 tag: Number: n is even|odd inside the tag BODY.
7. models/engine/file_storage.py, models/engine/db_storage.py, models/state.py: update some part of our engine = models/engine/file_storage.py (Add a public method def close(self):: call reload() method for deserializing the JSON file to object), models/engine/db_storage.py (Add a public method def close(self):: call remove() method on the private session attribute (self.__session) or close() on the class Session, models/state.py(If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State).
8. web_flask/7-states_list.py, web_flask/templates/7-states_list.html: script that starts a Flask web application = web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request you must remove the current SQLAlchemy Session:
- Declare a method to handle @app.teardown_appcontext
- Call in this method storage.close()
- Routes:
--/states_list: display a HTML page: (inside the tag BODY)
--H1 tag: States
--UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
--LI tag: description of one State: <state.id>: <B><state.name></B>.
9. web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html: Adding to task 8 = Routes:
- /cities_by_states: display a HTML page: (inside the tag BODY)
- H1 tag: States
- UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
- LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
- LI tag: description of one City: <city.id>: <B><city.name></B>
10. web_flask/9-states.py, web_flask/templates/9-states.html: Adding to the task 9 = Routes:
 /states: display a HTML page: (inside the tag BODY)
- H1 tag: States
- UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
- LI tag: description of one State: <state.id>: <B><state.name></B>
/states/<id>: display a HTML page: (inside the tag BODY)
- If a State object is found with this id:
- H1 tag: State:
- H3 tag: Cities:
- UL tag: with the list of City objects linked to the State sorted by name (A->Z)
- LI tag: description of one City: <city.id>: <B><city.name></B>
Otherwise:
- H1 tag: Not found!
11. web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/: Adding to the task 10 = Routes:
/hbnb_filters: display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static
- copy_files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles
- Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images
- Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.
- Use 6-index.html content as source code for the template 10-hbnb_filters.html:
- Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;
- State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)
