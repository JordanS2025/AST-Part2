 Jordan Scott, David Smical,  & Eli Streitmatter
AST Part 2 CST-301

This repository contains code developed by Jordan Scott, David Smical, and Eli Streitmatter for the second part of the Abstract Syntax Tree (AST) project in the CST-301 course.

 Description

The code presented here is aimed at analyzing and processing Abstract Syntax Trees (ASTs) generated from Java code. It involves traversing the AST, identifying different node types, and performing actions based on the identified nodes. Additionally, it includes functionality to access Java documentation for specified packages or classes directly from their URLs.

 Usage

To utilize this code, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required Python packages. You can do this by running:
   
   pip install beautifulsoup4 requests
   
3. Clone this repository to your local machine.
4. Navigate to the directory containing the cloned repository.
5. Run the Python script using the command:
   
   python ASTpt2.py
   

 Functions

- `load_ast_from_json(json_file)`: Loads AST data from a JSON file.
- `access_java_documentation(url)`: Fetches and prints all textual content from a given URL, typically Java documentation.
- `search_for_packages(package_names, base_url)`: Accesses documentation for a list of specific Java packages or classes.
- `traverse_ast(ast_node, variables, reserved_words, interesting_things)`: Traverses the AST and identifies node types, populating lists with variables, reserved words, and interesting things found in the AST.
- `main()`: The main function that orchestrates the loading of AST data, traversal, identification of node types, and printing of collected data.
