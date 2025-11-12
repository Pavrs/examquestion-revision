# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [linear search]
def one():
    try:
        #list
        nlist= [1,2,3,4,5,6,7,8,9,10]
        print(nlist)
        found = False
        user= int(input('What number do u want out of this list:  '))
        for x in range(len(nlist)):
            if user == nlist[x]:
                print('found')
                found = True
                break
            else:
                print('not found')
            
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [binary search]
def two():
    try:
        nlist = [1,2,3,4,5,6,7,8,9,10]
        print(nlist)
        found= True
        user= int(input('What number do u want out of this list:  '))
        for x in range(len(nlist)):
            #first and last
            first=0
            last=9
            while user== nlist[x]:
                print('within the list')
                middle = (first + last)//2
                if user == nlist[middle]:
                    
                
            
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        one()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
