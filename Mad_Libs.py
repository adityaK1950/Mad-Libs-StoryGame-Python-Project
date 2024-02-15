playing = input("Let's Play a Story Game, Yes/No\n")

if playing.lower() != "yes":
    quit()

print("\nGreat! Get ready for an exciting adventure! 🚀")

noun1 = input("Enter Your Heroic Name: ")
noun2 = input("Enter the Sidekick's Name: ")
noun3 = input("Enter the Friendly Creature's Name: ")
place = input("Enter a Mystical Place Name: ")
adjective1 = input("Describe the place in one word: ")
adjective2 = input("Give an Epic Adjective: ")
adjective3 = input("Choose a Magical Adjective: ")
adverb1 = input("Describe how you move (e.g., gracefully): ")
adverb2 = input("Describe a celebration action (e.g., cheerfully): ")
Exclamation = input("Enter an Exciting Exclamation: ")

# Start the Story
print(
    f"\nOnce upon a time, in the enchanted land of {place},"
    f"\n{noun1} embarked on an extraordinary journey. "
    f"\nFeeling the {adjective1} atmosphere, {noun1} decided to summon {noun2} and {noun3} to join the quest. "
    f"\nAs they arrived, they shared a shocking revelation - a {adjective2} event had occurred. "
    f"\nSwiftly and {adverb1}, {noun1} led the trio towards the mysterious incident. "
    f"\nTo their astonishment, they discovered {noun3}'s daring rescue from the edge of a mystical cliff. "
    f"\nOverwhelmed with relief, {noun1} exclaimed, '{Exclamation}' but deep down, felt a sense of {adjective3}. "
    f"\nWith courage, {noun1} saved the day, and they celebrated {adverb2} under the magical moonlight. "
    f"\nLaughter echoed through the enchanted land as they forged unforgettable memories."
)

print("\nCongratulations! You've created an enchanting story. 📜✨")
