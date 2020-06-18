import random as rand

experiment_iterations = 2000000

deck = ['2s','2c','2d','2h',
        '3s','3c','3d','3h',
        '4s','4c','4d','4h',
        '5s','5c','5d','5h',
        '6s','6c','6d','6h',
        '7s','7c','7d','7h',
        '8s','8c','8d','8h',          
        '9s','9c','9d','9h',
        'Ts','Tc','Td','Th',
        'Js','Jc','Jd','Jh',
        'Qs','Qc','Qd','Qh',
        'Ks','Kc','Kd','Kh',
        'As','Ac','Ad','Ah']

val_dict = {"1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "T" : 10,
            "J" : 11,
            "Q" : 12,
            "K" : 13,
            "A" : 14}

win_1 = 0
win_2 = 0
win_3 = 0
win_4 = 0
win_5 = 0

conditions = [win_1,win_2,win_3,win_4,win_5]

sec_win_1 = 0
sec_win_2 = 0
sec_win_3 = 0
sec_win_4 = 0
sec_win_5 = 0

sec_conditions = [sec_win_1,sec_win_2,sec_win_3,sec_win_4,sec_win_5]


def useDict(elem):
    return val_dict[elem[0]]


def checkConditions(hand,sec_draw): 
    #Condition 1: royal flush
    roy_flush = ["T","J","Q","K","A"]
    roy_suite = hand[0][1]
    for i in range(len(hand)):
        if hand[i][0] in roy_flush and hand[i][1] == roy_suite:
            roy_flush.remove(hand[i][0])
    if len(roy_flush) == 0:
        #print("Royal")
        conditions[0] += 1
        if sec_draw in hand:
            sec_conditions[0] += 1
        return
    
    #Condition 2: straight flush
    strt_suite = hand[0][1]
    card_values = []
    strt_count = 0

    for i in hand:
        card_values.append(i)
    card_values.sort(key=useDict)

    j = val_dict[card_values[0][0]]

    for i in card_values:
        if val_dict[i[0]] == j and i[1] == strt_suite:
            strt_count += 1
        j += 1

    if strt_count == 5:
        #print("Straight")
        conditions[1] += 1
        if sec_draw in hand:
            sec_conditions[1] += 1
        return

    #Condition 3: four of a kind
    kind_value = val_dict[card_values[0][0]]
    kind_values = 0
    for i in card_values:
        if val_dict[i[0]] == kind_value:
            kind_values += 1
    if kind_values < 4:
        kind_values = 0
        kind_value = val_dict[card_values[1][0]]
        for i in card_values:
            if val_dict[i[0]] == kind_value:
                kind_values += 1
    if kind_values == 4:
        #print("Four of a kind")
        conditions[2] += 1
        if sec_draw in hand:
            sec_conditions[2] += 1
        return

    #Condition 4: full house
    rptd_1 = val_dict[card_values[0][0]]
    rptd_2 = val_dict[card_values[2][0]]
    rpts = 0

    for i in range(len(card_values)):
        if i <= 1:
            if val_dict[card_values[i][0]] == rptd_1:
                rpts += 1
        if i >= 2:
            if val_dict[card_values[i][0]] == rptd_2:
                rpts += 1

    if rpts != 5:
        rpts = 0
        rptd_2 = val_dict[card_values[3][0]]

        for i in range(len(card_values)):
            if i <= 2:
                if val_dict[card_values[i][0]] == rptd_1:
                    rpts += 1
            if i >= 3:
                if val_dict[card_values[i][0]] == rptd_2:
                    rpts += 1
    
    if rpts == 5:
        conditions[3] += 1
        if sec_draw in hand:
            sec_conditions[3] += 1
        return

    #Condition 5: Flush
    kind_suite = hand[0][1]
    kind_suites = 0
    for i in hand:
        if i[1] == kind_suite:
            kind_suites += 1
    if kind_suites == 5:
        conditions[4] += 1
        if sec_draw in hand:
            sec_conditions[4] += 1
        return

def genHand():
    hand = set()
    while len(hand) < 5:
        hand.add(deck[rand.randint(0,51)])
    hand_list = list(hand)
    second_draw = deck[rand.randint(0,51)]
    checkConditions(hand_list,second_draw)

for i in range(experiment_iterations):
    genHand()

j = 1
for i in range(len(conditions)):
    print("Poker Condition",j,":",conditions[i],"|",conditions[i] / experiment_iterations * 100,"%")
    print("Adrian Condition",j,":",sec_conditions[i],"|",sec_conditions[i] / experiment_iterations * 100,"%\n")
    j += 1
    #print(condition_dict[i],"w/ extra draw :",sec_condition_dict[i],"|", sec_condition_dict[i] / experiment_iterations * 100,"%")
