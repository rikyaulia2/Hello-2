import time

def hello():
    message = "Hello, World!"
    print(message)
    time.sleep(1)  # Pause for 1 second
    return message

if __name__ == "__main__":
    hello()
