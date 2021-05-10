book_size = 5
#contact = ['Mom', 'Dad', 'Uncle', 'Sister']
phone_book = [0] * book_size
temp = 0

for i in range(book_size):
    print('Enter contact name:')
    temp = hash (input()) % book_size
    print('Enter contact number:')
    phone_book[temp] = int(input())
#for person in contact:
#   phone_book[(hash(person)) % book_size] = int(input())

print('Enter name to show number:')
print(phone_book[hash (input()) % book_size])
