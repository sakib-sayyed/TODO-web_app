# Flask Todo Web App
This is a simple web application built using Flask, a lightweight Python web framework, to manage your todo list. With this app, users can easily add, update, delete, and mark tasks as completed. The app utilizes SQLAlchemy to interact with a SQLite database to store todo items efficiently.

## Features
1. **Add Task**: Users can add new tasks with a title and description.
2. **Update Task**: Existing tasks can be updated with new titles and descriptions.
3. **Delete Task**: Users can delete tasks they no longer need.
4. **Mark Task as Completed**: Tasks can be marked as completed when done.
5. **Timezone Support**: The app supports displaying task creation time in the local time zone (IST - Indian Standard Time).

## Technologies Used
* Flask: Flask is used as the web framework to handle HTTP requests and responses.
* SQLAlchemy: SQLAlchemy is utilized as an ORM (Object-Relational Mapping) to interact with the SQLite database.
* Datetime: Datetime module is used to handle timestamps for task creation.
* Pytz: Pytz library is used to handle timezones, specifically to display task creation time in the local time zone (IST).


## Getting Started
1. Clone the repository to your local machine.
2. Install the required dependencies listed in requirements.txt.
3. Run the Flask app using python app.py.
4. Open your web browser and navigate to http://localhost:5000 to access the application.


## Usage
* Upon accessing the application, users will see their todo list.
* To add a new task, click on the "Add Task" button and fill in the title and description.
* To update an existing task, click on the task title, make necessary changes, and click "Update".
* To delete a task, click on the "Delete" button next to the task.
* To mark a task as completed, click on the "Complete" button next to the task.


## Contributions
Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.
