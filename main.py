def sort_on(dict):
    return dict["qty"]

def main():
    letters = {}
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            for char in word.lower():
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1
                
        list_letters = []
        
        for letter in letters:
            list_letters.append({"char": letter, "qty" :letters[letter]})
        
        list_letters.sort(reverse=True, key=sort_on)
                
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found on book")    
        for letter in list_letters:
            print(f"The char {letter["char"]} was found {letter["qty"]} times")
        print("--- End report ---")
main()