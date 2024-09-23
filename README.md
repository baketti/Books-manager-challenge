# Books Management Challenge

## Project Overview

The Books Management Challenge is an application designed to manage a library of books and authors. This project provides the ability to perform CRUD (Create, Read, Update, Delete) operations on both books and authors either directly from the command line interface (CLI) or through an exposed API with HTTP requests. The project ensures smooth data management and interaction between the CLI, API, and a SQLite database.

## Technologies Used

The project is built using Python with the following libraries:

- SQLAlchemy: for ORM and database interaction.
- Email Validator: for validating email inputs where required.
- Flask: to serve a local API for testing purposes.
- Rich: for terminal styling, providing visually appealing CLI outputs.
- InquirerPy: to enhance the user experience and simplify menu management.

## Main Features

- CRUD Operations: Manage books and authors directly from the command line, including creating, reading, updating, and deleting records.
- Data Validation: Proper validation of inputs.
- API Service: A local API served by Flask to interact with the app programmatically.
- Styled Terminal Outputs: Using the rich library to provide enhanced user interaction through styled CLI messages.
- Bulk Import from CSV: Import sets of data for books and authors directly from CSV files into the database.

## Installation Guide

To install the project locally, follow these steps:

- Clone the repository:

```bash

git clone <repository-url>
cd books-management-challenge

```

- Ensure Python is installed:
  If Python is not already installed, install it on your machine.

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Run the application: Navigate to the src directory and execute the main application file:

```bash
cd src
python main.py
```

## Project Structure

The project is structured as follows:

- cli/: This directory contains all CLI-related components and their subdirectories:

  - console/: Handles printing custom, styled messages to the terminal.
  - inputs/: Contains functions for gathering input data from the user via the CLI.
  - menu/: Functions responsible for creating the CLI menus.
  - operations/: Acts as a middle layer between the CLI and services. It processes user input, triggering the corresponding services.

- data/: Contains CSV files and the logic for extracting and importing data into the database.

- db/: Manages everything related to the SQLite database, including functions for creating the database and tables, defining table models, and implementing a singleton pattern for managing a single database connection.

- services/: This directory houses all application services, which interact with the database. Services include:

  - Books Service: Handles book-related operations.
  - Authors Service: Manages author-related operations.
  - Validation Service: Provides data validation functionalities.

- app/: Contains the API logic, enabling the application to serve a local API for testing the endpoints.
  Inside the `app` folder, there are two subfolders:
- `endpoints`:

  - `books`
  - `authors`
    which contain all the endpoints for each route.
    These two folders are further divided into `handlers`, where the functions called by the endpoints are located, and `validations`, which contains post and put data validation functions.
    `handlers` functions handle the logic when a request reaches a specific endpoint.
    Inside the `handlers` folder, the handlers are divided into four subfolders:
    - `get`
    - `post`
    - `put`
    - `delete`

- `middleware`: Contains the middleware.

- utils: Contains utility functions that are used throughout the application in more files.
- main.py: The main entry point for executing the CLI application.

In general, all directories are divided into subdirectories `books` and `authors` to separate everything related to books and authors. This structure is followed throughout the project, ensuring that each directory where operations for books and authors are needed is divided into `books` and `authors` subdirectories, containing all relevant files and functions.

## Models

The project includes two primary models: `Author` and `Book`.
These models are defined using `SQLAlchemy` and represent the core entities in the application.
Below is a detailed explanation of each model, their attributes, and the relationship between them.

### Author Model

The `Author` model represents an author entity in the database. It includes the following attributes:

- id: An integer that serves as the primary key and is auto-incremented.
- name: A unique and non-nullable string representing the author's name.
- birth_date: A nullable date representing the author's birth date.
- email: A unique and nullable string representing the author's email.

An author can have multiple books.

### Book Model

The `Book` model represents a book entity in the database. It includes the following attributes:

- id: An integer that serves as the primary key and is auto-incremented.
- title: A unique and non-nullable string representing the book's title.
- author_id: A non-nullable integer that serves as a foreign key referencing the Author model.
- pages: An integer representing the number of pages in the book.
- price: A float representing the price of the book.
- publisher: A string representing the publisher of the book.
- category: A string representing the category of the book.

Each book is associated with a single author.

### Relationship Between Author and Book

The relationship between the Author and Book models is a one-to-many relationship. This means that one author can have multiple books, but each book is associated with a single author. This relationship is defined using SQLAlchemy's relationship and ForeignKey constructs.

In the Author model, the books attribute is defined as a relationship to the Book model with back_populates="author".
In the Book model, the author attribute is defined as a relationship to the Author model with back_populates="books".
This bidirectional relationship ensures that you can easily navigate from an author to their books and from a book to its author.

### Common Methods

Both models include the following common methods:

`__init__`: Initializes the model with the provided attributes.
`__repr__`: Returns a string representation of the model instance, useful for debugging.
`to_dict`: Converts the model instance to a dictionary, which can be useful for serialization and API responses.

## Database Connection

The project uses a singleton class `DbConnection` to manage the database connection, ensuring that only one connection is established throughout the application's lifecycle. This approach helps maintain consistency and have one and only one connection.

### DbConnection Class

The `DbConnection` class is responsible for initializing and providing access to the database connection. It uses SQLAlchemy's sessionmaker to create a session bound to the engine initialized by the init_struct function.

### Key Components

- Singleton Pattern: The class ensures that only one instance of the database connection exists. This is achieved using the `__new__` method, which checks if an instance already exists before creating a new one.
- Initialization: The `_initialize_connection` class method initializes the database connection. It creates an engine using the `init_struct` function and binds it to a session. If the connection fails, it raises a RuntimeError.
- Connection Access: The `get_connection` class method provides access to the established database connection.

## Usage Guide

Upon starting the application, the database will be created inside src/db folder and you will first be prompted to decide whether to import data from CSV files. If you choose to import, the application will read data from CSV files located in the data/ directory and populate the database. Please note that if you attempt to re-import data into an existing database, you may encounter errors due to unique constraints on authors and books.

After the data import, you will be presented with a menu to choose between the CLI application or the API service:

- CLI Application: If you choose the CLI, you will have the option to manage either books or authors. You can perform the following operations:
  - Adding new books or authors.
  - Viewing the list of all books or authors.
  - Searching books by title, author name or category.
  - Searching authors by name.
  - Editing existing books or authors.
  - Deleting books or authors from the database.
- API Service: If you choose the API service, you will be provided with the local URL for making API requests.

## API Structure

The application exposes two main groups of endpoints: books and authors.

### Books Endpoints

`/books`: Supports the following functionalities:

- POST `/books`: Allows you to add a new book to the database.
- GET `/books`: If no query parameters are provided, it returns all books in the database. You can also specify a limit query parameter to return only a specified number of books from the entire collection. Additionally, you can search for books by the author's name using the authorName query parameter.
  Example:

  - To retrieve all books: GET `/books`.
  - To retrieve a limited number of books: GET `/books?limit=<number>`.
    Response:

```js
{
    "list": [
        {
            "author_id": <author_id>,
            "category": "<category>",
            "id": <book_id>,
            "pages": <number_of_pages>,
            "price": <price>,
            "publisher": "<publisher>",
            "title": "<title>"
        }
    ]
}
```

- To search for books by a specific author: GET `/books?authorName=<authorName>`
  If you search by author name, you can access returned books by `list` property, which contains an array. This consists of objects containing an `author_name` property with the author's name and a `books` property that contains all the books by that author. For Example:

```js
{
    "list": [
        {
          "author_name": "<author_name>"
          "books": [
              {
                  "author_id": <author_id>,
                  "category": "<category>",
                  "id": <book_id>,
                  "pages": <number_of_pages>,
                  "price": <price>,
                  "publisher": "<publisher>",
                  "title": "<title>"
              }
          ]
        }
    ]
}
```

    The endpoint is designed to handle query string parameters, allowing you to limit and filter results based on the author's name.

- GET `/books/<book_id>`: Returns the details of a specific book based on its book_id.
- PUT `/books/<book_id>`: Updates a specific book identified by its book_id.
- DELETE `/books/<book_id>`: Deletes a specific book identified by its book_id.

### Authors Endpoints

`/authors`: Supports the following functionalities:

- POST `/authors`: Allows you to add a new author to the database.
- GET `/authors`: Returns all authors in the database.
- GET `/authors/<author_id>`: Returns the details of a specific author based on their author_id.
- PUT `/authors/<author_id>`: Updates the information of a specific author identified by their author_id.
- DELETE `/authors/<author_id>`: Deletes a specific author identified by their author_id.

### Middleware

The application uses a middleware function that intercepts POST and PUT requests targeting the `/books` and `/authors` endpoints.
This middleware performs the following checks and actions:

- Request Body Validation: It ensures that the request body is present and in JSON format. If the body is missing, empty, or not in JSON format, the middleware returns an appropriate error message with a 400 Bad Request status.
- Data Validation: For POST requests to `/books` and `/authors`, it validates the provided data using dedicated validation functions. If the data is invalid, an error message is returned.
- Global Variable Storage: After validation, the validated data is stored in Flask's g object, making it accessible in the respective request handlers for further processing.

This middleware ensures that the data sent in requests is properly structured and valid before it reaches the core logic of the application.

## Contributing

Contributions are welcome! To contribute to this project:

- Fork the repository.
- Create a new branch.
- Make your changes and push them.
- Create a pull request.

## Testing

While no automated testing suite is currently implemented, manual testing can be performed by running the application, testing CRUD operations, and interacting with the API.

###### Thanks for reading!
