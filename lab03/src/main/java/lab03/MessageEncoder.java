package lab03;

public class MessageEncoder {
    public String encode(Message message) {
        return message.getMessage().toUpperCase();
    }
}
