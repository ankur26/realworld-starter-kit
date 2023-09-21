# ![RealWorld Example App](logo.png)

> ### [Sanic](https://sanic.dev/en/) codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld) spec and API.


### [Demo](https://demo.realworld.io/)&nbsp;&nbsp;&nbsp;&nbsp;[RealWorld](https://github.com/gothinkster/realworld) (Work in progress, these are the original links)


This codebase was created to demonstrate a fully fledged fullstack application built with **Sanic** including CRUD operations, authentication, routing, pagination, and more.

We've gone to great lengths to adhere to the **Sanic** community styleguides & best practices.

For more information on how to this works with other frontends/backends, head over to the [RealWorld](https://github.com/gothinkster/realworld) repo.


# How it works

> Describe the general architecture of your app here

# Getting started

1. Clone the repo
2. Create a virtual environemnt using venv, virtualenv inside the repo directory
<code>
python -m venv .venv
</code>
3. Activate the virtual enviroment in 
    1. Windows - using `./.venv/Scripts/activate`
    2. Linus - using `source .venv/bin/activate` 
4. Install the required dependencies using `pip install -r requirements.txt`
5. Launch the app locally using `sanic server:create_app --factory (--dev:optional)`

