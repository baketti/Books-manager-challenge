# Books Management Challenge

## Project Overview

The Books Management Challenge is a CLI-based application designed to manage a library of books and authors. This project provides the ability to perform CRUD (Create, Read, Update, Delete) operations on both books and authors directly from the command line interface (CLI). The project ensures smooth data management and interaction between the CLI and a SQLite database.

## Technologies Used

The project is built using Python with the following libraries:

- SQLAlchemy: for ORM and database interaction.
- Email Validator: for validating email inputs where required.
- Flask: to serve a local API for testing purposes.
- Rich: for terminal styling, providing visually appealing CLI outputs.

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
pip install sqlalchemy email_validator flask rich
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
  - Validation Service: Provides input validation functionalities.
- app/: Contains the API logic, enabling the application to serve a local API for testing the endpoints.

- main.py: The main entry point for executing the CLI application.

## Usage Guide

Upon starting the application, you will first be prompted to decide whether to import data from CSV files. If you choose to import, the application will read data from CSV files located in the data/ directory and populate the database. Please note that if you attempt to re-import data into an existing database, you may encounter errors due to unique constraints on authors and books.

After the data import (if applicable), you will be presented with a menu to choose between the CLI application or the API service:

- CLI Application: If you choose the CLI, you will have the option to manage either books or authors. You can perform the following operations:
  - Adding new books or authors.
  - Viewing the list of all books or authors.
  - Editing existing entries.
  - Deleting books or authors from the database.
- API Service: If you choose the API service, you will be provided with the local URL for making API requests.

## API Structure

Currently, the application exposes a single endpoint:

- `bash /books`, this endpoint supports two main functionalities:
  - Retrieve all books: if no query parameters are provided, the endpoint will return all books in the database.
  - Search books by author name: if the `bash authorName` query parameter is provided, the endpoint will return books that match the specified author's name.
    The query parameter to use is authorName. For example:
    - to retrieve all books: `bash GET /books`
    - to search for books by a specific author name: `bash GET /books?authorName=<AuthorName>`

The endpoint is designed to handle query string parameters, allowing you to filter results based on the author's name.

## Contributing

Contributions are welcome! To contribute to this project:

- Fork the repository.
- Create a new branch.
- Make your changes and push them.
- Create a pull request.

## Testing

While no automated testing suite is currently implemented, manual testing can be performed by running the application, testing CRUD operations, and interacting with the API.
