# Django Q&A Platform

This is a Django-based Q&A platform that allows users to ask and answer questions on various topics.

## Features
- User registration and authentication
- User profiles with avatar images
- Asking and answering questions
- Upvoting and downvoting questions and answers
- Tagging questions with topics
- Searching questions and answers by keywords and tags
- Sorting questions and answers by date and popularity
- Commenting on questions and answers
- Marking questions as answered
- Following and unfollowing questions and topics
- Notifications for new answers and comments
- Admin panel for managing users, questions, answers, and tags

## Installation

- Clone the repository:

```
git clone git@github.com:dyussenov/django-blog.git
```

- Install the dependencies:

```
pip install -r requirements.txt
```

- Apply the database migrations:

```
python manage.py migrate
```

- Create a superuser:

```
python manage.py createsuperuser
```

- Run the development server:

```
python manage.py runserver
```

## Usage
- Register a new user or log in with an existing one.
- Ask a question by clicking on the "Ask a question" button.
- Answer a question by clicking on the "Answer" button below the question.
- Upvote or downvote a question or answer by clicking on the arrow icons.
- Tag a question with one or more topics by typing them in the "Tags" field.
- Search for questions and answers by entering keywords in the search bar or clicking on a tag.
- Sort questions and answers by date or popularity using the dropdown menu.
- Comment on a question or answer by clicking on the "Comment" button below it.
- Mark a question as answered by clicking on the "Mark as answered" button below the accepted answer.
- Follow or unfollow a question or topic by clicking on the "Follow" or "Unfollow" button.
- Receive notifications for new answers and comments in the notifications panel.
- Manage users, questions, answers, and tags in the admin panel at http://localhost:8000/admin/.

## Contributing

If you want to contribute to this project, please follow these steps:

Fork the repository.
- Create a new branch with your changes: ```git checkout -b my-feature-branch```
- Make your changes and commit them: git commit -am 'Add new feature'
- Push the branch to your fork: git push origin my-feature-branch
- Create a pull request against the main branch of the original repository.
- Wait for the code review and merge approval.

## License

This project is licensed under the MIT License - see the LICENSE file for details.