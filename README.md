# Final Capstone - Task Manager

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Reports](#reports)

## Description
A task manager application where users can be registered and tasks are then assigned to them. Admin functionality built in to generate reports to show statistics such as tasks assigned to each user, completion rate, and tasks that are overdue.

## Installation
1. Install Python from the official Python website (https://www.python.org) if you haven't already.
2. Clone the repository containing the task_manager.py file to your local machine.
3. Navigate to the directory where the task_manager.py file is located.
4. Open a terminal here and execute the command "python task_manager.py"

## Features
reg_user - A new standard (non-admin) user can be added to the system. The application will check for a unique username

add_task - A new task can be added to the system. This will require an assignee, description and due date

view_all - All the tasks (completed/uncompleted) that have been added to the system will be displayed

view_mine - Tasks assigned to the user that is currently logged in will be shown. If this option is selected, the user is presented with options to edit the task

## Reports
Two reports are available to be generated within the application, these are:

Task Overview - This will generate a text file that contains information relating to tasks within the system. Key information includes the number of uncompleted tasks and tasks that are overdue, this is further broken down into percentages to give more insight and overview

User Overview - This will generate a text file that contains information about users, but also users and tasks related to that user. The total number of users registered in the system, along with a breakdown of each user and their task statuses are included in this report
