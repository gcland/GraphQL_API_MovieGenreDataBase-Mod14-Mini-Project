Welcome to GraphQL_API_MovieGenreDataBase: A python Graphene, Flask, SqlAlchemy API project by Grant Copeland

First, you need to clone down the project using this command here:

git clone git@github.com:gcland/GraphQL_API_MovieGenreDataBase-Mod14-Mini-Project.git

This project is centered around graphQL. We will be creating graphQL queries / mutations in GraphiQL after initializing our database and files.

Next, enter the following commands into the terminal:

    python3 -m venv myenv (if using mac, 'python -m venv venv' if using windows)
    source myenv/bin/activate
    pip install Flask Flask-Script Flask-SQLAlchemy Flask-GraphQL graphene graphene-sqlalchemy PyMySQL cryptography

Then, make sure your interpretter is in the virtual environment we just created:

    cmd + shift + p (mac) -> select virtual environment

This project uses MySQL and Postman to operate the functions. Start MySQL and enter the following command:

CREATE DATABASE movies_db;

Begin by opening the project folder. Within the 'password.py' file, enter your MySQL password. Save the file.

Next, you will need to create the routes to communicate with the database. You will need to create these routes in GraphiQL and NOT Postman (Postman does not allow list entry for genres into movies). 
Run the 'app.py' file and open the localhost url: http://127.0.0.1:5000. 
GraphiQL is set to run on the localhost url + /graphql. The url is http://127.0.0.1:5000/graphql.

This project contains a database of movies and genres where the genres are defined by an id and a name. 
Movies are defined by an id, title, description, release year, and a list of genres. Thus, the relationship between movies and genres is many-to-many. 
For this project, four queries and six mutations are available. 
The queries are:
1. Get all genres - Returns a list of all genres
2. Get all movies - Returns a list of all movies
3. Find a genre by id - Returns a genre by id entered and can display all movies associated with that genre within the movie's internal genre list.
4. Find a movie by id - Returns a movie by id entered and displays all genres associated with the movie

The mutations are:
1. Create genre - creates a genre (enter name, id autoincrements)
2. Update genre by id - updates details of a genre
3. Delete genre by id - deletes a genre from the database
4. Create movie - creates a movie (enter title, description, release year, and list of genres, id autoincrements)
5. Update genre by id - updates details of a movie
6. Delete genre by id - deletes a movie from the database

Begin by creating at least one genre. Then create a movie and add the genre(s) to the movie. From here view, create, update, or delete genre(s) or movie(s).
For your convenience below is the formatted code to input into GraphiQL for all queries / mutations. 

Enjoy and thanks for viewing this project!
- Grant

# Queries:

    query Genres {
        genres {
            id
            name
            genres {
                id
                title
                description
                releaseYear
            }
        }
    }
    
    query FindGenre {
        findGenre(genreId: 1) {
            id
            name
            genres {
                id
                title
                description
                releaseYear
            }
        }
    }
    
    query Movies {
        movies {
            id
            title
            description
            releaseYear
            genres {
                id
                name
            }
        }
    }
    
    query FindMovie {
        findMovie(movieId: 1) {
            id
            title
            description
            releaseYear
            genres {
                id
                name
            }
        }
    }

# Mutations

    mutation CreateGenre {
      createGenre(name: "Romance") {
          genre {
              id
              name
          }
      }
    }
    
    mutation UpdateGenre {
      updateGenre(id: 1, name: "Comedy") {
          genre {
              id
              name
          }
      }
    }
    
    mutation DeleteGenre {
      deleteGenre(id: 1) {
          genre {
              id
              name
          }
      }
    }
    
    mutation CreateMovie {
      createMovie(description: "A thrilling action movie.", releaseYear: 2024, title: "Mission Impossible", genres: [1, 2]) {
          movie {
              id
              title
              description
              releaseYear
              genres {
                  id
                  name
              }
          }
      }
    }
    
    mutation UpdateMovie {
      updateMovie(
          description: "A thrilling action movie."
          id: 1
          releaseYear: 2024
          title: "Mission Impossible 10293"
          genres: [1]
      ) {
          movie {
              id
              title
              description
              releaseYear
              genres {
                  id
                  name
              }
          }
      }
    }
    
    mutation DeleteMovie {
      deleteMovie(id: 2) {
          movie {
              id
              title
              description
              releaseYear
              genres {
                  id
                  name
              }
          }
      }
    }
     
    
    
