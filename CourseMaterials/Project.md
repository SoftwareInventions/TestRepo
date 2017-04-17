# Software Engineering Project

## Overview
In this project, you'll work in teams of 3 to find a customer and a product, and conduct an initial Scrum sprint.

## Tasks

### Pick a Team (Due 3/27)
You must choose from among those who have already finished the individual WorldFactory project, and your team must have my OK.  I will choose teams by Monday if I do not hear from you with any preferences.

### Find a Customer (Due 3/30)
This stage is similar to what you did for database, and indeed may even involve the same customer if you like.  You're looking for a project that will produce a reasonable backlog and a manageable initial sprint, meaning something you can demonstrate as a working "version 0.1" including automated tests, code reviews, and very basic functionality.



#### About UI
I would prefer a project that is a web or mobile application, but I recognize not all teams will have the expertise for this.  A desktop GUI interface, e.g. JavaFX, WinForms is a close second, and a purely text UI is acceptable if necessary.

#### Deliverable
Deliverable for this phase is a brief (e.g. 400 words) description of what you're planning to take on, and an explanation of how it meets the stated criteria.  Get my approval for this; no need to hand anything in formally.

### Backlog and First Sprint Plan (Due 4/4)
#### Create a backlog
Express your "spec" for the project in the form of a prioritized list of 15-20 PBIs.  This must include 5-10 ready-for-sprint stories, with estimates using ideal days.  It must also include less-refined PBIs, with "shirt size" estimates".

#### Plan an initial sprint
Select features for an initial sprint, planning for TDD-style development (see below).  Budget for 10 ideal days of effort, including test development and implementation.  (This is 80 hrs, 27 hrs/member -- just under 3 weeks nominal effort for a 3 unit class.)

#### Set up a repo
Create a Github-based project repo, and make all team members and SoftwareInventions contributors.  

Register each of your PBIs as Issues in the repo, with number of ideal days or "shirt size" estimates embedded in the title, e.g. Create Registration System (medium).  Since Github lacks a general prioritization system, fake this by setting up five labels P1->P5 for priority.

Establish a "Sprint 1" milestone and put the agreed upon PBIs under that milestone.  Get my OK on the milestone.

#### Deliverable
The GitHub issues and first milestone are your deliverable for this step.  They require my formal approval, however, and the deliverable is not "done" until I OK what you have.

### Build tests (Due 4/13)
Write a suite of automated tests for your initial sprint *before you write any code for the features themselves*.  (You may, and will probably have to, write interface descriptions, but not implementations.) 

#### Individual branches
During test building and implementation, each team member must maintain a separate branch, and periodically merge his/her branch into master.  I will want to review each individual's work via their branch commit history.  Do not do work on anyone's branch but your own.

There must be some automated tests, but where these are not feasible (e.g. to test UI) a written test script will suffice.

#### About language and framework choice
You are already familiar with JUnit, and using Java and JUnit is an acceptable default choice.

If you want to be more adventurous, JS, Python, C#, or C++ are other good languages to consider.  There are JUnit-like libraries for these.  Indeed, many of them are highly similar to JUnit in design.  Interestingly this is not because they are imitating JUnit but because JUnit, and the others, imitate a sort of ur-framework called sUnit, for Smalltalk.  Googling 'xUnit' will get you lots of references, including the predictable comprehensive and completely undiscriminating Wikipedia list of all such tools, including the defunct and unused ones.  See me for advice on how to pick one if you go this route.

#### Deliverable
A test branch under your repo, containing the tests, and a src branch with any interface implementations neede to make the tests buildable (though of course at this stage they'll all be "red".

### Implement Your Sprint (Due 4/20)
Build code that satisfies your tests and meets the PBIs for your sprint.  In particular, ensure that all your tests, automated or written, are met for the sprint.

#### Deliverable
Completed code for the sprint, under a src directory in your repo, meeting standard style requirements.  You must demo this to my satisfaction to have met the milestone.

### Code Reviews (4/22)
Be prepared to do code reviews on three other teams, and to be reviewed by three, during our Saturday session.
