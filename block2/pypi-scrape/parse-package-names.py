with open("pypi_simple.txt", "r") as packages:
    for package in packages:
        package_name = package[package.find(">") + 1:package.rfind("<")]
        print(package_name)