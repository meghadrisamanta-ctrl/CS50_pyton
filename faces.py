def convert(word):
    converted = word.replace(":)","😊").replace(":(","😢")
    return converted

def main():
    word = input("Enter: ")
    change = convert(word)
    print(change)
    
main()
    