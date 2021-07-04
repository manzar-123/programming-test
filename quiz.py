# make a game quiz for 5 questions
# add a limit of 1 tries for each question. 

answer1 = "b"
answer2 = "c"
answer3 = "b"
answer4 = "a"
answer5 = "d"

guess1 = ""
guess2 = ""
guess3 = ""
guess4 = ""
guess5 = ""
guess_count1 = 0
guess_count2 = 0
guess_count3 = 0
guess_count4 = 0
guess_count5 = 0
guess_limit1 = 1
guess_limit2 = 1
guess_limit3 = 1
guess_limit4 = 1
guess_limit5 = 1

out_of_guesses1 = False
out_of_guesses2 = False
out_of_guesses3 = False
out_of_guesses4 = False
out_of_guesses5 = False



score = 0
while guess1 != answer1 and not(out_of_guesses1):
  if guess_count1 < guess_limit1:
    guess1 = input("Question#1\nWhich one of the following is not a programming language?\n(write the option: a, b, c, d) \n(a) Python\n(b) HTML\n(c) R\n(d) Ruby\n\n")
    guess_count1 += 1
    for answer in guess1:
        if answer == answer1:
             score += 1
    print("\nYou got", score, "out of 5\n")
  else:
    out_of_guesses1 = True
     



# question 2


while guess2 != answer2 and not(out_of_guesses2):
  if guess_count2 < guess_limit2:
    guess2 = input("Question#2\n<!DOCTYPE html>\n<html>\n<h2 title='I am a header'>Welcome to our orientation<h2>\n</body>\nCount the errors!! (write the option)\n(a) 1\n(b) 2\n(c) 3\n(d) 4\n\n")
    guess_count2 += 1
    for answer in guess2:
        if answer == answer2:
             score += 1
    print("\nYou got", score, "out of 5\n")
  else:
    out_of_guesses2 = True
     


# question 3

while guess3 != answer3 and not(out_of_guesses3):
  if guess_count3 < guess_limit3:
    guess3 = input("Question#3\nA <- c(23, 123*6, 3566/9, 23/9)\nB <- c(9*9, 9+9998, 7, 234)\nCheck if any component of A or B is less than 55:\n(a) any(A<55 & B<55)\n(b) any(A<55 | B<55)\n(c) all(A<55 | B<55)\n(d) any(A>55 & B>55)\n\n")
    guess_count3 += 1
    for answer in guess3:
        if answer == answer3:
             score += 1
    print("\nYou got", score, "out of 5\n")
  else:
    out_of_guesses3 = True
     

# question 4


while guess4 != answer4 and not(out_of_guesses4):
  if guess_count4 < guess_limit4:
    guess4 = input("Question#4\nWhich of R or SPSS is better for data visualization?\n(a) R\n(b) SQL\n(c) STATA\n(d) SPSS\n\n")
    guess_count4 += 1
    for answer in guess4:
        if answer == answer4:
             score += 1
    print("\nYou got", score, "out of 5\n")
  else:
    out_of_guesses4 = True
     


# question 5


while guess5 != answer5 and not(out_of_guesses5):
  if guess_count5 < guess_limit5:
    guess5 = input("Question#5\nWho were the three people sitting in the lecture hall in \nthe picture on the slide 'Who we are?'\n(a) Javeria Qamar, Javerya Hassan, Russell Seth Martins\n(b) Manzar Abbas, Hajra Arshad, Javerya Hassan\n(c) Javerya Hassan, Javeria Qamar, Hajra Arshad\n(d) Javeria Qamar, Manzar Abbas, Javerya Hassan\n\n")
    guess_count5 += 1
    for answer in guess5:
        if answer == answer5:
             score += 1
    print("\nYou got", score, "out of 5\n")
  else:
    out_of_guesses5 = True
     
