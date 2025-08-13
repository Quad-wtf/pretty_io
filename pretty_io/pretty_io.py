"""
pretty_io - A Python module for pretty terminal input/output with ANSI styling.

This module provides functions to print and get input with colored text,
styles, and formatting in the terminal.

Functions:
    PrintPretty: Print text with optional styling and colors
    InputPretty: Get user input with a styled prompt
    InputOutputPretty: Combined input/output with styling

Example:
    >>> from pretty_io import PrintPretty, InputPretty
    >>> PrintPretty(Style1="bold", Color1="red", Print="Hello World!")
    >>> name = InputPretty(Prompt="Name: ", Color="blue", UserInputColor="green")
"""

from typing import Optional

__version__ = "1.0.1"
__author__ = "Quad, Wtf"
__all__ = [
    "PrintPretty",
    "InputPretty",
    "InputOutputPretty",
    "PrintPossibilities",
    "STYLES",
    "COLORS",
]

# ANSI escape codes for styling
STYLES = {
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "reverse": "\033[7m",
    "strikethrough": "\033[9m",
}

COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}

RESET = "\033[0m"


def PrintPretty(
    Style1: Optional[str] = None,
    Style2: Optional[str] = None,
    Color1: Optional[str] = None,
    Color2: Optional[str] = None,
    Print: Optional[str] = None,
):
    """
    Print text with optional styling and colors using ANSI escape codes.

    Args:
        Style1: First style (e.g., 'bold', 'italic', 'underline')
        Style2: Second style (can be combined with Style1)
        Color1: Text color
        Color2: Background color (use bg_ prefix)
        Print: The text to print
    """
    if Print is None:
        print()
        return

    # Build the formatting string
    format_str = ""

    # Add styles
    if Style1 and Style1 in STYLES:
        format_str += STYLES[Style1]
    if Style2 and Style2 in STYLES:
        format_str += STYLES[Style2]

    # Add text color
    if Color1 and Color1 in COLORS:
        format_str += COLORS[Color1]

    # Add background color (assuming Color2 is for background)
    if Color2:
        if Color2.startswith("bg_") and Color2[3:] in COLORS:
            # Convert text color code to background color code
            bg_code = COLORS[Color2[3:]].replace("[3", "[4").replace("[9", "[10")
            format_str += bg_code
        elif Color2 in COLORS:
            # Convert to background color
            bg_code = COLORS[Color2].replace("[3", "[4").replace("[9", "[10")
            format_str += bg_code

    # Print with formatting and reset
    print(format_str + Print + RESET)


def InputPretty(
    Prompt: Optional[str] = None,
    Style1: Optional[str] = None,
    Style2: Optional[str] = None,
    Color: Optional[str] = None,
    UserInputColor: Optional[str] = None,
    UserInputStyle: Optional[str] = None,
) -> str:
    """
    Get user input with a pretty formatted prompt.

    Args:
        Prompt: The prompt text to display
        Style1: First style for prompt
        Style2: Second style for prompt
        Color: Text color for prompt
        UserInputColor: Color for user input text
        UserInputStyle: Style for user input text

    Returns:
        User input as string
    """
    # Build prompt formatting
    prompt_format = ""
    if Style1 and Style1 in STYLES:
        prompt_format += STYLES[Style1]
    if Style2 and Style2 in STYLES:
        prompt_format += STYLES[Style2]
    if Color and Color in COLORS:
        prompt_format += COLORS[Color]

    # Build user input formatting
    input_format = ""
    if UserInputStyle and UserInputStyle in STYLES:
        input_format += STYLES[UserInputStyle]
    if UserInputColor and UserInputColor in COLORS:
        input_format += COLORS[UserInputColor]

    # Create formatted prompt
    if Prompt:
        formatted_prompt = prompt_format + Prompt + RESET
    else:
        formatted_prompt = ""

    # Get input with formatting
    try:
        if input_format:
            user_input = input(formatted_prompt + input_format)
            print(RESET, end="")  # Reset formatting after input
            return user_input
        else:
            return input(formatted_prompt)
    except KeyboardInterrupt:
        print(RESET)  # Make sure to reset formatting
        raise


def InputOutputPretty(
    Prompt: Optional[str] = None,
    Style1: Optional[str] = None,
    Style2: Optional[str] = None,
    Color: Optional[str] = None,
    UserInputColor: Optional[str] = None,
    UserInputStyle: Optional[str] = None,
    ResponseText: Optional[str] = None,
    ResponseStyle: Optional[str] = None,
    ResponseColor: Optional[str] = None,
) -> str:
    """
    Combined function that gets pretty input and optionally prints a pretty response.

    Args:
        Prompt: The prompt text
        Style1: First style for prompt
        Style2: Second style for prompt
        Color: Text color for prompt
        UserInputColor: Color for user input text
        UserInputStyle: Style for user input text
        ResponseText: Optional response to print after input (use {input} for user input)
        ResponseStyle: Style for response text
        ResponseColor: Color for response text

    Returns:
        User input as string
    """
    # Get the input
    user_input = InputPretty(
        Prompt, Style1, Style2, Color, UserInputColor, UserInputStyle
    )

    # Print response if provided
    if ResponseText:
        formatted_response = ResponseText.format(input=user_input)
        PrintPretty(
            Style1=ResponseStyle, Color1=ResponseColor, Print=formatted_response
        )

    return user_input


def PrintPossibilities():
    print(", ".join(STYLES.keys()))
    print(", ".join(COLORS.keys()))


def print_colors():
    print(", ".join(COLORS.keys()))


def print_styles():
    print(", ".join(STYLES.keys()))


# Add the attributes to the function
PrintPossibilities.colors = print_colors
PrintPossibilities.styles = print_styles
