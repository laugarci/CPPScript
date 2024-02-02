# -*- coding: utf-8 -*-

class Colors:
    RESET = '\033[0m'
    GREEN = '\033[32m'
    RED = '\033[31m'

def create_class_hpp(name, args):

    fileName = name + ".hpp"

    if args != "":
        args_list = [arg.strip() for arg in args.split(',')]
        private_attributes = "\n\t".join(" {} {};".format(arg.split()[0], "_" + arg.split()[1]) for arg in args_list)
    else:
        private_attributes = ""

    content = (
        "#ifndef " + name.upper() + "_HPP\n"
        "#define " + name.upper() + "_HPP\n\n"
        "#include <iostream>\n\n"
        "class " + name + " {\n"
        "private:\n\t"
        + private_attributes + "\n"
        "public:\n"
        "\t" + name + "(" + args + ");\n"
        "\t~" + name + "();\n"
        "\t" + name + "(const " + name + "& other);\n"
        "\t" + name + "& operator=(const " + name + "& other);\n"
        "};\n\n"
        "#endif"
    )


    with open(fileName, 'w') as openFile:
        openFile.write(content)

    print("\nfile " + fileName + " was created")

def create_class_cpp(name, args):
    fileName = name + ".cpp"

    content = (
        "#include " + "\""+ name + ".hpp" + "\"\n\n"
        + name + "::" + name + "(" + args + ")\n{\n}\n\n"
        + name + "::~" + name + "()\n" + "{\n}\n\n"
        + name + "::" + name + "(const " + name + "& other)\n{\n" + "\t" + "*this = other;\n}\n\n"
        + name + " &" + name + "::operator=(const " + name + "& other)\n{\n\t//add info\n\treturn(*this);\n}\n" 
    )

    with open(fileName, 'w') as openFile:
        openFile.write(content)

    print("file " + fileName + " was created")

name = raw_input(Colors.GREEN + "Class name: " + Colors.RESET)
name = name[0].upper() + name[1:]
args = ""

while True:
    yn = raw_input(Colors.GREEN + "Does the constructor receive arguments? (y/n): " + Colors.RESET).lower()
    if yn == 'y':
        args = raw_input(Colors.GREEN + "Variables it receives, separated by commas: (e.g.: std::string name, int number):\n" + Colors.RESET)
        break  
    elif yn == 'n':
        args = ""
        break  
    else:
        print (Colors.RED + "Please enter 'y' or 'n'" + Colors.RESET)

create_class_hpp(name, args)
create_class_cpp(name, args)
