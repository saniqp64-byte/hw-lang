
def run(commands: dict):

    try:
        for key, value in commands.items():
            if key == '@':
                key = ''

            if value == 'print':
                print(key)
            elif value == 'input':
                input(key)
    except:
        print("you invalid") 
    