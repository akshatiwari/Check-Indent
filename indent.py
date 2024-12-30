class CodeFormatter:
    def __init__(self, spaces_per_indent=4):
        self.spaces_per_indent = spaces_per_indent
        self.indent_level = 0
        self.opening_chars = {'{', '(', '['}
        self.closing_chars = {'}', ')', ']'}
        
    def format_code(self, code: str) -> str:
        # Split code into lines and strip existing whitespace
        lines = [line.strip() for line in code.splitlines()]
        formatted_lines = []
        
        for line in lines:
            if not line:  # Preserve empty lines
                formatted_lines.append('')
                continue
                
            # Decrease indent for lines starting with closing brackets
            if line[0] in self.closing_chars:
                self.indent_level -= 1
            
            # Add current indentation
            current_indent = ' ' * (self.indent_level * self.spaces_per_indent)
            formatted_lines.append(current_indent + line)
            
            # Adjust indent level based on brackets
            self.adjust_indent_level(line)
            
        return '\n'.join(formatted_lines)
    
    def adjust_indent_level(self, line: str) -> None:
        # Count brackets that affect next line's indentation
        for char in line:
            if char in self.opening_chars:
                self.indent_level += 1
            elif char in self.closing_chars:
                # Don't decrease if we already decreased for line-starting bracket
                if char != line[0]:
                    self.indent_level -= 1
        
        # Ensure indent_level doesn't go negative
        self.indent_level = max(0, self.indent_level)


def format_code(code: str, spaces_per_indent: int = 4) -> str:
    formatter = CodeFormatter(spaces_per_indent)
    return formatter.format_code(code)


if __name__ == "__main__":
    print("Enter your code block (Press ENTER twice when finished):")
    try:
        # Read multiple lines until empty line is entered
        code_lines = []
        while True:
            line = input()
            if line.strip() == "" and code_lines:  # Empty line and we have some code
                break
            code_lines.append(line)
        
        # Join the lines and format the code
        code_block = '\n'.join(code_lines)
        formatted_code = format_code(code_block)
        
        print("\nFormatted code:")
        print(formatted_code)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
