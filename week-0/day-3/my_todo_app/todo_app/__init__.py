import os

from flask import Flask
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that list my todos
	
    def todo_viewer(todo_list):
        list_is = 'My Todos are:' + '<br/>'
        for items in todo_list:
                list_is += (items + '<br/>')
        list_is += 'List end here.'
        return (list_is)
    
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print(name)
        if name == 'vaibhav':
                todo_list = ['A', 'B', 'C']
        elif name == 'shivang':
                todo_list = ['D', 'E', 'F']
        return(todo_viewer(todo_list))
    
    """@app.route('/shivang')
    def shivang():
        todo_list = ['A', 'B', 'C']
        return (
            todo_viewer(todo_list)
       )
    """
    return app

