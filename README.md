# todos
Todo App in Python and Next.js


## How to run locally

### Prerequisites
- Installed [Docker](https://www.docker.com/)

> #### *NOTE*:
>
> *The project is set up to run in development mode.
> That means that any live changes to the code will 
> automatically reflect in a running instance*


### Steps

1. Clone the project 
    ```sh
    git clone git@github.com:IlliaChalyk/todos.git
    ```

2. cd into the todos folder
    ```sh
    cd todos
    ```
3. Copy `.env.example` and rename it to `.env`. *For local setup, default values in the example file should be satisfactory*

4. Run docker compose
    ```sh
    docker compose up -d
    ```

5. To stop the project run
    ```sh
    docker compose down
    ```
