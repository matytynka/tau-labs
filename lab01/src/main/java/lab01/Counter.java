package lab01;

public class Counter {
    private int counter;
    public Counter(int number) {
        counter = number;
    }
    public void increase(int value){
        if (value >= 100) throw new IllegalArgumentException();
        if (counter + value <= 100) counter = counter + value;
        else {
            System.out.println("Value is too high");
            counter = 100;
        }
    }
    public void decrease(int value){
        if (value >= 100) throw new IllegalArgumentException();
        if (counter - value >= 0) counter = counter - value;
        else {
            System.out.println("Value is too low");
            counter = 0;
        }
    }
    public boolean check(){
        System.out.println("Value is perfect");
        return counter == 50;
    }
    public int getCounter() {
        return counter;
    }
}
