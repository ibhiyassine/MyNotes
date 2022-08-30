# **MyNotes** : My first ever project.
### *URL* : [MyNotes](https://youtu.be/PPvzZr2_r9A)
## Description:
this project is a note-taking webapp based on HTML CSS JS and Python with Flask.
i made this project as a final project for the cs50 course which was excellent in everything, basically i took the finance PS as a model along with Trivia and made this project.
Basically it has a login page that prompts at the beginning and you have the ability to register, there's some code behind to make you registered in the database.
Then in the index you have the main page where you can create the note, and it is saved, you can access it later if you want it below.
You have the ability to full screen it and see the whole note and also can star it if it's important and it will be redricted to another window called starred; you can also delete the note, but unfortunately you can't modify iy later as i hadn't found an efficient way to make that happen (most of the time you get stuck with the outstanding loading times especially for large notes). Then you have also the ability to log out if you'd like.Also, due to Google's new policy i can't send emails using flask mail or even stmplib. Anyway, that's it for my project, i'm very proud of it and really glad i took the cs50 course.

## About the folder
* The App.py file contains the heavy lift it has a login function along with a register function a logout function (they are brand-new not to confuse with the finance ones.), also there's an index function where i can save the notes, a starred function where starred objects are saved, and also a delete function. There's also the helpers.py (to be honest i copied the login_required function and deleted the others.).

* The template folder contains all the HTML, a layout.html, a login.html, a register.html, a starred.html and index.html (their names are enough to explain their use). Which of them are specified for a certain route.

* The static folder contains some JS and CSS (there are also the bootstrap framworks for js and css) to make the website a bit more interactive, along with some svgs from bootstrap for the icons

* Finally, there's the database.db file which contains all the informations to be stored, we have a user table (from the finance project) and a note table where we find the title, note, and state which corresponds to the state of the note whether it's starred (state = 1) or not (starred = 0)

## Informations:
    My name is IBHI Ahmed Yassine
    I'm 17 from Casablanca, Morocco
    It took around a week or so to build the web-app
    I love C and Python
    I'm interested in AI and also Data Science.

## ***HOPE YOU LOVE IT!***