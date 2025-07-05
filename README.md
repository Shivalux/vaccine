# Program:
    vaccine

# Discription:
    A SQL Injection tool that scans the given URL to detect vulnerable parameters
    and extract database information. The results will be optionally saved to a file.
        • Each header must be provided as a key:value pair (e.g., "User-Agent=vaccine/1.0").
        • This tool currently supports MySQL and PostgreSQL injection techniques.
        • The defutal of output path is ./defualt_one.txt

 # Installation:
    • Clone the project into your computer:
        git clone <repository-url> ~/infection
    • Install the required Python packages:
        pip install -r requirements.txt

# Usege:
    <pre> ```./vaccine [-h] [-o FILE] [-X MEDTHOD] [-H HEADER [HEADER ...]] URL ``` </pre>

# Option:
| Option                                                 | Description                                                |
| ------------------------------------------------------ | ---------------------------------------------------------- |
| `-h, --help`                                           | Show this help message and exit                            |
| `-o FILE, --output FILE`                               | Specify a file to save the output of the injection process.|
| `-X MEDTHOD, --method MEDTHOD`                         | Show the version of the program                            |
| `-H HEADER [HEADER ...], --header HEADER [HEADER ...]` | Additional request headers in the format: Key=Value        |

