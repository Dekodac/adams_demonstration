# Git Workshop

## Prerequesites

Students should already have experience using git and github (solo, not in teams) for their assignments and assessments. This workshop assumes some basic knowledge and experience with Git

## Objectives

You will learn git workflows and techniques for common "scenarios" that can be tricky. We will do some branching, but not yet focus on things like merge conflicts, etc. You will do solo work in a repo to "simulate" some aspects of doing work collaboratively.

These skills will be helpful for Part Two of the workshop, where you will do work in teams and be making "feature branches", pull requests, and merging feature branches onto shared dev/main/prod branches.

### The "School" app

We will build a simple "school" web app using python/flask, and React.js. For simplicity we will not use a database, React Router, etc. This is purely to give us enough code to make our "scenarios" interesting. All code will be given - the focus is on git. 

Depending how far we get, the "School" app will have the following features:

- Students
- Courses
- Professors
- TA's

We will fake and hardcode our data in our flask app, and write the various backend endpoints needed for a simple REST API. We will also build a simple frontend.

## Topics Covered

1. ["I committed code I don't want" - using `git reset` to safely un-stage or un-commit code](./git-reset.md)
