# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](Q1/classObjectUML.md)

## Design Revision

Removed methods Power On and Load Game and replaced them download_game, upgrade_storage, and console_status.

## Visibility Decisions

| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Generation | int | Private | Private so it can't be accidentally modified. |
| Brand | str | Private | Private so brand names won't be swapped. |
| Model | str | Public | Public so the model is accessible in selling it. |
| Storage Capacity | int | Private | Priavate so the specifications won't be changed from unauthorized changes. |
| Price | int | Public | Public so it is accessible in selling it. |

## Updated UML Class Diagram
[Class Diagram](Q1/Images%20Folder/classDiagramSG5.png)

## Python Implementation
[View Python Source](Q1/classImplementation.py)

## Test Run
[Test Run](Q1/Images%20Folder/classTestRun.png)

## Object Diagram
![Object Diagram](Q1/Images%20Folder/objectDiagram.png)

## Analysis
### Why did you make your chosen attribute private?
So that it won't be modified by unauthorized people.

### Which method changes the state of your object?
upgrade_storage

### How did your two objects demonstrate that instances are independent?
If I change an attribute of one instance, it won't change the other.

### What is the difference between your class diagram and your object diagram?
The class diagram shows the diagram of the whole class, which includes the objects below it. The object diagram shows the attributes that object has.
