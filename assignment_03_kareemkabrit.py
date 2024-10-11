#menu function:
def menu():
    print("Please choose one of the following options: ")
    print("1. Count Digits")
    print("2. Find Max")
    print("3. Count Tags")
    print("4. Exit")
    print("-" * 21)
    return input("Please choose an option ") 


# 1. count digits
def digitcount(n):
    if n < 0:
        n = -n  #positive and negative input wont matter
    return len(str(n))  #switches input to string and counts the length 



# 2. find max
def maxlist(lst):
    return max(lst)


#3. html tag definition

def tagcount(html, tag):
    if not html:  
        return 0
    tag1 = "<" + tag + ">"
    tag2 = "</" + tag + ">"
    count = html.count(tag1) + html.count(tag2)
    index = html.find(tag1)
    if index == -1:
        return count
    return count + tagcount(html[index + len(tag1):], tag)

def main(): #example of html from google
    html_code = """                
   <html>
<head>
    <title>My Simple Page</title>
</head>
<body>
    <h1>Welcome to My Simple Page</h1>
    <p>This is a paragraph of text on my page.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
    <footer>
        <p>Copyright © 2024</p>
    </footer>
</body>
</html>>
    """
    
    while True:
        choice = menu()
        
        if choice == '1':
            num = int(input("Enter an integer: "))
            print("The number of digits is: " + str(digitcount(num)))
        
        elif choice == '2':
            lst = list(map(int, input("Enter a list of integers seperated by a comma ' , ' : ").split(',')))
            print("The maximum number is:  " + str(maxlist(lst)))
        
        elif choice == '3':
            tag = input("Enter an HTML tag (eg. 'li', 'ul', 'p' etc.): ")
            print("The number of",tag, "tags is: " + str(tagcount(html_code, tag)))
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")


main()