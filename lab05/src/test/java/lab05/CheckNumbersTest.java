package lab05;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.Mockito;
import static org.mockito.Mockito.*;

public class CheckNumbersTest {

    @Mock
    CheckNumbers checkNumbers = Mockito.mock(CheckNumbers.class);

    @Test
    public void sameNumbersGCD() {
        when(checkNumbers.gcdByBruteForce(5,5)).thenReturn(5);
        Assertions.assertEquals(5, checkNumbers.gcdByBruteForce(5,5));
    }

    @Test
    public void oddNumberTrue() {
        when(checkNumbers.isOdd(9)).thenReturn(true);
        Assertions.assertTrue(checkNumbers.isOdd(9));
    }

    @Test
    public void intToString() {
        when(checkNumbers.toString(1)).thenReturn("1");
        Assertions.assertEquals(checkNumbers.toString(1),"1");
    }

}
