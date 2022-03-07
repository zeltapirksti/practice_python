# exercise 1

username = input("What is your name? ")
print(f"{username[::-1].capitalize()}, a thorough mess is it not {username[0]}?")

#####################################################
# exercise 2

p1_text = input("First player enters the test: ")
print(p1_text)
print(len(p1_text) * "*")

p2_input = input("Second player guesses a letter: ")
new_string = ""
for i in enumerate(p1_text):
    if i[1] == " ":
        new_string += i[1]
    elif i[1] != p2_input:
        new_string += "*"
    else:
        new_string += i[1]
print(new_string)

#####################################################
# exercise 3
bad_text = input("Please input text: ")
# bad_text = "This cottage cheese is not so bad"
print(bad_text)
start_location = bad_text.find("not")
# print(start_location)
end_location = bad_text.find("bad")
# print(end_location)
good_str = ""
if end_location > start_location:
    good_str = (f"{bad_text[0:bad_text.find('not')]}good")
else:
    good_str = bad_text
print(good_str)
