
# recieve a specific postiion and tell if that pos is the answer
def test_location(cards, query, mid):
    
    # gets mid number
    mid_number = cards[mid]
    print("mid:", mid,", mid_number:", mid_number)
    
    # compares mid number with query
    if mid_number == query:
        # checks mid is greater than 0 and if its equal
        if mid-1>= 0 and cards[mid-1]== query:
            return 'left'
        else: 
            return 'found'
    # searches where
    elif mid_number < query:
            return 'left'
    else: 
            return 'right'
            

def locate_card(cards, query):
    
    # low is set to the beginning index
    # high is set to the end of the array
    lo,hi = 0 , len(cards)-1
    
    # if the low index is greater that the high we have exhausted out conditions
    while lo<=hi:
        
        # if not divisible by 2 the double slash returns the quotient
        mid = (lo+hi) // 2
        mid_number = cards[mid]
        result = test_location(cards,query,mid) 
        #prints where wee are in the search
        print("lo:",lo, ", hi:", hi)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
            
    return -1

def main():
    
    cards = [7,6,5,3,2,1,-1]
    
    query = 2
    
    print(locate_card(cards,query))

main()