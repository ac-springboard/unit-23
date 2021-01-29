## IMPORTANT: this is still a WORK IN PROGRESS. The final version will be published as soon as possible.

# Flask Blogly

<p>A blog app created from scratch!</p>

-----
#### 1 - Manually Create the Database and Schemas

The ***Flask Blogly*** app uses the PostgreSQL database.
You can configure it to use any database and schema names to use with it.
The only requirement is that you ***MUST*** inform these names to the application via environment variables.

<p>Please, see the next section for details.</p>

-----
#### 2 - Set the Environment Variables

You ***MUST*** configure the following environtment variables:

| VARIABLE | VALUES |DESCRIPTION |
| :--- | :--- | :--- |
|  **BLOGLY_DATABASE_NAME** | Name of the database   | - |
|  **BLOGLY_SCHEMA_NAME** |  Name of the schema | - |
|  **BLOGLY_INIT** |  True or False  | If 'True' the tables will be dropped and recreated  |
|  **BLOGLY_SEED** |  True or False  | If 'True' some data will be inserted into the tables  |

This feature is very useful in several different scenarios. For example:

- To run the app for testing purposes:
```
export BLOGLY_DATABASE_NAME=QA_DB
export BLOGLY_SCHEMA_NAME=QA_SCHEMA
export BLOGLY_INIT=True
export BLOGLY_SEED=True
```
- To run the app on the production environment:
```
export BLOGLY_DATABASE_NAME=PROD_DB
export BLOGLY_SCHEMA_NAME=PROD_SCHEMA
export BLOGLY_INIT=False
export BLOGLY_SEED=False
```

-----
#### 3 - Install the Required Packages

```
pip install -r requirements.txt
```

You can check the `requirements.txt` file on this page. 

-----
#### 4 - Run the Application Using Flask

Remember that this is a ***Flask*** application. You ***MUST*** use the `Flask` command to run it:

```
Flask run
``` 

The file [run.sh](https://github.com/ac-springboard/unit-23/blob/master/23.1/exercise/flask-blogly/run.sh) is a convenient way to configure and run the application.

-----
#### 5 - Navigation Flow

![Navigation Flow](https://raw.githubusercontent.com/ac-springboard/unit-23/master/23.3/exercise/docs/blogly-navigation-v2.jpg)

-----
#### Additional Notes

1 - The documentation and tests will be completed during this unit (Unit 23)

2 - The styling is far from completed. It's formatted for test purposes only.

3 - I've used some techniques ***beyond the scope of the exercises***, such as:

- ***Multiple Inheritance***.
- ***Generics***.
- **Blueprint** architecture.
- Using multiples schemas in the same or separated database.
- Parametrizing the database and schema names.
- `@staticmethod` annotation.
- Others.

4 - The decision about using this architecture since the beginning was made due the fact that I intend to develop a professional blog for myself as my capstone project. I'm strongly tempted to use the microservices architecture for that so I can continue practicing ohter development languages and some dev-ops skills.


