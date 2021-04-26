package lab05;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.Mockito;
import static org.mockito.Mockito.*;

public class CheckAnotherTest {

    @Mock
    CheckAnother checkAnother = Mockito.mock(CheckAnother.class);

    @Test
    public void substractToNegative() {
        when(checkAnother.substract(5,6)).thenReturn(-1);
        Assertions.assertEquals(-1, checkAnother.substract(5,6));
    }

    @Test
    public void checkFalse() {
            when(checkAnother.orGate(false,false)).thenReturn(false);
            Assertions.assertFalse(checkAnother.orGate(false, false));
    }

    @Test
    public void stringifyResult() {
        when(checkAnother.substractStringify(checkAnother.substract(5,6))).thenReturn("-1");
        Assertions.assertEquals("-1", checkAnother.substractStringify(checkAnother.substract(5,6)));
    }
}
