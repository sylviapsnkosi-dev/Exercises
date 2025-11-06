#re -code , cashregister

def cashregister(total, payment ):
    # create denominations list of all possible notes and coins from biggest to smallest because we want minimun

    denominations = [200_00, 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00, 50, 20, 10,5]

    # initialize variables
    notes = {}
    amount_due = total
    amount_payed = payment
    change = 0


    # check if customer is eligible for change and check which minimun notes to give them
    if (amount_payed > amount_due):
        change = amount_payed - amount_due
    
    for note in denominations:
        freq = int(change // note)
        # if note goes into change we will give then this note - the number of times it goes to their change
        if freq > 0:
            notes[note] = freq
            change -= note * freq

    return notes
    
    # retrun empty dictionary if they dont have change for whatever reason
    if (amount_due > amount_payed) or (amount_payed < 0) or (amount_due == amount_payed):
        return notes





#test function # something is not right with the code, the change is missing R2 
print(cashregister(250,522))

