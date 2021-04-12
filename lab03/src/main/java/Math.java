public class Math {

    public int sumChar(char a, char b){
        return a + b;
    }

    public int subChar(char a, char b){
        return a - b;
    }

    public boolean charComparison(char a, char b){
        if(a > b){
            System.out.println(a + " is bigger than " + b);
            return a > b;
        }
        else {
            if(a < b){
                System.out.println(a + " is lower than " + b);
                return a < b;
            }
            else {
                System.out.println(a + " is equal to " + b);
                return false;
            }
        }
    }

    public int divideInt(int a, int b) {
        try {
            return a/b;
        } catch (ArithmeticException arithmeticException) {
            System.out.println("No dividing by 0.");
        }
        return 0;
    }

    public boolean compareLengthOfStrings(String text01, String text02){
        return text01.length() > text02.length();
    }

    public int getStringLengthDifference(String text01, String text02){
        return text01.length() - text02.length();
    }

    public boolean primeNumber(int a){

        boolean isPrimeNumber = true;
        for (int i = 2; i <= a / 2; ++i) {
            if (a % i == 0) {
                isPrimeNumber = false;
                break;
            }
        }
        if(isPrimeNumber){
            System.out.println(a + " is a prime number.");
            return true;
        }
        else{
            System.out.println(a + " isn't a prime number.");
            return false;
        }
    }

}