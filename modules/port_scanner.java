import java.net.*;
import java.io.IOException;

public class port_scanner {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("[!] Usage: java port_scanner <target>");
            return;
        }
        String target = args[0];
        int[] commonPorts = {21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080};

        System.out.println("[*] Scanning common ports on: " + target);
        for (int port : commonPorts) {
            try {
                Socket socket = new Socket();
                socket.connect(new InetSocketAddress(target, port), 1000); // 1 second timeout
                socket.close();
                System.out.println("[+] Port " + port + " is OPEN");
            } catch (IOException e) {
                // Port is closed or filtered, silence is golden.
            }
        }
    }
}
