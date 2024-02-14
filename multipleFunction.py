class multipleFunction():
    def Subfields():
        print("  Subfields in AI are :")
        lists=['machine learning','netural network','vision','Robotices','speech processing','natural lanuageprocessing']
        for i in lists:
            print(i)
        
    def oddeven():
        num=int(input("Enter the number"))
        if (num%2==0):
            print("the number is even")
        else:
            print("The number is odd")
    def eligiblitymarriage():
    
        gender=input("Enter the your gender :")
        if(gender=='male'):
            age=int(input("Enter your age :"))
            if(age==21):
                print("Eligible")
            else:
                print("not eligible")
        elif(gender=='female'):
            age=int(input("Enter your age :"))
            if(age==18):
                print("Eligible")
            else:
                print("not eligible")

    def percentage():
            subject1=int(input("Enter the subject1 mark:"))
            subject2=int(input("Enter the subject2 mark:"))
            subject3=int(input("Enter the subject3 mark:"))
            subject4=int(input("Enter the subject4 mark:"))
            subject5=int(input("Enter the subject5 mark:"))
            Total=(subject1+subject2+subject3+subject4+subject5)
            percent=(Total/500)*100
            print(percent)
    def triangle():
        height=int(input("Enter the height of triangle:"))
        breath=int(input("Enter the breath of triangle:"))
        Area =(height*breath)/2
        print(Area) 
        height1=int(input("Enter the height1 of triangle:"))
        height2=int(input("Enter the height2 of triangle:"))
        breath1=int(input("Enter the breath of triangle:"))
        perimeter=(height1+height2+breath1)
        print(perimeter)
    
        