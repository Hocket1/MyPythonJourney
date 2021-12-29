print('Welcome to my rollercoaster!')
height = int(input('Enter your height in cm: \n'))
bill = 0
if height >= 120:
    print('you can ride the rollercoaster')
    age = int(input('Enter your age here: \n'))
    if age < 5:
        bill = 5
        print('Child tickets are $5.')
    if age <= 18:
        bill = 7
        print('Youth tickets are $7.')
    else:
        bill = 12
        print('Adult tickets are $12.')
    
    wants_a_photo = (input('Do you want a photo taken? Y or N: \n'))
    if wants_a_photo == 'Y':
        bill +=3
    print(f'Your total bill is {bill}.')
else:
    print('You need to grow taller to ride a rollercoaster')

        
        
