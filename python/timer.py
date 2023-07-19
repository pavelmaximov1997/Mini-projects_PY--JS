import time

timer = int(input('How long should the counter work? Enter seconds: '))

for x in reversed(range(0, timer + 1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f'{hours:02}.{minutes:02}.{seconds:02}', end='\r' )
    time.sleep(2)
print('Your time has come to an end...')