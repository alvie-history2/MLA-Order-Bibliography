def myBib():
    Bibliography = []
    inputs = input(' > ')
    if inputs != '':
        charOne = inputs[:1]
        if(charOne == ' '):
            if(len(inputs) == 1):
                print("Error, you inputted just a space. Please input a full line. If you are done, press return")
            inputs = inputs[1:]
        else:
            inputs = inputs[0:]

        Bibliography.append(inputs)
        myBib()

    print('\n'.join(sorted(Bibliography)))

print('When you have entered all your entries, press return.')
myBib()
