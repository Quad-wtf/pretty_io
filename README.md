# Pretty IO

A Python module for beautiful terminal input/output with ANSI styling and colors.

## Features

- 🎨 **Colorful Output**: Print text in various colors (red, green, blue, etc.)
- ✨ **Text Styling**: Bold, italic, underline, and more styles
- 🎯 **Pretty Input**: Get user input with styled prompts
- 🔄 **Combined I/O**: Input with automatic styled responses
- 🚀 **Easy to Use**: Simple function calls with intuitive parameters
- 📦 **Print-like Interface**: Works just like Python's built-in `print()` function

## Installation

### From Source
```bash
git clone https://github.com/yourusername/pretty-io.git
cd pretty-io
pip install -e .
```

### Using pip (when published)
```bash
pip install pretty-io
```

## Quick Start

```python
from pretty_io import PrintPretty, InputPretty, InputOutputPretty

# Print colorful text (just like print!)
PrintPretty("Error: Something went wrong!", Style1="bold", Color1="red")
PrintPretty("Success: Operation completed!", Style1="italic", Color1="green")

# Print multiple variables
name = "John"
age = 25
PrintPretty("Hello", name, "you are", age, "years old", Color1="cyan")

# Get styled input
user_name = InputPretty(Prompt="Enter your name: ", Style1="bold", Color="cyan")

# Combined input/output
favorite = InputOutputPretty(
    Prompt="Favorite color? ",
    Style1="bold", Color="blue",
    ResponseText="Nice! {input} is awesome!",
    ResponseColor="green"
)
```

## Functions

### PrintPretty()
Print text with optional styling and colors using ANSI escape codes.
Works like the standard `print()` function with styling options.

**Parameters:**
- `*args`: Values to print (like standard print function)
- `Style1` (str): First style (bold, italic, underline, etc.)
- `Style2` (str): Second style (can be combined)
- `Color1` (str): Text color
- `sep` (str): Separator between values (default: ' ')
- `end` (str): String appended after the last value (default: '\n')

**Examples:**
```python
# Print single value
PrintPretty("Important message!", Style1="bold", Color1="red")

# Print multiple values (like print())
PrintPretty("Name:", name, "Age:", age, Color1="blue")

# Custom separator
PrintPretty("A", "B", "C", sep=" | ", Color1="green")

# No newline at end
PrintPretty("Loading", end="", Color1="yellow")
PrintPretty("...", Color1="yellow")
```

### InputPretty()
Get user input with a styled prompt.

**Parameters:**
- `Prompt` (str): Prompt text to display
- `Style1` (str): First style for prompt
- `Style2` (str): Second style for prompt
- `Color` (str): Color for prompt
- `UserInputColor` (str): Color for user's typing
- `UserInputStyle` (str): Style for user's typing

**Example:**
```python
email = InputPretty(
    Prompt="Email: ", 
    Style1="bold", Color="blue",
    UserInputColor="green", UserInputStyle="italic"
)
```

### InputOutputPretty()
Combined input with automatic styled response.

**Parameters:**
- All InputPretty parameters, plus:
- `ResponseText` (str): Text to print after input (use `{input}` for user input)
- `ResponseStyle` (str): Style for response
- `ResponseColor` (str): Color for response

**Example:**
```python
result = InputOutputPretty(
    Prompt="Choose a number: ",
    Style1="bold", Color="cyan",
    UserInputColor="yellow",
    ResponseText="You chose: {input}",
    ResponseStyle="italic", ResponseColor="green"
)
```

## Available Styles

- `bold` - **Bold text**
- `dim` - Dimmed text
- `italic` - *Italic text*
- `underline` - <u>Underlined text</u>
- `blink` - Blinking text
- `reverse` - Reversed colors
- `strikethrough` - ~~Strikethrough text~~

## Available Colors

### Regular Colors
- `black`, `red`, `green`, `yellow`
- `blue`, `magenta`, `cyan`, `white`

### Bright Colors
- `bright_black`, `bright_red`, `bright_green`, `bright_yellow`
- `bright_blue`, `bright_magenta`, `bright_cyan`, `bright_white`

## Examples

### Basic Usage
```python
from pretty_io import PrintPretty, InputPretty

# Simple colored output (new print-like syntax)
PrintPretty("This is red text", Color1="red")
PrintPretty("Bold green text", Style1="bold", Color1="green")

# Print variables
name = "Alice"
score = 95
PrintPretty("Player:", name, "Score:", score, Color1="cyan")

# Get user input with styling
user_name = InputPretty(Prompt="Name: ", Color="blue")
age = InputPretty(
    Prompt="Age: ", 
    Style1="bold", Color="yellow",
    UserInputColor="bright_green"
)
```

### Advanced Styling
```python
# Multiple styles combined
PrintPretty(
    "Multi-styled text!",
    Style1="bold", 
    Style2="underline", 
    Color1="bright_cyan"
)

# Print lists and multiple values
numbers = [1, 2, 3, 4, 5]
PrintPretty("Numbers:", *numbers, sep=" | ", Color1="magenta")

# Progress indicator
PrintPretty("Processing", end="", Color1="yellow")
for i in range(3):
    PrintPretty(".", end="", Color1="yellow")
PrintPretty(" Done!", Color1="green", Style1="bold")
```

### Interactive Applications
```python
from pretty_io import InputOutputPretty, PrintPretty

def interactive_quiz():
    PrintPretty("=== Quiz Time! ===", Style1="bold", Color1="cyan")
    
    answer1 = InputOutputPretty(
        Prompt="What's 2+2? ",
        Style1="bold", Color="yellow",
        UserInputColor="bright_green",
        ResponseText="You answered: {input}",
        ResponseColor="blue"
    )
    
    if answer1 == "4":
        PrintPretty("Correct! ✓", Style1="bold", Color1="green")
    else:
        PrintPretty("Try again! ✗", Style1="bold", Color1="red")

# Debug output example
def debug_variables():
    x = 10
    y = 20
    result = x + y
    
    PrintPretty("Debug Info:", Style1="bold", Color1="yellow")
    PrintPretty("x =", x, "y =", y, "result =", result, Color1="cyan")

interactive_quiz()
debug_variables()
```

### Replacing Standard Print
```python
# You can easily replace print() with PrintPretty() in existing code
# Old code:
# print("Hello", name, "your score is", score)

# New code with styling:
PrintPretty("Hello", name, "your score is", score, Color1="green", Style1="bold")

# Works with all print() features
data = ["apple", "banana", "cherry"]
PrintPretty("Fruits:", *data, sep=", ", end="!\n", Color1="magenta")
```

## Utility Functions

### PrintPossibilities()
Display all available styles and colors:

```python
from pretty_io import PrintPossibilities

# Show all options
PrintPossibilities()

# Show just colors
PrintPossibilities.colors()

# Show just styles  
PrintPossibilities.styles()
```

## Requirements

- Python 3.6+
- Terminal with ANSI color support (most modern terminals)

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Changelog

### v1.0.1
- **NEW**: PrintPretty now works like built-in `print()` function
- **NEW**: Accepts multiple positional arguments like `print()`
- **NEW**: Supports `sep` and `end` parameters
- **REMOVED**: `Color2` parameter for simplicity
- **REMOVED**: Complex variable printing features
- InputPretty with user input styling
- InputOutputPretty for combined I/O
- Full ANSI color and style support
