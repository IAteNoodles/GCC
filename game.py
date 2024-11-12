import time
import shutil
import os
from playsound import playsound

# Define paths
source_directory = r"C:\Users\Noodl\Music\Ignite\Clips\GCC"
destination_directory = os.getcwd()

# Final round riddle and cipher
riddle_question_1 = "I’m tall when I’m young, and I’m short when I’m old. What am I?"
correct_answer_1 = "candle"


# Cipher clue: dynamic shifting cipher (Justice League)
cipher_text = "KWVXNIL TYKRGR"
cipher_answer = "JUSTICE LEAGUE"

#First Riddle

# Final round game logic
def final_round():
    print("\nFinal Riddle...")
    time.sleep(1)

    # Step 1: Ask the final riddle
    for attempt in range(1, final_riddle_attempts + 1):
        print(final_riddle_question)
        answer = input("Your answer: ").strip().lower()
        
        if answer == final_riddle_answer:
            # Fake victory message
            print("\nWell done, but you're not done yet!")
            time.sleep(2)
            
            # Play Joker's mocking sound
            print("\nJoker: *Laughs* You solved the riddle... but now, on to the next challenge!")
            playsound('mocking.mp3')  # Path to Joker mocking sound
            
            # Give a hint to the cipher
            print("\nA hint: Shift your perspective with every step.")
            time.sleep(2)
            
            # Step 2: Solve the cipher
            print("\nNow, solve this: The cipher text is 'Jofis Ucfmjf!'")
            print("Use the hint to decipher it.")
            cipher_answer = dynamic_shift_cipher(cipher_text)
            print(f"\nThe ciphered message is: {cipher_answer}")
            
            # Step 3: Play Joker's taunt after cipher is solved
            print("\nJoker: You solved it... but that's not enough, is it? Let's see if you can handle the final challenge!")
            time.sleep(2)
            playsound('mocking.mp3')  # Path to another Joker mocking sound
            
            # Create a hint.txt for the cipher
            with open("hint.txt", "w") as hint_file:
                hint_file.write("Final challenge: The cipher shifts dynamically at each step. The answer is linked to the Justice League.\n")
                hint_file.write("The other name of chaos here is: Kdnxr Gvavjf.")  # Insert the cipher for "chaos"
            
            # Final message before the last challenge
            print("\nGood luck with the next round... if you dare.")
            break
        else:
            print(f"Incorrect. Try again. ({attempt}/{final_riddle_attempts} attempts used)")
        
        if attempt == final_riddle_attempts:
            print("\nYou've reached the maximum attempts. The game is over!")
            break

# Start the final round
final_round()
