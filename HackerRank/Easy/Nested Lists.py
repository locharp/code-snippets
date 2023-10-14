if __name__ == "__main__":
    students = []
    
    for _ in range( int( input() ) ):
        name = input()
        score = float( input() )

        students.append( [ name, score ] )

    second_lowest = sorted( set( student[1] for student in students ) )[1]

    for student in sorted( students ):
        if student[1] == second_lowest:
            print( student[0] )
