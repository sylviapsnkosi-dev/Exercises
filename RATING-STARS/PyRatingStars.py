def printing_full(num):

    #1 . Ensure the number passed in in only between 0 and 5, not zero is not included
    if num <= 5 and num > 0:
        stars = round(float(num),2)
    else:
        return ""

    # 3 this function will handle full stars, expected case and will call itself if condition is still true else it will call the lower method half
    if stars >= 1:
        print('full')
        stars -= 1

        if stars >= 1:
            printing_full(stars)
            
        elif stars < 1 and stars >= 0.50:
            printing_half(stars)

    # note if the initial stars is never above 1 and not below condition for lower method we call it right away
    elif stars < 1 and stars >= 0.50:
        printing_half(stars)

    return ""
            

# 2 function that will handling half a star
def printing_half(stars):
    if stars >= 0.50:
        print("half") 
        stars -= 0.50
    return ""

print(printing_full(4.80))
    

#how to round off to the neareset numbers rounding off 2 decimal places, 4,96 should 5


# TRANSLATE FUNCTION INTO JAVA FUNCTION
#1 . # 1 Ensure the number passed in in only between 0 and 5, not zero is not included
#2 . # 2 function that will handling half a star
#3 . # 3 this function will handle full stars, expected case and will call itself if condition is still true else it will call the lower method half


static void stars(int num){

    #1 . # 1 Ensure the number passed in in only between 0 and 5, not zero is not included
    if num <= 5 && num > 0{
        int stars = double(num);
    }else{
        return "";
    }
    # 3 this function will handle full stars, expected case and will call itself if condition is still true else it will call the lower method half
    static void printingFull(stars){
        if stars > 1{
            System.out.println("full");
            stars -= 1;

            if stars > 1{
                printingFull(stars);
            }else if stars < 1 && stars >= 0.50{
                printingHalf(stars);
            }
        }else if stars < 1 && stars >= 0.50{
            printingHalf(stars);
        }
        return "";
    }

    # 2 function that will handling half a star
    static String printingHalf(stars){
        if stars < 1 && stars >= 0.50{
            System.out.println("half");
            stars -= 0.50;
        }
    }
}


# LEARNING OBJECTIVES
# how to round off to the neareset numbers rounding off 2 decimal places, 4,96 should 5