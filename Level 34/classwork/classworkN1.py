def validate_hello(greetings):
    hellos = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    
    greetings = greetings.lower()

    for word in hellos:
        if word in greetings:
            return True

    return False