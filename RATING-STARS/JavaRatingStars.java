public class JavaRatingStars{
    public static void main(String[] args) {
        stars(3.5);     // prints 5 full stars

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

