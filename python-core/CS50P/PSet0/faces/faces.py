def main():
    prompt = input()
    print(convert(prompt))

def convert(string):
    string = string.replace(':)', '🙂')
    string = string.replace(':(', '🙁')
    return string

main()
