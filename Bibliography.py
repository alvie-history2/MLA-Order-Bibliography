def myBib():
    Bibliography = []
    inputs = input(' > ')
    if inputs != '':
        Bibliography.append(inputs)
        myBib()

    print('\n'.join(sorted(Bibliography)))

print('When you have entered all your entries, press return.')
myBib()
