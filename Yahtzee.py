import random

# Establish the function for rolling the dice
def rollDice(n):
    round = []
    if n == 0:
        print('You\'ve choosen not to roll any dice this round.')
    else:
        for i in range(0,n):
            roll = str(random.randint(1,6))
            round.append(roll)
        print('You place your ' + str(n) + ' dice into the cup and shake it up good.')
        input()
        input(' *' * n + ' SHAKE' + ' *' * n)
        input(' *' * n + 'K\'SHAKE' + '* ' * n)
        input(' *' * n + 'K\'SHAKE' + '* ' * n)
        print()
        print('You empty the cup of dice onto the table and review your results.')
        return round

# Establish the function to verify user input
def choiceCheck(ch,tr):
    test = ''
    tally = 0
    temp = []
    for i in tr:
        temp.append(i)
    for i in range(len(ch)):
        test = ch[i]
        if test in temp:
            temp.remove(test)
            tally += 1
    if tally != len(ch):
        return False
    else:
        return True

print('  Welcome to \n'
      'Y*A*H*T*Z*E*E! \n')

score = 0

# Beginning the program
while True:

    # Establish the global values
    addPoints = 0
    keep = 0
    dice = 5
    tally = {'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0, 'six': 0}
    key = ''
    choice = []
    round = []
    results = []

    print('Would you like to view the (r)ules, view the (s)core parameters, or (p)lay the game? Enter (q)uit to end it.')
    response = input('> ')

    # Establish the quit path.
    if response == 'q' or response == 'quit':
        quit()

    # Establish the rules path.
    elif response == 'r' or response == 'rules':
        print()
        print('RULES'.center(11,'-'))
        print('You have the choice to roll the dice up to three times, but can stop if you like your current roll.', end='')
        input()
        print('You can either select to keep dice or roll them all again.', end='')
        input()
        print('After your third roll, your score will be tallied and the game will end.',end='')
        input()
        print('You can continue to play and see how high of a score you can get.', end='')
        input()
        print('Try and attain the best score for each round! Here\'s hoping for a YAHTZEE!\n')

    # Establish the score parameters
    elif response == 's' or response == 'score':
        print()
        print('SCORING'.center(13, '-'))
        print('The scoring is based on the dice you hold at the end of the three rounds.\n'
              'The rules for scoring are as follows:')
        input()
        print('DICE TALLY'.center(24,'-') + '\t' +  'SCORE'.center(19,'-'))
        print('3 of a kind'.ljust(24,'.') + 'Total of all 5 dice'.rjust(27))
        print('4 of a kind'.ljust(24, '.') + 'Total of all 5 dice'.rjust(27))
        print('Full house'.ljust(24, '.') + '25 points'.rjust(17))
        print('Small straight'.ljust(24, '.') + '30 points'.rjust(17))
        print('Large straight'.ljust(24, '.') + '40 points'.rjust(17))
        print('YAHTZEE (5 of a kind)'.ljust(24, '.') + '50 points'.rjust(17))
        print('Chance'.ljust(24, '.') + 'Total of all 5 dice'.rjust(27))
        input()

    # Establish the play path.
    elif response == 'p' or response == 'play':
        print('\nROUND ONE!')
        results = rollDice(dice)
        round = results

        # Establish setup for round 2
        response = 'n'
        while response != 'y' or response != 'yes':
            dice = 0
            print()
            print(round)
            print('\nEnter the individual dice value\'s you wish to keep (separated by a comma),\n'
                  'otherwise enter (k)eep to keep all dice or enter (r)oll to roll everything again.\n')
            response = input()
            if response == '':
                print('Please review the results and enter a valid response.')
                response = 'n'
                continue
            elif response == 'r' or response == 'roll':
                keep = len(choice)
                dice = 5 - len(choice)
                print('\nPlease confirm that you have selected to do the following:')
                print('You are keeping ' + str(keep) + ' dice and planning to roll ' + str(dice) + ' for round 2.\n')
                print('Is this correct? (y)es or (n)o')
                response = input('> ')
                if response == 'n' or response == 'no':
                    print('\nYou wish to review the dice again.')
                    continue
                else:
                    round = []
                    break
            elif response == 'k' or response == 'keep':
                keep = 5
                dice = 0
                print('\nPlease confirm that you have selected to keep the following:')
                print(round)
                print('You are keeping 5 dice and planning to roll 0 for round 2.\n')
                print('Is this correct? (y)es or (n)o')
                response = input('> ')
                if response == 'n' or response == 'no':
                    print('\nYou wish to review the dice again.')
                    continue
                elif response == 'y' or response == 'yes':
                    break
                else:
                    print('Invalid response.')
                    continue
            else:
                choice = response.split(',')
                keep = len(choice)
                dice = 5 - len(choice)
                check = choiceCheck(choice,round)
                if not check:
                    print('\nPlease enter a valid selection.')
                    continue
                print('\nPlease confirm that you have selected to keep the following:')
                print(choice)
                print('You are keeping ' + str(keep) + ' dice and planning to roll ' + str(dice) + ' for round 2.\n')
                print('Is this correct? (y)es or (n)o')
                response = input('> ')
                if response == 'n' or response == 'no':
                    print('\nYou wish to review the dice again.')
                    continue
                elif response == 'y' or response == 'yes':
                    round = choice
                    break
                else:
                    print('Invalid response.')
                    continue
        print()
        print('ROUND TWO'.center(15,'-'))
        results = rollDice(dice)
        if results == None:
            pass
        else:
            for i in results:
                round.append(i)

        # Establish setup for round 3
        response = 'n'
        while response == 'n' or response == 'no':
            dice = 0
            print()
            print(round)
            print('\nEnter the individual dice value\'s you wish to keep (separated by a comma),\n'
                  'otherwise enter (k)eep to keep all dice or enter (r)oll to roll everything again.\n')
            response = input()
            if response == '':
                print('Please review the results and enter a valid response.')
                response = 'n'
                continue
            elif response == 'r' or response == 'roll':
                keep = len(choice)
                dice = 5 - len(choice)
                print('\nPlease confirm that you have selected to do the following:')
                print('You are keeping ' + str(keep) + ' dice and planning to roll ' + str(dice) + ' for round 3.\n')
                print('Is this correct? (y)es or (n)o')
                response = input('> ')
                if response == 'n' or response == 'no':
                    print('\nYou wish to review the dice again.')
                    continue
                else:
                    round = []
                    break
            elif response == 'k' or response == 'keep':
                keep = 5
                dice = 0
                print('\nPlease confirm that you have selected to keep the following:')
                print(round)
                print('You are keeping 5 dice and planning to roll 0 for round 3.\n')
                print('Is this correct? (y)es or (n)o')
                response = input('> ')
                if response == 'n' or response == 'no':
                    print('\nYou wish to review the dice again.')
                    continue
                elif response == 'y' or response == 'yes':
                    break
                else:
                    print('Invalid response.')
                    continue
            else:
                choice = response.split(',')
                keep = len(choice)
                dice = 5 - len(choice)
                check = choiceCheck(choice,round)
                if not check:
                    print('\nPlease enter a valid selection.')
                    continue
                print('\nPlease confirm that you have selected to keep the following:')
                print(choice)
                print('You are keeping ' + str(keep) + ' dice and planning to roll ' + str(dice) + ' for round 3.\n')
                print('Is this correct? (y)es or (n)o')
                response = input('> ')
                if response == 'n' or response == 'no':
                    print('\nYou wish to review the dice again.')
                    continue
                elif response == 'y' or response == 'yes':
                    round = choice
                    break
                else:
                    print('Invalid response.')
                    continue
        print()
        print('ROUND THREE'.center(17,'-'))
        results = rollDice(dice)
        if results == None:
            pass
        else:
            for i in results:
                round.append(i)
        input()
        print('Your final dice roll:')
        print(round)
        print('Press enter to view your results.')
        input()

        # Establish setup for scoring
        for i in round:
            if i == '1':
                tally['one'] += 1
            elif i == '2':
                tally['two'] += 1
            elif i == '3':
                tally['three'] += 1
            elif i == '4':
                tally['four'] += 1
            elif i == '5':
                tally['five'] += 1
            elif i == '6':
                tally['six'] += 1

        print('LETS TALLY THE SCORE!'.center(27, '-'))

        for k,v in tally.items():
            print(str(v).ljust(19,'.') + k.rjust(8))

        #for k,v in tally.items():

        # Scoring for a FUll House
        for v in tally.values():
            if v == 3:
                for n in tally.values():
                    counter = 0
                    while counter != 6:
                        if n == 2:
                            print('Full house!')
                            addPoints = 25
                            break
                        else:
                            counter += 1
                if addPoints == 0:
                    for k, v in tally.items():
                        if k == 'one':
                            addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + \
                                        tally['five'] * 5 + tally['six'] * 6
                            print('Three of a kind!')
                            break
                        elif k == 'two':
                            addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + \
                                        tally['five'] * 5 + tally['six'] * 6
                            print('Three of a kind!')
                            break
                        elif k == 'three':
                            addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + \
                                        tally['five'] * 5 + tally['six'] * 6
                            print('Three of a kind!')
                            break
                        elif k == 'four':
                            addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + \
                                        tally['five'] * 5 + tally['six'] * 6
                            print('Three of a kind!')
                            break
                        elif k == 'five':
                            addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + \
                                        tally['five'] * 5 + tally['six'] * 6
                            print('Three of a kind!')
                            break
                        elif k == 'six':
                            addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + \
                                        tally['five'] * 5 + tally['six'] * 6
                            print('Three of a kind!')
                            break
                        else:
                            pass

            # Scoring for 4 of a kind
            if v == 4:
                if k == 'one':
                    addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + tally['five'] * 5 + tally['six'] * 6
                    print('Four of a kind!')
                    break
                elif k == 'two':
                    addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + tally['five'] * 5 + tally['six'] * 6
                    print('Four of a kind!')
                    break
                elif k == 'three':
                    addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + tally['five'] * 5 + tally['six'] * 6
                    print('Four of a kind!')
                    break
                elif k == 'four':
                    addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + tally['five'] * 5 + tally['six'] * 6
                    print('Four of a kind!')
                    break
                elif k == 'five':
                    addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + tally['five'] * 5 + tally['six'] * 6
                    print('Four of a kind!')
                    break
                elif k == 'six':
                    addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + tally['five'] * 5 + tally['six'] * 6
                    print('Four of a kind!')
                    break
                else:
                    pass

            # Scoring for YAHTZEE (5 of a kind)
            if v == 5:
                addPoints = 50
                print('GOT A YAHTZEE!')
                break

            # Scoring for Small Straight
            if tally['one'] == 1 and tally['two'] == 1 and tally['three'] == 1 and tally['four'] == 1 and tally['five'] == 1:
                addPoints = 30
                print('Small Straight!')
                break

            # Scoring for Large Straight
            if tally['six'] == 1 and tally['two'] == 1 and tally['three'] == 1 and tally['four'] == 1 and tally['five'] == 1:
                addPoints = 40
                print('Large Straight!')
                break
                
        # Scoring for Chance
        if addPoints == 0:
            addPoints = tally['one'] * 1 + tally['two'] * 2 + tally['three'] * 3 + tally['four'] * 4 + tally['five'] * 5 + tally['six'] * 6
            print('Score for chance')

        print('Points scored this round:')
        if addPoints == 0:
            print('No dice, grandma! Better luck next time.')
        else:
            print(addPoints)
        score = score + addPoints
        print('SCORE:')
        print(score)
        input()
