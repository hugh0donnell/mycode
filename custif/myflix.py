#!/usr/bin/env python3

message = 'You got '

def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0 or value > 100:
            print("Sorry, your response must be an integer between 0 and 100")
            continue
        else:
            break
    return value

# wrap connection in a float() to accept decimals as numbers
score = get_non_negative_int("What was your score on the test?")


if score >= 90:
    message = message + 'an A'
elif score >= 80:
    message = message + 'a B'
elif score >= 70:
    message = message + 'a C'
elif score >= 60:
    message = message + 'a D'
else:
    message = message + 'an F!'

print(message)


