from rich.console import Console
import platform

def logicalToStrConverter(logic):
    return "yes" if logic else "no"

def Menu(modes):
    console.rule("[bold yellow] Menu")
    for option in options:
        print(str(options.index(option)) + ") [ " + logicalToStrConverter(modes[option]) + " ]: " + option)
    print(str(len(options)) + "): Proceed")

def getUserChoice(modes):
    Menu(modes)
    return int(input("Choose the option by number: "))

def buildModes():
    modes = {}
    for option in options:
        modes[option] = False
    return modes

def proceed(choice):
    match choice:
        case 0:
            dataFile.write("Processor: " + str(platform.processor()) + "\n")
        case 1:
            dataFile.write("Architecture: " + str(platform.architecture()) + "\n")
        case 2:
            dataFile.write("System name: " + str(platform.system()) + "\n")
        case 3:
            dataFile.write("Network name: " + str(platform.node()) + "\n")
        case 4:
            dataFile.write("System realese: " + str(platform.release()) + "\n")
        case 5:
            dataFile.write("System version: " + str(platform.version()) + "\n")
        case 6:
            dataFile.write("Machine type: " + platform.machine() + "\n")
        case 7:
            dataFile.write("All from 2 to 6: " + str(platform.uname()) + "\n")
        case 8:
            dataFile.write("Python build number and date: " + str(platform.python_build()) + "\n")
        case 9:
            dataFile.write("Python compiler: " + str(platform.python_compiler()) + "\n")
        case 10:
            dataFile.write("Python implementation: " + str(platform.python_implementation()) + "\n")
        case 11:
            dataFile.write("Python version: " + str(platform.python_version()) + "\n")

def start():
    modes = buildModes()
    while True:
        choice = getUserChoice(modes)
        proceed(choice)
        if choice == len(options):
            dataFile.close()
            console.rule("[bold red] Result of your choice in OSDetails.txt")
            break
        else:
            modes[options[choice]] = not modes[options[choice]]

console = Console()
options = ("Processor", "Architecture", "System name", "Network name", "System realese", "System version", "Machine type", "All from 2 to 6", "Python build number and date", "Python compiler", "Python implementation", "Python version")
dataFile = open(r"c:\Users\user\NG_2022_Alexey_Tkachenko\Lesson_4\OSDetails.txt", "w")
start()