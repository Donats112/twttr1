def main():
    word= input("Ievadi vārdu: ")
    shorten(word)

def shorten(word):
    short_word=""
    for letter in word:
        if letter  != "a" and letter !="A" and letter !="e" and letter !="E" and letter !="o" and letter !="O" and letter !="i" and letter !="I" and letter !="u" and letter !="U":
            short_word +=letter
    return(short_word)

if __name__ == "__main__":
    main()