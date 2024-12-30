# Code Indentation Formatter

A simple Python program that automatically formats unindented or poorly indented code by adding proper indentation based on code structure. The program analyzes code blocks and applies consistent indentation rules based on nested structures using brackets ({, }, (, ), [, ]).

## Features

- Automatically indents code based on bracket structure
- Configurable spaces per indentation level (default: 4 spaces)
- Preserves empty lines
- Handles nested structures
- Simple interactive command-line interface

## Usage

1. Run the program:
python indent.py

2. Enter your code block. For example:
int main(){
int x = 5;
if(x > 0){
printf("Positive");
}
}

3. Press ENTER twice (input an empty line) when you're finished entering code.

4. The program will output the properly formatted code:
int main() {
    int x = 5;
    if(x > 0) {
        printf("Positive");
    }
}

## Supported Features

- Handles multiple types of brackets: {}, (), []
- Maintains proper indentation levels for nested structures
- Preserves empty lines in the code
- Strips existing indentation before applying new formatting
- Prevents negative indentation levels

## Requirements

- Python 3.x