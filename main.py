# - you're not like the other doctors.
# + no, and you're not like other patients
import re
from enum import Enum
from colorama import Fore, Style

def main():
    print(f"\n\t\t{4 * '-'}be matab khosh amadid{4 * '-'}\n{8 * '-'}gozineh morede nazar khod ra entekhab konid{8 * '-'}")
    print("\n\t\t1- pezeshkan\n\t\t2- bimaran\n\t\t3- exit")

    Which_Option = input(Fore.LIGHTYELLOW_EX + ">" + Fore.RESET)

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
    print("\nbe menu pezeshkan khosh omadid\ngozineh morde nazre khod ra entekhab konid")
    print("\n\t\t1- ezafe kardn pezeshk jadid\n\t\t2- hazf pezeshk\n\t\t3- viraish pezeshk\n\t\t4- joste'joi pezeshk\n\t\t5- list pezeshk\n\t\t6- joste'joi takhasos\n\t\t7- main menu↩")
    Doctor_Option = input(Fore.LIGHTYELLOW_EX + ">" + Fore.RESET)
    match Doctor_Option:
        case '1':
            isNew = str(input("pezeshk jadid\n\ncode pezesh ra vard konid:\t"))
            if findIsUser("doctors.txt", isNew) == "no":

                if total_checker("integer", isNew):
                    datas = isNew + ","
                else:
                    print(Fore.RED + "\ncode pezeshk bayad add sahih bashd\n" + Fore.RESET)
                    doctor()

                name = str(input("\nname pezesh ra vard konid:\t"))
                if total_checker("string", name):
                    datas += name + ","
                else:
                    print(Fore.RED + "\nname pezesh bayad shamel horof bashad bashad [A-Z/a-z/-/'/.]\n" + Fore.RESET)
                    doctor()

                phone = str(input("\nmobile pezesh ra vard konid:\t"))
                if total_checker("mobile", phone):
                    datas += phone + ","
                else:
                    print(Fore.RED + "\nshomare mobile bayad 11 raghami bashad va ba 09 shoro shavad\n" + Fore.RESET)
                    doctor()

                specialist = str(input("\ntakhasos pezesh ra vard konid:\n1. cardiologist\n2. optometrist\n3. pediatrician\n4. general\n"))
                if specialist in Specialist._value2member_map_:
                    datas += Specialist._value2member_map_[specialist].name
                else:
                    print(Fore.RED + "\ntakhasos pezesh bayad az bein gozineh haye zir bashad\n" + Fore.RESET)
                    for i in Specialist:
                        print(Fore.LIGHTBLUE_EX + i.name + Fore.RESET)
                    doctor()

                TouchMyfile("doctors.txt", f"{datas}\n")

                print(Fore.LIGHTGREEN_EX +"\npezeshke jadid ba movafaghit ezafe shod !\n" + Fore.RESET)
                doctor()

            else:
                print(Fore.MAGENTA + "\npezeshke morde nazar mojod mibashd\n" + Fore.RESET)
                doctor()

        case '2':
            code = str(input("\ncode pezesh ra vard konid:\t"))
            if total_checker("integer", code):
                results = search_db("doctors.txt", search_value=code)
                if results:
                    with open("doctors.txt", "r+") as file:
                        lines = file.readlines()
                        file.close()
                    lines = list(filter(lambda line: line not in results, lines))
                    with open("doctors.txt", "w+") as file:
                        file.writelines(lines)
                        file.close()

                    headers = ["code", "name", "mobile", "specialist"]
                    for result in results:
                        values = result.split(',')
                        for header, value in zip(headers, values):
                            print(Fore.LIGHTCYAN_EX + f"-{header}: " + Fore.RESET + Style.DIM + Fore.LIGHTRED_EX + f"{value}" + Style.RESET_ALL + Fore.RESET)
                    print("\n")
                    print(Fore.LIGHTGREEN_EX + "\npezeshk hazf shod\n" + Fore.RESET)
                    doctor()

                else:
                    print(Fore.MAGENTA + "\npezeshk mojod nist\n" + Fore.RESET)
                    doctor()

            else:
                print(Fore.RED + "\ncode pezeshk bayad add sahih bashd\n" + Fore.RESET)
                doctor()

        case '3':
            code = str(input("\ncode pezesh ra vard konid:\t"))
            if total_checker("integer", code):
                results = search_db("doctors.txt", search_value=code)

                if results:
                    with open("doctors.txt", "r+") as file:
                        lines = file.readlines()
                        file.close()
                    lines = list(filter(lambda line: line not in results, lines))
                    with open("doctors.txt", "w+") as file:
                        file.writelines(lines)
                        file.close()

                    datas = code + ","
                    name = str(input("\nname jadide pezesh ra vard konid:\t"))
                    if total_checker("string", name):
                        datas += name + ","
                    else:
                        print(Fore.RED + "\nname pezesh bayad shamel horof bashad bashad [A-Z/a-z/-/'/.]\n" + Fore.RESET)
                        doctor()

                    phone = str(input("\nmobile jadid pezesh ra vard konid:\t"))
                    if total_checker("mobile", phone):
                        datas += phone + ","
                    else:
                        print(Fore.RED + "\nshomare mobile bayad 11 raghami bashad va ba 09 shoro shavad\n" + Fore.RESET)
                        doctor()

                    specialist = str(input("\ntakhasos jadid pezesh ra vard konid:\n1. cardiologist\n2. optometrist\n3. pediatrician\n4. general\n"))
                    if specialist in Specialist._value2member_map_:
                        datas += Specialist._value2member_map_[specialist].name
                    else:
                        print(Fore.RED + "\ntakhasos pezesh bayad az bein gozineh haye zir bashad\n" + Fore.RESET)
                        for i in Specialist:
                            print(Fore.LIGHTBLUE_EX + i.name + Fore.RESET)
                        doctor()

                    TouchMyfile("doctors.txt", f"\n{datas}\n")
                    empty_lines("doctors.txt")

                    print("Original " + Fore.LIGHTCYAN_EX + code + Fore.RESET + " information:\n")
                    headers = ["code", "name", "mobile", "specialist"]
                    for result in results:
                        values = result.split(',')
                        for header, value in zip(headers, values):
                            print(Fore.LIGHTWHITE_EX + Style.DIM + f"-{header}: " + Style.RESET_ALL + Fore.RESET + Fore.LIGHTRED_EX + f"{value}" + Fore.RESET)
                    print("\n")
                    print("Updated " + Fore.LIGHTCYAN_EX + code + Fore.RESET + " information:\n")
                    headers = ["code", "name", "mobile", "specialist"]
                    for header, value in zip(headers, datas.split(',')):
                        print(Fore.LIGHTWHITE_EX + Style.DIM + f"-{header}: " + Fore.RESET + Style.RESET_ALL + Fore.LIGHTGREEN_EX + f"{value}" + Fore.RESET)
                    print("\n")

                    doctor()

                else:
                    print(Fore.MAGENTA + "\npezeshk mojod nist\n" + Fore.RESET)
                    doctor()

            else:
                print(Fore.RED + "\ncode pezeshk bayad add sahih bashd\n" + Fore.RESET)
                doctor()

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
                    print(Fore.MAGENTA + Style.BRIGHT + "\npezeshk mojod nist\n" + Fore.RESET + Style.RESET_ALL)
                    doctor()

            else:
                print(Fore.RED + "\ncode pezeshk bayad add sahih bashd\n" + Fore.RESET)
                doctor()

        case '5':
            pretty_print_lists_and_search(filename="doctors.txt")
            print("\n")
            doctor()

        case '6':
            specialist = str(input("\ntakhasos pezesh ra vard konid:\n1. cardiologist\n2. optometrist\n3. pediatrician\n4. general\n"))
            if specialist in Specialist._value2member_map_:
                specialist_name = Specialist._value2member_map_[specialist].name
                results = search_db("doctors.txt", search_value=specialist_name)
                if results:
                    print(Style.DIM + Fore.LIGHTRED_EX + f"\n{specialist_name}" + Fore.RESET + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " list:\n" + Fore.RESET)
                    pretty_print_lists_and_search(array=results)
                    print("\n")
                    doctor()
                else:
                    print(Fore.LIGHTCYAN_EX + "\npezeshke " + Fore.RESET + Style.DIM + Fore.LIGHTRED_EX + f"{specialist_name}" + Fore.RESET + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " mojod nist\n" + Fore.RESET)
                    doctor()
            else:
                print(Fore.RED + "\ngozineh monaseb ro entekhab konid\n" + Fore.RESET)
                doctor()

        case '7':
            main()

        case _:
            print(Fore.RED + "\ngozineh monaseb ro entekhab konid\n" + Fore.RESET)
            doctor()


def mariz():
    print("\nbe menu mariz khosh omadid\ngozineh morde nazre khod ra entekhab konid")
    print("\n\t\t1- ezafe kardn bimar\n\t\t2- hazfe bimar\n\t\t3- viraish etelaate bimar\n\t\t4- joste'joi bimarhaye ye doctor\n\t\t5- list bimaran\n\t\t6- main menu↩")

    Mariz_gozineh = input(Fore.LIGHTYELLOW_EX + ">" + Fore.RESET)

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
                        print(Fore.RED + "name bimar bayad shamel horof bashad" + Fore.RESET)
                        mariz()

                    code_pezeshk =  str(input("\npezeshke bimar ra vard konid:\t"))
                    if total_checker("integer", code_pezeshk):
                        if findIsUser("doctors.txt", code_pezeshk) == "yes":
                            datas += code_pezeshk + ";"
                        else:
                            print(Fore.RED + "\npezeshk mojod nist\n" + Fore.RESET)
                            mariz()

                    TouchMyfile("marizan.txt", f"{datas}\n")

                    print(Fore.LIGHTGREEN_EX + "\nbimar jadid ba movafaghit ezafe shod !\n" + Fore.RESET)
                    mariz()

                else:
                    print(Fore.MAGENTA + "\nbimar morde nazar mojod mibashd\n" + Fore.RESET)
                    mariz()

            else:
                print(Fore.RED + "\ncode meli bayad adade 10 raghami bashad\n" + Fore.RESET)
                mariz()

        case '2':
            code = str(input("\ncode meli bimar ra vard konid:\t"))
            if total_checker("code_meli", code):
                results = search_db("marizan.txt", search_value=code)
                if results:
                    with open("marizan.txt", "r+") as file:
                        lines = file.readlines()
                        file.close()
                    lines = list(filter(lambda line: line not in results, lines))
                    with open("marizan.txt", "w+") as file:
                        file.writelines(lines)
                        file.close()

                    headers = ["code", "name", "doctor"]
                    for result in results:
                        values = result.split(',')
                        for header, value in zip(headers, values):
                            print(Fore.LIGHTCYAN_EX + f"-{header}: " + Fore.RESET + Style.DIM + Fore.LIGHTRED_EX + f"{value}" + Style.RESET_ALL + Fore.RESET)
                    print("\n")
                    print(Fore.LIGHTGREEN_EX + "\nbimar hazf shod\n" + Fore.RESET)
                    mariz()

                else:
                    print(Fore.MAGENTA + "\nbimar mojod nist\n" + Fore.RESET)
                    mariz()

            else:
                print(Fore.RED + "\ncode meli bayad adade 10 raghami bashad\n" + Fore.RESET)
                mariz()

        case '3':
            code = str(input("\ncode meli bimar ra vard konid:\t"))
            if total_checker("code_meli", code):
                results = search_db("marizan.txt", search_value=code)
                if results:
                    with open("marizan.txt", "r+") as file:
                        lines = file.readlines()
                        file.close()
                    lines = list(filter(lambda line: line not in results, lines))
                    with open("marizan.txt", "w+") as file:
                        file.writelines(lines)
                        file.close()

                    datas = code + ","
                    name = str(input("\nname jadide bimar ra vard konid:\t"))
                    if total_checker("string", name):
                        datas += name + ","
                    else:
                        print(Fore.RED + "\nname bimar bayad shamel horof bashad bashad [A-Z/a-z/-/'/.]\n" + Fore.RESET)
                        mariz()

                    code_pezeshk = str(input("\npezeshke bimar ra vard konid:\t"))
                    if total_checker("integer", code_pezeshk):
                        if findIsUser("doctors.txt", code_pezeshk) == "yes":
                            datas += code_pezeshk + ";"
                            TouchMyfile("marizan.txt", f"\n{datas}\n")
                            empty_lines("marizan.txt")
                        else:
                            print(Fore.RED + "\npezeshk mojod nist\n" + Fore.RESET)
                            mariz()

                    print("Original " + Fore.LIGHTCYAN_EX + code + Fore.RESET + " information:\n")
                    headers = ["code meli", "name", "doctor"]
                    for result in results:
                        values = result.split(',')
                        for header, value in zip(headers, values):
                            print(Fore.LIGHTWHITE_EX + Style.DIM + f"-{header}: " + Style.RESET_ALL + Fore.RESET + Fore.LIGHTRED_EX + f"{value}" + Fore.RESET)
                    print("\n")
                    print("Updated " + Fore.LIGHTCYAN_EX + code + Fore.RESET + " information:\n")
                    headers = ["code meli", "name", "doctor"]
                    for header, value in zip(headers, datas.split(',')):
                        print(Fore.LIGHTWHITE_EX + Style.DIM + f"-{header}: " + Fore.RESET + Style.RESET_ALL + Fore.LIGHTGREEN_EX + f"{value}" + Fore.RESET)
                    print("\n")

                    mariz()

                else:
                    print(Fore.MAGENTA + "\nbimar mojod nist\n" + Fore.RESET)
                    mariz()

            else:
                print(Fore.RED + "\ncode meli bayad adade 10 raghami bashad\n" + Fore.RESET)
                mariz()

        case '4':
            print("serch marizhaye doctor")

        case '5':
            pretty_print_lists_and_search(filename="marizan.txt")
            print("\n")
            mariz()

        case '6':
            main()

        case _:
            print(Fore.RED + "\ngozineh monaseb ro entekhab konid\n" + Fore.RESET)
            mariz()


def TouchMyfile(Path, datas):
    file = open(Path, "a+")
    file.seek(0)
    file.write(datas)
    file.close()

def findIsUser(file, value):
    with open(file, "r") as file:
        lines = file.readlines()
        file.close()
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
        'string': r'^[a-zA-Z \-\'\.]+$'
    }

    if re.match(patterns[type], value):
        return True

class Specialist(Enum):
    cardiologist = "1"  # heart
    optometrist = "2"  # eye
    pediatrician = "3"  # children
    general = "4"  # omomi

def search_db(filename, search_index=None, search_value=None):
    with open(filename, "r") as file:
        lines = file.readlines()
        file.close()

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


def pretty_print_lists_and_search(filename=None, array=None):
    if filename:
        with open(filename, "r") as file:
            file_lines = file.readlines()
            file.close()
        file_lines = sorted(file_lines, key=lambda x: x.strip().split(',')[2])
    else:
        file_lines = array

    if filename == "marizan.txt":
        headers = ["No", "code meli", "name", "doctor"]
        column_widths = [4, 12, 14, 26]
    elif filename == "doctors.txt" or (array and not filename):
        headers = ["No", "code", "name", "mobile", "specialist"]
        column_widths = [4, 12, 14, 14, 12]

    separator = " | "
    header_line = separator.join(f"{header:{width}}" for header, width in zip(headers, column_widths))
    divider_line = "-" * len(header_line)

    if filename:
        print(f"{filename.split('.')[0]} file list:")
    print(divider_line)
    print(header_line)
    print(divider_line)

    for idx, line in enumerate(file_lines, start=1):
        values = line.strip().split(',')
        values.insert(0, str(idx))
        formatted_line = separator.join(f"{value:{width}}" for value, width in zip(values, column_widths))
        print(formatted_line)
        print(divider_line)

def empty_lines(filename):
    if filename:
        with open(filename, "r") as file:
            lines = file.readlines()
            file.close()
        lines = [line for line in lines if line.strip()]

        with open(filename, "w") as file:
            file.writelines(lines)
            file.close()


main()
#sorte list ha a-z / fix ",") / fix ; list and outputs / fix virayesh mariz to not delete /