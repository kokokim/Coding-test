grade=input()
rating=0.0

if grade[0]=='A':
    rating+=4.0
elif grade[0]=='B':
    rating+=3.0
elif grade[0]=='C':
    rating+=2.0
elif grade[0]=='D':
    rating+=1.0

if grade[-1]=='+':
    rating+=0.3
elif grade[-1]=='-':
    rating-=0.3
    
print(rating) 