import truenet

while True:
    text = raw_input("Enter your query: ")
    if text == "q":
        break
    print truenet.analyze(text)
