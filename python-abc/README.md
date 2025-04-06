# Python ABC (Abstract Base Classes) 🧩

This project explores Python's Abstract Base Classes (ABC) module, which provides infrastructure for defining abstract base classes in Python. ABCs are a powerful way to create interfaces and ensure that derived classes implement specific methods.

## Project Overview 📋

The project consists of exercises demonstrating various aspects of abstract base classes:

- **Basic ABC Implementation**: Creating and using abstract base classes
- **Method Requirements**: Enforcing derived classes to implement specific methods
- **Abstract Properties**: Using abstract properties in interfaces
- **ABC Registration**: Registering classes as virtual subclasses
- **Custom ABCs**: Creating specialized abstract base classes for specific domains

## Key Concepts ✨

- **@abstractmethod**: Decorator to declare abstract methods
- **@abstractproperty**: Decorator for abstract properties
- **ABC Module**: Understanding the abc module tools
- **Interface Design**: Creating clean interfaces with ABCs
- **Duck Typing vs ABCs**: When to use each approach
- **Metaclasses**: How ABC uses metaclasses to enforce contracts

## File Structure 📁

- **basic_abc.py**: Fundamental ABC implementation examples
- **abstract_shapes.py**: Shape hierarchy using ABCs
- **custom_containers.py**: Custom container types with ABCs
- **abc_registration.py**: Examples of registering virtual subclasses
- **tests/**: Test cases for the ABC implementations

## Learning Objectives 🎯

- Understand the concept and purpose of abstract base classes
- Create interfaces using ABC to enforce method implementations
- Use abstract methods and properties effectively
- Recognize when to use ABCs versus duck typing
- Implement custom abstract base classes for specific domains
- Apply best practices for interface design in Python

## Requirements ⚙️

- Python 3.8 or higher
- All files will be interpreted/compiled on Ubuntu 20.04 LTS
- All files should end with a new line
- First line of all files should be `#!/usr/bin/python3`
- Code should follow PEP 8 style guide (pycodestyle)
- All modules, classes, and functions should have documentation
- All your test files should be inside a `tests` folder

## Usage 🛠️

```python
#!/usr/bin/python3
from abstract_shapes import Shape, Circle

# This will fail because Shape is abstract
# shape = Shape()  # TypeError: Can't instantiate abstract class

# This works because Circle implements all abstract methods
circle = Circle(radius=5)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
```

## Advanced Topics 🔍

- **ABC and Collections Module**: How ABCs are used in Python's collections module
- **Runtime ABC Checking**: Using `isinstance()` and `issubclass()` with ABCs
- **Multiple Inheritance with ABCs**: Combining several interfaces
- **Performance Implications**: Understanding the cost of using ABCs

## Author ✍️
- Benjamin Ristord