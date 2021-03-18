def likedIt(likers):
    lengthLikers = len(likers)

    if lengthLikers == 0:
        return 'Nobody likes this post'
    elif lengthLikers == 1:
        return likers[0] + ' likes this post'
    elif lengthLikers == 2:
        return likers[0] + ' and ' + likers[1] + ' like this post'
    elif lengthLikers == 3:
        return likers[0] + ', ' + likers[1] + ' and ' + likers[2] + ' like this post'
    else:
        return likers[0] + ', ' + likers[1] + ' and ' + str(lengthLikers - 2) + ' others like this post'


print(likedIt(["Mikko", "Francis", "Jorgie", "Brian"]))