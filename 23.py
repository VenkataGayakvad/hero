# menu based program to perform the operation on queue.
def Enqueue(n): 
    L.append(n) 
    if len(L)==1: 
        f=r=L[0] 
    else: 
        r=L[len(L)-1] 
        f=L[0] 
 
def Dequeue(): 
    if len(L)==0: 
        print("Queue is empty") 
    elif len(L)==1: 
        print("Deleted element is: ", L.pop(0)) 
        print("Now queue is empty") 
    else:
        print("Deleted element is: ", L.pop(0))      
         
def Display(): 
    if len(L)==0: 
        print("Queue is empty") 
    else: 
        print(L) 
        r=L[len(L)-1] 
        f=L[0] 
        print("Front is : ", f) 
        print("Rear is : ", r) 
     
def size():   
    print("Size of queue is: ",len(L)) 
 
def FrontRear(): 
    if len(L)==0: 
        print("Queue is empty") 
    else: 
        r=L[len(L)-1] 
        f=L[0] 
        print("Front is : ", f) 
 
        print("Rear is : ", r) 
 
#main program 
L =[] 
print("MENU BASED QUEUE") 
cd=True 
while cd: 
    print(" 1.  ENQUEUE ") 
    print(" 2.  DEQUEUE  ") 
    print(" 3.  Display ") 
    print(" 4.  Size of Queue ") 
    print(" 5.  Value at Front and rear ") 
 
    choice=int(input("Enter your choice (1-5) :  ")) 
     
    if choice==1: 
        val=input("Enter the element: ") 
        Enqueue(val) 
    elif choice==2: 
        Dequeue( ) 
    elif choice==3: 
        Display( ) 
    elif choice==4: 
        size( ) 
    elif choice==5: 
        FrontRear()
    else:   
        print("You enetered wrong choice ") 
    print("Do you want to continue? Y/N") 
    option=input( ) 
    if option=='y' or option=='Y': 
        cd=True 
    else: 
        cd=False
