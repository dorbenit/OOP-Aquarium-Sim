# 🐟 OOP Aquarium Simulation in Python

## Overview
This project implements a complete object-oriented simulation of an aquarium using Python. It features a dynamic environment where various types of animals (fish and crabs) interact with each other, age over time, and respond to environmental constraints such as hunger, collisions, and boundaries.

The system is designed with clarity and modularity in mind, making use of abstract base classes, inheritance, and polymorphism. It also includes a suite of automated tests to ensure correctness and robustness.

## Key Features
- **Object-Oriented Design** using abstract base classes (`Animal`) and specialized subclasses (`Molly`, `Scalar`, `Ocypode`, `Shrimp`, `Crab`)
- **Inheritance and Polymorphism** for animal behavior (e.g., horizontal/vertical movement, different shapes)
- **Collision handling** between crabs and walls
- **Lifecycle management**: animals die from starvation or old age
- **Visual rendering**: textual representation of the aquarium
- **Custom exceptions** for input validation and simulation errors
- **Unit tests** written using Python’s `unittest` framework

## File Structure
```
├── Aquarium.py              # Main simulation engine
├── Animal.py                # Abstract base class for all animals
├── Fish.py / Crab.py        # Intermediary classes
├── Molly.py, Scalar.py, Ocypode.py, Shrimp.py  # Specific animal types
├── Exceptions.py            # Custom exceptions for input and simulation
├── Animals_lists.py         # Static shape representations for animals
├── main.py                  # CLI (provided by course staff)
├── test_molly.py            # Unit tests for Molly
├── test_aquarium.py         # Comprehensive simulation tests
```

## How to Run
You can run the simulation using the interactive interface:

```bash
python main.py
```

To run the tests:
```bash
python -m unittest test_aquarium.py
```

## Example Output
```
The aquarium, sized 27/45 and currently in step 0, contains the following animals:
The molly momo is 110 years old and has 10 food.
The scalar s2 is 20 years old and has 10 food.
...
```

## Concepts Demonstrated
- Abstract classes with `@abstractmethod`
- Encapsulation of animal logic and board rendering
- Method overriding (e.g., `move()`, `get_animal()`)
- Error handling via custom exceptions
- Independent test cases to verify functionality

## Notes
- The project emphasizes clarity, maintainability, and extensibility.
- Animals are visualized as character matrices inserted into the board.
- Simulation logic (movement, aging, feeding) is clearly separated from visualization logic.
- **Note:** The file `main.py` was provided by the course staff and is included here for demonstration and testing purposes only. All core logic and testing were implemented independently.

## License
This project is released under the MIT License – feel free to use, share, and extend!