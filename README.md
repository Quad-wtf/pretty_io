# Pretty IO

A Python module for beautiful terminal input/output with ANSI styling and colors.

## Features

- 🎨 **Colorful Output**: Print text in various colors (red, green, blue, etc.)
- ✨ **Text Styling**: Bold, italic, underline, and more styles
- 🎯 **Pretty Input**: Get user input with styled prompts
- 🔄 **Combined I/O**: Input with automatic styled responses
- 🚀 **Easy to Use**: Simple function calls with intuitive parameters

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

# Print colorful text
PrintPretty(Style1="bold", Color1="red", Print="Error: Something went wrong!")
PrintPretty(Style1="italic", Color1="green", Print="Success: Operation completed!")

# Get styled input
name = InputPretty(Prompt="Enter your name: ", Style1="bold", Color="cyan")

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
Print text with optional styling and colors.

**Parameters:**
- `Style1` (str): First style (bold, italic, underline, etc.)
- `Style2` (str): Second style (can be combined)
- `Color1` (str): Text color
- `Color2` (str): Background color
- `Print` (str): Text to print

**Example:**
```python
PrintPretty(Style1="bold", Style2="underline", Color1="red", Print="Important!")
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

# Simple colored output
PrintPretty(Color1="red", Print="This is red text")
PrintPretty(Style1="bold", Color1="green", Print="Bold green text")

# Get user input with styling
name = InputPretty(Prompt="Name: ", Color="blue")
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
    Style1="bold", 
    Style2="underline", 
    Color1="bright_cyan", 
    Print="Multi-styled text!"
)

# Background colors
PrintPretty(
    Style1="bold", 
    Color1="white", 
    Color2="red", 
    Print="White text on red background"
)
```

### Interactive Applications
```python
from pretty_io import InputOutputPretty, PrintPretty

def interactive_quiz():
    PrintPretty(Style1="bold", Color1="cyan", Print="=== Quiz Time! ===")
    
    answer1 = InputOutputPretty(
        Prompt="What's 2+2? ",
        Style1="bold", Color="yellow",
        UserInputColor="bright_green",
        ResponseText="You answered: {input}",
        ResponseColor="blue"
    )
    
    if answer1 == "4":
        PrintPretty(Style1="bold", Color1="green", Print="Correct! ✓")
    else:
        PrintPretty(Style1="bold", Color1="red", Print="Try again! ✗")

interactive_quiz()
```

## Demo

Run the built-in demo to see all features:

```python
from pretty_io import _demo
_demo()
```

Or run the module directly:
```bash
python -m pretty_io
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

### v1.0.0
- Initial release
- Basic PrintPretty function
- InputPretty with user input styling
- InputOutputPretty for combined I/O
- Full ANSI color and style support