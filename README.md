# HMBooks API

HMBooks is an organizer for books at home, where sometimes we fall in love with a lot of books, buy them and have a series of problems:
  - store books in a disorganized manner along our home.
  - want to discover more category of books
  - reads a lot of books at the same time and dont remember where we left.
  - dont know which book to start reading.
  - want to remember some part of the book and share inspirations on a central place.
  - want to share an specific book

## Installation
  HMBooks requires [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) to run

  For a development environment run:  

  ```sh
  export COMPOSE_FILE="local.yml"
  $ docker-compose build
  $ docker-compose up
  ```

  For a production environment run:

  ```sh
  export COMPOSE_FILE="production.yml"
  $ docker-compose build
  $ docker-compose up
  ```  

## Process of development

  1. Similar Market
  2. Define User Journey
  3. Define Proto-Personas
  4. Define User Stories
  5. List of User Stories Mapping
  6. List of Features
  7. Tests cases


### 1. Similar Market
  - Goodreads
  - beek.io
  - .

### 2. Define User Journey
  1. A Book Lover
    -searches and buys books that wanted to read in the near future
    -every book bought its put in order of the day it was bought
    -in a future time she tries to find a book she bought around 2 years or so.
    -she search an excel with all her books and order them by year because she only remembers the story or parts of the plot.
    -she has pasted stickers on her bookshelft to easly find her books.
    -at reading time she likes taking notes of interesting quotes to later share with friends.
    -outside home she cant remember how many and which books she have, but she keeps buying interesting titles that she knows she dont have.
    -if a friend asks for a book to borrow, both coordinate a date to go to her personal library and find that book.


### 3. Define Proto-Personas
  1. Karina
    -32 years old
    -lives with her lovely cat
    -works as an artist
    -never leaves home without a novel
    -visits the bookstore once in a week.
    -she keeps up to date with the latest books of her favourite authors
    -she also read entrepreneurship and business books
    (Objectives)
    -a way to better organize her bookshelft
    -know how many books she have and which are they

  2. Luis
    -20 years old
    -lives with his parents
    -he studies computer science
    -loves reading tech books
    -started reading Machine Learning Papers
    -he keeps up to date with the latest tech with ranked books.
    -he exchange books with his friends
    (Objectives)
    -easily organize all his books and papers
    -keep a record of exchanged books with notes related.


### 4. Define User Stories 
  1. Karina
    In a pursue to read all the books that stand out by its cover, title or description, she ended up with alot of books at her personal library, there you can find different categories from novels to technical books, including financial, collection issued by newspapers editorials, even cooking recipies. Everytime she walks into her library she dont know where to start and just pick a random novel to read because she dont know exactly how many books she have, when she bought it, the reason or idea in mind that bring him to adquire it. Also from time to time she remembers that she bought a book about a certain topic but dont know exactly where she left it.

  2. Luis
    Went to a conference and listen about this new technology that he didnt know existed, instantly after the conference he start searching books about it but dont know which book to buy, he search for advice at forums and articles that point to some books. Unfortunately after buying and thenreading the top book he endup confused or even worse found that the book was too basic for him. He searches for papers within the related topic and get some concepts to research and find more books to learn, develop and take important notes to later write his blog.


### 5. List of User Stories Mapping
  - [ ] would like to look at a list of books
  - [ ] would like to add new books
  - [ ] would like a way to organize his books at the bookshelf
  - [ ] would like a way to explore all his books.
  - [ ] wants to keep the page he left reading
  - [ ] wants to keep notes and quotes about chapter, page, section. 


### 6. List of Features 
  (Must)
  - [ ] list all books
  - [ ] add new books
  - [ ] automatic generate a code for the new book (according to the bookshelft, genre and publisher)
  - [ ] sort books and group book in different ways (author, genre)
  - [ ] mark picked book for reading
  - [ ] search books by multiple criteria

  (Should) 
  - [ ] assign a note to a book
  - [ ] create family and friends groups
  - [ ] give access to our friends to search our books.
  - [ ] 

  (Nice)
  - [ ] generate a qr code for the book and find his place at bookshelf
  - [ ] real time group readings and comments
  - [ ] match books with new published books
  


### 7. Tests Cases
  1. Functional test
    (New book bought)
    -[ ] the user opens the app and see a list of all his books
    -[ ] he has bought a new book and wants to add it to his collection
    -[ ] fills all the book data and pick a place in the bookshelft
    -[ ] see his book added with the current date and a code asigned 

    (Search his books)
    -[ ] re-order his books by date, place bought, publisher, author, genre.
    -[ ] found a book and pick it from the bookshelft with the number asigned.
    -[ ] see the book marked as "reading by <username>"

    (take notes)
  2. Integration tests
  3. Unit Tests


