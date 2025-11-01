public class JavaRatingStars{
    public static void main(String[] args) {
        stars(5);     // prints 5 full stars
        stars(3.5);   // prints 3 full stars and 1 half star
        stars(0.5);   // prints 1 half star
        stars(0);     // prints nothing
    }

    public static void stars(double rate) {
        double num;

        if (rate > 0 && rate <= 5) {
            num = rate;
        } else {
            return;
        }

        // print full stars
        while (num >= 1) {
            System.out.println("full");
            num -= 1;
        }

        // print half star if remaining num >= 0.5
        if (num >= 0.5) {
            halfStar(num);
            num -= 0.5;
        }

        // any remaining less than 0.5 is ignored
    }

    // print half star
    public static void halfStar(double num) {
        System.out.println("half");
    }
}

