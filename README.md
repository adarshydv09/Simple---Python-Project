# Simple Python Calculator

A clean, easy-to-use command-line calculator built with Python. Perfect for learning and performing basic arithmetic operations.

## Features

- **Addition** - Add two numbers
- **Subtraction** - Subtract one number from another
- **Multiplication** - Multiply two numbers
- **Division** - Divide numbers with zero-division protection
- **Power** - Raise a number to any power
- **Modulus** - Find the remainder of division
- **Error Handling** - Validates user input and prevents errors
- **User-Friendly Interface** - Clean menu system with clear prompts

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only built-in Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/simple-calculator.git
```

2. Navigate to the project directory:
```bash
cd simple-calculator
```

3. Run the calculator:
```bash
python calculator.py
```

## Usage

When you run the calculator, you'll see a menu with options:

```
=== Simple Calculator ===
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)
6. Modulus (%)
7. Exit
=========================
```

Simply:
1. Choose an operation by entering its number (1-7)
2. Enter the first number when prompted
3. Enter the second number when prompted
4. View your result
5. Repeat or exit

### Example

```
Select operation (1-7): 1
Enter first number: 15
Enter second number: 25

15.0 + 25.0 = 40.0
```

## Code Structure

The calculator is organized into simple, reusable functions:

- `add(a, b)` - Performs addition
- `subtract(a, b)` - Performs subtraction
- `multiply(a, b)` - Performs multiplication
- `divide(a, b)` - Performs division with error checking
- `power(a, b)` - Calculates power
- `modulus(a, b)` - Calculates remainder
- `display_menu()` - Shows the menu
- `get_numbers()` - Gets user input with validation
- `main()` - Main program loop

## Error Handling

The calculator handles common errors:
- **Invalid input**: Prompts user to enter valid numbers
- **Division by zero**: Shows error message instead of crashing
- **Invalid menu choice**: Asks user to select a valid option

## Future Enhancements

Potential features to add:
- Square root and other scientific functions
- History of calculations
- Memory functions (M+, M-, MR, MC)
- Expression evaluation (e.g., "2 + 3 * 4")
- GUI version using tkinter

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Happy Calculating!** 🧮
