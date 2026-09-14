# Class Relationships: Association and Multiplicity
## [Previous Work](Q1/classAttributesMethods.md)
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Video Game Console
Description: A class that shows the properties a video game console has.
## New Related Class
Class: Games
Description: A class that shows the attributes a game has.
## Association
Relationship: Console -> Game
Explanation: A Console has many Games, because multiple games can be played on one console.
## Multiplicity 

Multiplicity: One to Many
Explanation: A console has many games.
## UML Class Relationship Diagram
![Class Relationship Diagram](Q1/Images%20Folder/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](Q1/classRelationships.py)
## Test Run
![Relationship Test Run](Q1/Images%20Folder/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](Q1/Images%20Folder/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes? A Console has many Games that can be played on it.
### What multiplicity did you choose and why? I chose One to Many because a console can have multiple games.
### How did you implement the relationship in Python? I stored game objects inside the Console class.
### Why did you store an object reference instead of copying its data? So that the Console can access the game's actuall attributes and methods.
### If your relationship uses many, why is a list appropriate? A list is appropriate because it can store multiple Game objects in one Console.
