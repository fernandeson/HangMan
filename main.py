import random
from hangman_art import logo, stages_ASCII
from PIL import Image

img0 = Image.open(r"images\stage0.png")
img1 = Image.open(r"images\stage1.png")
img2 = Image.open(r"images\stage2.png")
img3 = Image.open(r"images\stage3.png")
img4 = Image.open(r"images\stage4.png")
img5 = Image.open(r"images\stage5.png")
img6 = Image.open(r"images\stage6.png")
img7 = Image.open(r"images\stage7.png")

stages = [img7, img6, img5, img4, img3, img2, img1, img0]

print(logo)

# CHOOSES RANDOM WORD FROM LIST
word_list = [ 'awkward', 'buffalo', 'cobweb', 'duplex', 'espionage', 'funny', 'galaxy', 'hyphen', 'injury', 'jukebox',
              'kiwifruit', 'luxury', 'matrix', 'nightclub', 'oxygen', 'pneumonia', 'queue', 'rhythm', 'subway',
              'transplant', 'unknown', 'vodka', 'wizard', 'yummy', 'zombie']
chosen_word = random.choice(word_list)

# CREATES AN EMPTY LIST DISPLAYED AS '_' FOR EACH LETTER IN chosen_word
display = []
word_length = len(chosen_word)
for i in range(word_length):
    display.append('_')
print(f"{' '.join(display)}")

lives = 7
end_of_game = False
while not end_of_game:
    # ASK USER TO GUESS A LETTER
    guess = input('Guess a letter: ').lower()
    # CHECK IF THE USER ENTERED A REPEATED GUESS
    if guess in display:
        guess = input(f'You already guessed "{guess}". Guess another letter: ')
    # CHECK IF guess IS PART OF THE chosen_word AND CHANGE '_' FOR guess IF SO
    if guess in chosen_word:
        for i in range(word_length):
            letter = chosen_word[i]
            if guess == letter:
                display[i] = letter
        print(f"{' '.join(display)}")
    elif guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        stages[lives].show()
    # CHECK END OF GAME:
    if '_' not in display:
        end_of_game = True
        print('You Won!')
    elif lives == 0:
        print('You Lost!')
        break
