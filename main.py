# - you're not like the other doctors.
# + no, and you're not like other patients
import re
from enum import Enum
from colorama import Fore, Style

def main():
    print(
        f"\n\t\t{4 * '-'}be matab khosh amadid{4 * '-'}\n{8 * '-'}gozineh morede nazar khod ra entekhab konid{8 * '-'}")
    print("\n\t\t1- pezeshkan\n\t\t2- bimaran\n\t\t3- exit")

    Which_Option = input(">")

    match Which_Option:
        case '1':
            doctor()

        case '2':
            mariz()

        case '3':
            exit(Style.BRIGHT + "roze khobi dashte bashid 🤍" + Style.RESET_ALL)

        case _:
            print(Fore.RED + "gozineh monaseb ro entekhab konid" + Fore.RESET)
            main()



def doctor():
    global datas
    print("be menu pezeshkan khosh omadid\ngozineh morde nazre khod ra entekhab konid")
    print(
        "\n\t\t1- ezafe kardn pezeshk jadid\n\t\t2- hazf pezeshk\n\t\t3- viraish pezeshk\n\t\t4- joste'joi pezeshk\n\t\t5- list pezeshk\n\t\t6- joste'joi takhasos\n\t\t7- main menu↩")
    Doctor_Option = input()
    match Doctor_Option:
        case '1':
            isNew = str(input("pezeshk jadid\n\ncode pezesh ra vard konid:\t"))
            if findIsUser("doctors.txt", isNew) == "no":

                if total_checker("integer", isNew):
                    datas = isNew + ","
                else:
                    print(Fore.RED + "code pezeshk bayad add sahih bashd\n" + Fore.RESET)
                    doctor()

                name = str(input("\nname pezesh ra vard konid:\t"))
                if total_checker("string", name):
                    datas += name + ","
                else:
                    print(Fore.RED + "name pezesh bayad shamel horof bashad bashad\n" + Fore.RESET)
                    doctor()

                phone = str(input("\nmobile pezesh ra vard konid:\t"))
                if total_checker("mobile", phone):
                    datas += phone + ","
                else:
                    print(Fore.RED + "shomare mobile bayad 11 raghami bashad va ba 09 shoro shavad" + Fore.RESET)
                    doctor()

                specialist = str(input("\ntakhasos pezesh ra vard konid:\n1. cardiologist\n2. optometrist\n3. pediatrician\n4. general\n"))
                if specialist in Specialist._value2member_map_:
                    datas += Specialist._value2member_map_[specialist].name
                else:
                    print(Fore.RED + "takhasos pezesh bayad az bein gozineh haye zir bashad\n" + Fore.RESET)
                    for i in Specialist:
                        print(i.name)
                    doctor()

                TouchMyfile("doctors.txt", f"{datas}\n")

                print(Fore.LIGHTGREEN_EX +"\npezeshke jadid ba movafaghit ezafe shod !\n" + Fore.RESET)
                doctor()

            else:
                print(Fore.RED + "pezeshke morde nazar mojod mibashd\n" + Fore.RESET)
                doctor()

        case '2':
            print("edit pezeshk")

        case '3':
            print("delete pezeshk")

        case '4':
            code = str(input("\ncode pezesh ra vard konid:\t"))
            if total_checker("integer", code):
                print("\n")
                results = search_db("doctors.txt", search_value=code)
                if results:
                    headers = ["code", "name", "mobile", "specialist"]
                    for result in results:
                        values = result.split(',')
                        for header, value in zip(headers, values):
                            print(Fore.LIGHTCYAN_EX + f"-{header}: " + Fore.RESET + Style.DIM + Fore.LIGHTRED_EX + f"{value}" + Style.RESET_ALL + Fore.RESET)
                            print("\n")

                    doctor()

                else:
                    print(Fore.MAGENTA + Style.BRIGHT + "pezeshk mojod nist\n" + Fore.RESET + Style.RESET_ALL)
                    doctor()

            else:
                print(Fore.RED + "code pezeshk bayad add sahih bashd\n" + Fore.RESET)
                doctor()

        case '5':
            pretty_print_lists("doctors.txt")
            doctor()

        case '6':
            print("serch takhasos")

        case '7':
            main()

        case _:
            print(Fore.RED + "gozineh monaseb ro entekhab konid" + Fore.RESET)
            doctor()


def mariz():
    print("be menu mariz khosh omadid\ngozineh morde nazre khod ra entekhab konid")
    print(
        "\n\t\t1- ezafe kardn bimar\n\t\t2- hazfe bimar\n\t\t3- viraish etelaate bimar\n\t\t4- joste'joi bimarhaye ye doctor\n\t\t5- list bimaran\n\t\t6- main menu↩")

    Mariz_gozineh = input()

    match Mariz_gozineh:
        case '1':
            isNew = str(input("bimar jadid\n\ncode meli bimar ra vard konid:\t"))
            if total_checker("code_meli", isNew):
                if findIsUser("marizan.txt", isNew) == "no":
                    datas = isNew + ","

                    name = str(input("\nname bimar ra vard konid:\t"))
                    if total_checker("string", name):
                        datas += name + ","
                    else:
                        print("name bimar bayad shamel horof bashad")
                        mariz()

                    datas += str(input("\npezeshke bimar ra vard konid:\t"))

                    TouchMyfile("marizan.txt", f"{datas}\n")

                    print("\nbimar jadid ba movafaghit ezafe shod !")
                    mariz()

                else:
                    print("bimar morde nazar mojod mibashd")
                    mariz()

            else:
                print("code meli bayad adade 10 raghami bashad")
                mariz()

        case '2':
            print("edit mariz")

        case '3':
            print("delete mariz")

        case '4':
            print("serch marizhaye doctor")

        case '5':
            pretty_print_lists("marizan.txt")
            mariz()

        case '6':
            main()

        case _:
            print(Fore.RED + "gozineh monaseb ro entekhab konid" + Fore.RESET)
            mariz()


def TouchMyfile(Path, datas):
    file = open(Path, "a+")
    file.seek(0)
    file.write(datas)
    file.close()

def findIsUser(file, value):
    with open(file, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines):
        values = line.strip().split(',')
        if value in values:
            return "yes"

    return "no"

def total_checker(type, value):
    patterns = {
        'code_meli': r'^\d{10}$',
        'mobile': r'^09\d{9}$',
        'integer': r'^\d+$',
        'string': r'^[a-zA-Z\s\-\'\.]+$'
    }

    if re.match(patterns[type], value):
        return True


class Specialist(Enum):
    cardiologist = "1"  # heart
    optometrist = "2"  # eye
    pediatrician = "3"  # children
    general = "4"  # omomi

def pretty_print_lists(filename):
    global headers, column_widths
    with open(filename, "r") as file:
        lines = file.readlines()

    if filename == "marizan.txt":
        headers = ["No", "code", "name", "doctor"]
        column_widths = [4, 12, 14, 6]

    elif filename == "doctors.txt":
        headers = ["No", "code", "name", "mobile", "specialist"]
        column_widths = [4, 6, 14, 14, 12]

    separator = " | "
    header_line = separator.join(f"{header:{width}}" for header, width in zip(headers, column_widths))
    divider_line = "-" * len(header_line)

    print(f"{filename.split('.')[0]} file list:")
    print(divider_line)
    print(header_line)
    print(divider_line)

    for idx, line in enumerate(lines, start=1):
        values = line.strip().split(',')
        values.insert(0, str(idx))  # Insert the row number at the beginning
        formatted_line = separator.join(f"{value:{width}}" for value, width in zip(values, column_widths))
        print(formatted_line)
        print(divider_line)

def search_db(filename, search_index=None, search_value=None):
    with open(filename, "r") as file:
        lines = file.readlines()

    results = []

    if search_index is not None and search_value is not None:
        results = [line for line in lines if line.strip().split(',')[search_index] == search_value]
    elif search_value is not None:
        results = [line for line in lines if search_value in line.strip().split(',')]
    elif search_index is not None:
        for line in lines:
            values = line.strip().split(',')
            if len(values) > search_index:
                results.append(values[search_index])

    if results:
        return results


main()
