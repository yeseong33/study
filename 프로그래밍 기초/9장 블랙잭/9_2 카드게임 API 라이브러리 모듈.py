import random


def fresh_deck():
    suits = {'Spade', 'Heart', 'Diamond', 'Club'}
    ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'}
    deck = []
    for i in suits:
        for j in ranks:
            deck.append((i, j))
    random.shuffle(deck)
    return deck


def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return deck[0], deck[1:]


def show_card(cards, message):
    print(message)
    for card in cards:
        print(' ', card[0], card[1])


def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'


def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        rank = card[1]
        if rank in ['K', 'J', 'Q']:
            rank = 10
            score += rank
        elif rank == 'A':
            rank = 11
            number_of_ace += 1
            score += rank
        else:
            score += rank
    if score > 21 and number_of_ace > 0:
        score -= 10
    return score


def backjack():
    print('Welcome to Softopia Casino')
    deck = fresh_deck()
    chips = 0
    again = 'y'
    while again == 'y':
        dealer = []
        player = []
        for _ in range(2):
            card, deck = hit(deck)
            player.append(card)
            card, deck = hit(deck)
            dealer.append(card)
        print('My cards are:')
        print(' ', '****', '**')
        print(' ', dealer[1][0], dealer[1][1])
        show_card(player, 'Your cards are:')
        score_player = count_score(player)
        score_dealer = count_score(dealer)


        if score_player == 21:
            chips += 2
            show_card(dealer, "Dealer card are:")
            show_card(player, 'Your cards are:')
            print('Black Jack!, player win!')
        elif score_player < 21:
            while more('Do you want get more card?: ') == True:
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                if score_player > 21:
                    show_card(dealer, "Dealer card are:")
                    show_card(player, 'Your cards are:')
                    print('You bust!, dealer win!')
                    break
                print('Dealer cards are:')
                print(' ', '****', '**')
                print(' ', dealer[1][0], dealer[1][1])
                show_card(player, 'Your cards are:')
            if score_player < 21:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                # show_card(dealer, "My card are:")
                if score_dealer > 21:
                    show_card(dealer, "Dealer card are:")
                    show_card(player, 'Your cards are:')
                    chips += 1
                    print('Dealer bust!, player win!')
                elif score_player > score_dealer:
                    show_card(dealer, "Dealer card are:")
                    show_card(player, 'Your cards are:')
                    chips += 1
                    print('player win!')
                elif score_player == score_dealer:
                    show_card(dealer, "dealer card are:")
                    show_card(player, 'Your cards are:')
                    print('draw')
                else:
                    show_card(dealer, "Dealer card are:")
                    show_card(player, 'Your cards are:')
                    chips -= 1
                    print('dealer win!')
        elif score_player > 21:
            show_card(dealer, "Dealer card are:")
            show_card(player, 'Your cards are:')
            chips -= 1
            print('You bust!, dealer win!')
            # break
        again = input('Do you want play again? (y / n): ')
    print('Your chips:',chips)


backjack()