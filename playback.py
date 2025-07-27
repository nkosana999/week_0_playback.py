def playback(fast):
    return fast.replace(' ','...')

def main():
    fast = input("Enter your voice: ")
    print(playback(fast))

main()