rec={}
def add_and_remove():
        print("________________________________________________\n")
        inp1=input("Enter Movie Name or Enter 'E' to Exit : ")
        if inp1.upper()=="E":
            main()
        try:
            inp2=input("Enter Rating Out Of 10 : ")
            rec[inp1]=int(inp2)
            print("\t")
            print("Movie and Ratings Added")
            add_and_remove()
        except ValueError:
            print("\t")
            print("Invalid Input")
            add_and_remove()


def updatte():
    print("________________________________________________\n")
    inp=(input("Enter The Name Of Movie To Update Rating or Enter 'E' to Exit: "))
    if rec.get(inp)!=None:
        try:
            inp2=int(input("Enter Rating Of The Movie To Update : "))
            rec[inp]=inp2
            print("\t")
            print("Ratings are updated :)")
            main()
        except ValueError:
            print("\t")
            print("Invalid Input :( ")
            updatte()            
    elif inp.upper()=="E":
        main()
    elif rec.get(inp)==None:
        print("\t")
        print("Movie Not Found")
        updatte()


def delete():
    print("________________________________________________\n")
    inp=input("Enter The Movie Name To Delete It's Name and Rating Or Enter 'E' to Exit : ")
    if rec.get(inp)!=None:
        del rec[inp]
        print("\t")
        print("The Movie is Deleted Now")
        main()
    elif inp.upper()=="E":
        main()    
    elif rec.get(inp)==None:
        print("\t")
        print("Invalid Movie Name Entered")
        delete()

def retreive():
    print("________________________________________________\n")
    inp=input("Enter Movie Name To Show It's Rating or Enter 'E' to Exit: ")
    print("\n")
    if rec.get(inp)!=None:
        print("\t")
        print(f"Rating of {inp} is {rec[inp]}.")
        main()
    elif inp.upper()=="E":
        main()
    elif rec.get(inp)==None:
        print("Invalid Movie Name Entered")
        main()

def showall():
    print("________________________________________________\n")
    for k,v in dict.items(rec):
        print(f"The Rating of {k} is {v}.\n")
    main()

def sort():
    print("\t")
    print("________________________________________________\n")
    print("1. Sort from A-Z ")
    print("2. Sort Ratings - High To Low")
    print("3. Exit")
    print("\t")
    inp=input("Enter 1,2 or 3 : ")
    print("\t")
    if inp=="1":
        store=sorted(rec)
        print("Movies                              Ratings")
        print("------------------------------------------")
        for i in store:
            print(f"{i: <37} {rec.get(i)}")
        sort()
    elif inp=="2":
        store2 = sorted(rec.items(), key=lambda item: item[1], reverse=True)
        for k, v in store2:
            print(f"{k:<37}{v}")
        sort()
    elif inp=="3":
        main()
    else:
        print("Invalid Input ")
        sort()


def search():
    print("________________________________________________\n")
    print("\t")
    inp = input("Enter Movies Name to Search or Enter 'E' to Exit : ")
    print("\t")
    if inp == "":
        print("Please Enter Something ....")
        search()
    if inp.upper()=="E":
        main() 

    inp = inp.upper()
    v = len(inp)
    found_movies = []  # List to store matching movies

    for j in rec:
        i = j.upper()
        if i[:v] == inp:
            found_movies.append((j, rec[j]))  # Add matching movie and rating to the list

    if found_movies:
        print("Movies                            Ratings")
        print("----------------------------------------")
        for movie, rating in found_movies:
            print(f"{movie: <30} {rating}")
        search()

    else:
        print("No Movie Found")
        search()


def main():
    print("\t")
    print("________________________________________________\n")
    print("1. Add and Rate Movies")
    print("2. Ratings Update Page")
    print("3. Delete Particular Movie and It's Rating")
    print("4. See Rating of a Particular Movie")
    print("5. See Ratings Of All Movies")
    print("6. Sort Movies")
    print("7. Search Movies\n")
    choice=input("Enter The Option To Perform Action : ")
    if choice=="1":
        add_and_remove()
    elif choice=="2":
        updatte()
    elif choice=="3":
        delete()
    elif choice=="4":
        retreive()
    elif choice=="5":
        showall()
    elif choice=="6":
        sort()
    elif choice=="7":
        search()


main()