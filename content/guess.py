print('guess a number between 1 to 100')
input('press enter to continue')

lower=1
upper=100

while True:
    mid = (upper - lower)/2.0
    answer = input('is your number higher than ' + str(mid))
    
    if answer == 'y':
        lower = mid