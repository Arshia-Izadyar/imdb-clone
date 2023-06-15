# imdb-clone


This is a IMDB clone with django 😁

## authentication 🔐

allauth used for authentication

2 step verification with your email is necessary

you can reset password with your Email

you can signup/login with GITHUB account or your GOOGLE account

## How site works (just like IMDB LOL) 🤔

you can add movies to your watch-list and get access to them through your profile page

rate movies and movie rate will update to average rate with one decimal filed like : "45.5"

you can add comments or read other people comments for a movie

if you dont see your favorite movie you can create it but movie titles are uniqe

## Database 👀

postgresql was used as a Database

Models : CommentModel, RatingModel, MovieModel, WatchListModel

## Problems 🥲
i had to deal with N+1 problem for my query but with prefetch_related i fixed it

and adding allauth was a new and fun challenge


