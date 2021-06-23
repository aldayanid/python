#!/usr/bin/env python3
stop_word = "stop"
run_word = "run"
start_word = "start"
word=" "
#while word.lower() != stop_word:
while word.lower() not in (stop_word, run_word, start_word):
    word = input("Enter a word: ")
    print(word)
    if word.lower() == start_word:
            print("Starting")
            continue
    elif word.lower() == run_word:
        print("Running")
    elif word.lower() == stop_word:
        print("Bye-bye!")
        break
    else:
        print("Try again")
    # if word.lower() == stop_word:
    #     print("Bye-bye!!!")
    #     break
