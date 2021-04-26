package lab05;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.runners.MockitoJUnitRunner;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class MessageTest {

    MessageEncoder messageEncoder = new MessageEncoder();

    @Mock
    Message message = Mockito.mock(Message.class);

    @Test
    public void smallLetters() {
        when(message.getMessage()).thenReturn("wiadomosc");
        Assert.assertEquals("WIADOMOSC", messageEncoder.encode(message));
        verify(message, Mockito.times(1)).getMessage();
    }

    @Test
    public void bigLetters() {
        when(message.getMessage()).thenReturn("TEKST");
        Assert.assertEquals("TEKST", messageEncoder.encode(message));
        verify(message, Mockito.times(1)).getMessage();
    }

    @Test
    public void mixedLetters() {
        when(message.getMessage()).thenReturn("POZDRawiam");
        Assert.assertEquals("POZDRAWIAM", messageEncoder.encode(message));
        verify(message, Mockito.times(1)).getMessage();
    }
}

