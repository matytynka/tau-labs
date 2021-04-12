package lab03;

public class Arrays {
    public static int max(int[] numbers) {
        int maxNumber = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > maxNumber) {
                maxNumber = numbers[i];
            }
        }
        return maxNumber;
    }

    public static int min(int[] numbers) {
        int minNumber = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] < minNumber) {
                minNumber = numbers[i];
            }
        }
        return minNumber;
    }

    public static double avg(int[] numbers) {
        double sum = 0.00f;
        for (int value : numbers) {
            sum += value;
        }
        return sum / numbers.length;
    }

    public static int sum(int[] numbers) {
        int sumNumber = 0;
        for (int value : numbers) {
            sumNumber += value;
        }
        return sumNumber;
    }
}
