# while basically lets you start a loop
loopcontinue = 1
loopcount = 0
while loopcontinue == 1:
    # += adds given value to existing one
    loopcount += 1
    print(loopcount)
    if loopcount == 20:
        # break stops the loop
        break
    if loopcount == 10:
        # can also make the while check come back false which will stop the loop
        loopcontinue = 0
