import os

from bs4 import BeautifulSoup

languages = {"Haskell": ".hs", "Python": ".py", "C": ".c", "C++": ".cpp"}


def remove_forbidden(file_name):
    forbidden_chars = '<>:"?/\\?*'
    for char in forbidden_chars:
        file_name = file_name.replace(char, "-")
    return file_name


while True:
    codewars_directory = input("Which directory would you like to download your tasks to?\n")
    if codewars_directory in [x for x in os.listdir() if os.path.isdir(x)]:
        break
    else:
        check_new = input("This directory does not exist! Would you like to create this directory? (y/n)\n")
        if check_new.lower() == "y":
            codewars_directory = remove_forbidden(codewars_directory)
            os.mkdir(codewars_directory)
            break
        else:
            continue

html_file = input("Please enter the HTML file where your solutions are stored:\n")
html_file += ".html" if ".html" not in html_file else ""

with open(html_file, "r") as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')

solution_list = soup.prettify().split("""<div class="list-item solutions">""")

os.chdir(codewars_directory)

for solution in solution_list[1:]:
    sub_soup = BeautifulSoup(solution, 'html.parser')
    sub_soup_name = sub_soup.a.get_text().split("\n")[1].strip()
    sub_soup_level = sub_soup.span.get_text().split("\n")[1].strip()
    sub_soup_language = sub_soup.h6.get_text().split("\n")[1].strip()[:-1]
    sub_soup_code = sub_soup.pre.get_text()
    # print("+++++++++++++++\n")
    # print("Task:", sub_soup_name)
    # print("Level:", sub_soup_level)
    # print("Language:", sub_soup_language)
    # print("Code:\n", sub_soup_code, "\n")

    if sub_soup_language not in [x for x in os.listdir() if os.path.isdir(x)]:
        os.mkdir(sub_soup_language)
    os.chdir(sub_soup_language)

    if sub_soup_level not in [x for x in os.listdir() if os.path.isdir(x)]:
        os.mkdir(str(sub_soup_level))
    os.chdir(sub_soup_level)

    current_file_name = str(os.getcwd()) + "/" + remove_forbidden(str(sub_soup_name + languages[sub_soup_language]))

    try:
        with open(current_file_name, "x") as new_file:
            new_file.write(sub_soup_code)

    except FileExistsError:
        print("-" * len(current_file_name))
        print(current_file_name, "already exists!")
        print("-" * len(current_file_name) + "\n")

    os.chdir("..")
    os.chdir("..")
