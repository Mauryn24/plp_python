# Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). OOP allows for the organization of code into reusable, modular units, making it easier to manage and maintain complex systems.

## Core Concepts

### 1. Classes and Objects

- **Class**: A blueprint for creating objects. It defines the attributes and methods that the objects will have.
- **Object**: An instance of a class. It represents a specific entity or instance in the program.

### 2. Encapsulation

Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (class). It hides the internal state of an object and only exposes the necessary functionalities to interact with it.

### 3. Inheritance

Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reuse and supports the concept of "is-a" relationships.

### 4. Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables flexibility and dynamic behavior in the program by allowing methods to be called on objects without knowing their specific class types.

## Benefits of OOP

- **Modularity**: Code is organized into classes, making it easier to manage and maintain.
- **Reusability**: Classes and objects can be reused in different parts of the program or in other programs.
- **Flexibility**: OOP supports abstraction, encapsulation, inheritance, and polymorphism, allowing for flexible and extensible code.

## Usage

To use OOP in your Python projects:

1. Define classes that represent the entities or concepts in your problem domain.
2. Create objects (instances) of these classes and manipulate them using their methods and attributes.
3. Utilize inheritance, encapsulation, and polymorphism to organize and structure your code effectively.

## Example

Here's a simple example of defining a class in Python:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("John", 30)

# Call the introduce method to display the person's information
person1.introduce()

## Resources
Python Documentation on Classes
Real Python - Object-Oriented Programming (OOP) in Python
GeeksforGeeks - Object Oriented Programming in Python

## Author
Mauryn Nyakio Gitonga