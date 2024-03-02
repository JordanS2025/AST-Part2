# Jordan Scott, David Smical,  & Eli Streitmatter
# AST part 2 CST-301 
import json
import requests
from bs4 import BeautifulSoup

# Load AST from JSON file
def load_ast_from_json(json_file):
    with open(json_file, 'r') as f:
        ast_data = json.load(f)
    return ast_data

def access_java_documentation(url):
    """
    Fetches and prints all textual content from the given URL.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('title').get_text()
            print(f"\nTitle of the page: {title}\n")

            # Remove script and style elements to clean up the text
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()

            # Get text from the body, clean it up, and print it
            body_text = soup.body.get_text(separator='\n', strip=True)
            print(body_text)
        else:
            print(f"Failed to access content at {url}.")
    except Exception as e:
        print(f"An error occurred while accessing {url}: {e}")

def search_for_packages(package_names, base_url="https://docs.oracle.com/javase/8/docs/api/"):
    """
    Directly accesses documentation for a list of specific Java packages or classes.
    """
    for package_name in package_names:
        # Adjust the URL construction for accessing the specific package or class documentation
        package_url = f"{base_url}{package_name.replace('.', '/')}.html"
        print(f"\nAccessing documentation for: {package_name} at {package_url}")
        access_java_documentation(package_url)


# Traverse AST and identify node types
def traverse_ast(ast_node, variables, reserved_words, interesting_things):
    if isinstance(ast_node, dict):
        if 'type' in ast_node:
            node_type = ast_node['type']
            if node_type == 'VariableDeclarator':
                if 'name' in ast_node:
                    variables.append(ast_node['name'])
            elif node_type == 'Import':
                if 'path' in ast_node:
                    interesting_things.append(ast_node['path'])
                    # Access Java documentation for interesting things
                    #access_java_documentation()
            elif node_type == 'BasicType':
                if 'name' in ast_node:
                    reserved_words.append(ast_node['name'])
        for key, value in ast_node.items():
            traverse_ast(value, variables, reserved_words, interesting_things)
    elif isinstance(ast_node, list):
        for item in ast_node:
            traverse_ast(item, variables, reserved_words, interesting_things)

# Main function
def main():
    # Load AST from JSON file
    ast_data = load_ast_from_json('/Users/bignola/Desktop/output_ast2.json')

    # Initialize data structures
    variables = []
    reserved_words = []
    interesting_things = []

    # Traverse AST and identify node types
    traverse_ast(ast_data, variables, reserved_words, interesting_things)

    # Print or process the collected data
    search_for_packages(interesting_things)
    print("Variables:", variables)
    print("Reserved Words:", reserved_words)
    print("Interesting Things:", interesting_things)

if __name__ == "__main__":
    main()
