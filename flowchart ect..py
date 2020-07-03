def course():
    x = input("enter course")
    print("compulsory for all - fundamentals of programming")
    
   if x == "business":
       print(" compulsory: -smart business -systems design and development")
        print(" optional: -computer security -web development")
   
   elif x == "cyber security":
       print(" compulsory: -computer security -web development ")
       print(" optional: -smart business -systems design and development")
   
   elif x == "computing":
       print("compulsory: - systems design and development")
       print("optional: - computer security - smart business - web development")
course()
