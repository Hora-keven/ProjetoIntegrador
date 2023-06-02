import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Write {
    public static void main(String[] args) {
        String csvFile = "C://Users//53688621808//Documents//planilhas//motorola.csv";
        String line = "";
        String csvSeparator = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            while ((line = br.readLine()) != null) {
                String[] data = line.split(csvSeparator);
                for (String value : data) {
                    System.out.print(value + " ");
                }
                System.out.println();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

