package lab03;
import static org.junit.Assert.*;
import org.junit.*;

public class CounterTest {
    @Test
    public void AfterIncreasing() {
        Counter counter = new Counter(50);
        counter.increase(10);
        Assert.assertEquals(60,counter.getCounter());
    }
    @Test
    public void AfterIncreasingAnother() {
        Counter counter = new Counter(4);
        counter.increase(2);
        Assert.assertEquals(6,counter.getCounter());
    }
    @Test
    public void AfterIncreasingTooMuch() {
        Counter counter = new Counter(90);
        counter.increase(20);
        Assert.assertEquals(100,counter.getCounter());
    }
    @Test
    public void AfterDecreasing() {
        Counter counter = new Counter(5);
        counter.decrease(1);
        Assert.assertEquals(4, counter.getCounter());
    }
    @Test
    public void AfterDecreasingAnother() {
        Counter counter = new Counter(34);
        counter.decrease(12);
        Assert.assertEquals(22, counter.getCounter());
    }
    @Test
    public void AfterDecreasingTooMuch() {
        Counter counter = new Counter(24);
        counter.decrease(98);
        Assert.assertEquals(0, counter.getCounter());
    }
    @Test
    public void AfterDecreasingTooMuchAnother() {
        Counter counter = new Counter(70);
        counter.decrease(71);
        Assert.assertEquals(0, counter.getCounter());
    }
    @Test
    public void AfterChecking() {
        Counter counter = new Counter(50);
        Assert.assertTrue(counter.check());
    }
    @Test
    public void AfterCheckingWrong() {
        Counter counter = new Counter(15);
        Assert.assertFalse(counter.check());
    }
    @Test
    public void AfterCheckingWrongAnother() {
        Counter counter = new Counter(99);
        Assert.assertFalse(counter.check());
    }
}
