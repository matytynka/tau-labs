package lab03;

import org.junit.Assert;
import org.junit.Test;

public class ArraysTest {
    @Test
    public void maxNumber() {
        Assert.assertEquals(10, Arrays.max(new int[]{10, 9, 8, -7, 6}));
    }
    @Test
    public void maxNumberOnlyNegative() {
        Assert.assertEquals(1, Arrays.max(new int[]{-10, -5, 1, -2, -13}));
    }
    @Test
    public void minNumber() {
        Assert.assertEquals(-999, Arrays.min(new int[]{-998, -999, -90, 1, 0}));
    }
    @Test
    public void minNumberOnlyPositive() {
        Assert.assertEquals(1, Arrays.min(new int[]{9, 7, 3, 1, 5}), 3);
    }
    @Test
    public void avgNumber() {
        Assert.assertEquals(5, Arrays.avg(new int[]{3, 4, 5, 6, 7}), 3);
    }
    @Test
    public void sumOfNumbers() {
        Assert.assertEquals(25, Arrays.sum(new int[]{3, 4, 5, 6, 7}));
    }
    @Test
    public void sumOfNumbersWithNegative() {
        Assert.assertEquals(5, Arrays.sum(new int[]{1, 2, 3, 4, -5}));
    }
}