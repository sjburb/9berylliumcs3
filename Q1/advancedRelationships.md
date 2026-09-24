# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md) <br>
[classRel](classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: Console <br>
Child: GamingConsole <br>
Explanation: GamingConsole share attributes with Console.
## Inheritance UML
![Inheritance](Images%20Folder/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation - GamingConsole has Games <br>
Explanation: The class GamingConsole has the class Games which is an independent class.
## Advanced UML Diagram
![Advanced UML](Images%20Folder/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](Images%20Folder/advancedTestRun.png)
## Object Diagram
![Objects](Images%20Folder/advancedObjectDiagram.png)

## Reflection
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class. <br> - Because GamingConsole is a type of Console and they share similar attributes.
2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused. <br> - It allowed GamingConsole to use Console's attributes and methods.
3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects. <br> - It is aggregation because the Games objects can exist without GamingConsole.
4. What is the difference between Association from Part III and the advanced relationship you
implemented? <br> - Association shows connections between classes and aggregation is about classes having other classes that can function without the parent class.
5. How does your design follow the DRY principle? <br> - It follows dry because it reuses code without writing it again.
