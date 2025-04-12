def main():
    message = "Hello, World!"
    print(message)
    
    with open("output.txt", "w") as file:
        file.write(message)
    
if __name__ == "__main__":
    main()
