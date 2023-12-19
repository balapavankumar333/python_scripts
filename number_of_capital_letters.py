
def count_letter():

    """
    Count the number of uppercase letters in a file and print the result.
    """

    try:
        file = open("Sample.txt", "r")
        data = file.read()
        count = 0
        for letter in data:
            if letter.isupper():
                count += 1
        print(f"Total uppercase letters found in the file: {count}")
        file.close()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_letter()
