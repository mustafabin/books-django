[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Django Book API

Use Django and the Django REST Framework to build an API of books.

## Prerequisites

- Django
- Django REST Framework

## Instructions

1.  Fork and clone this repository.
1.  Change into the new directory.
1.  Set up a virtual environment and install dependencies.
1.  Fulfill the listed requirements.

Please turn in your submission by the deadline on your cohort calendar.

## Requirements

### Part 1: Setup

Create a new Django project and app. Define a `Book` model and create a few
instances through the admin interface.

Don't forget to create a new database and user in Postgres!

Install the `djangorestframework` module for the next section.

### Part 2: Build the Model and Serializer

Define
a [`ModelSerializer`](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)
for your Book Model.

> Note: Do not use the `HyperlinkedModelSerializer` serializer. That serializer
> is for linked models. Here we have just a plain model.

### Part 3: Views and URLS

Once you have your model and serializer in place, use the [generic
views](https://www.django-rest-framework.org/api-guide/generic-views/) to create
your views and URLs.

Make it so you can perform full CRUD on your Book model (without needing to be
logged in).

## Bonus

Implement one of the following as a bonus. When you finish, implement the rest!

* [Validation](https://www.django-rest-framework.org/api-guide/validators/)
* [Throttling](https://www.django-rest-framework.org/api-guide/throttling/)
* [Pagination](https://www.django-rest-framework.org/api-guide/pagination/)
* [Filtering](https://www.django-rest-framework.org/api-guide/filtering/)

## [License](LICENSE)

1.  All content is licensed under a CC­BY­NC­SA 4.0 license.
1.  All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
