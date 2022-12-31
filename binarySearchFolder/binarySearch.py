def locate_card(cards, query):
    
    # low is set to the beginning index
    # high is set to the end of the array
    lo,hi = 0 , len(cards)-1
    
    # if the low index is greater that the high we have exhausted out conditions
    while lo<=hi:
        # if not divisible by 2 the double slash returns the quotient
        mid = (lo+hi) // 2
        mid_number = cards[mid]
        #prints where wee are in the search
        print("lo:",lo, ", hi:", hi,", mid:", mid,", mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def main():
    
    cards = [7,6,5,3,2,1,-1]
    
    query = 2
    
    print(locate_card(cards,query))

main()