


# Overview

This is a Python web project that uses Flask web framework to scrape data from Jumia and Tonaton websites, make comparisons of product before proceeding to purchasing site. The project includes two custom API files (jumia_api.py and tonaton_api.py) that make requests to the two servers, parse the response and retrieve data based on a user-defined search keyword.


### Prerequisites

-   Python 3.6
-   Flask 1.1.2
-   Requests library
-   BeautifulSoup4 library 4.9.3

### Installation

1.  Clone the repository to your local machine
1.  Navigate to the root directory of the project in your terminal or command prompt.
2.  Run `pip install -r requirements.txt` to install the required dependencies.

### Running the Application

1.  Run `export FLASK_APP=main.py` on Linux/MacOS or `set FLASK_APP=main.py` on Windows to set the FLASK_APP environment variable to the name of the main Flask application file.
2.  Run `flask run` to start the application.
3.  Open your web browser and navigate to `http://localhost:5000`


## APIs

The application uses two APIs to fetch the search results:

### Jumia API

The `jumia_api.py` file defines a `jumia` function that takes a search term as input and returns a list of dictionaries representing the search results from the Jumia website. Each dictionary contains the following keys:

-   `title`: The title of the product.
-   `price`: The price of the product.
-   `prod_link`: The link to the product page.
-   `thumbnail_link`: The link to the product image.

### Tonaton API

The `tonaton_api.py` file defines a `tonaton` function that takes a search term as input and returns a list of dictionaries representing the search results from the Tonaton website. Each dictionary contains the following keys:

-   `title`: The title of the product.
-   `price`: The price of the product.
-   `location`: The location of the seller.
-   `prod_link`: The link to the product page.
-   `thumbnail_link`: The link to the product image.


## Usage

1.  Enter a search query in the search box and click the "Search" button
2.  The application will retrieve and display up to 10 results each from Jumia and Tonaton websites based on the search query


## Authors

-   [Prince Mireku](mailto:mirekuprince66@gmail.com)

## Acknowledgments

-   [Flask documentation](https://flask.palletsprojects.com/)
-   [Requests library documentation](https://requests.readthedocs.io/en/master/)
-   [BeautifulSoup4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)