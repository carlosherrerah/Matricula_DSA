public class SeekArray {
        public static void main(String[] args) {
            int datos[] = {6,2,9,3,1};
            int pos = -1;
            int num = 9;

            for (int i = 0; i < datos.length; i++) {
                if (num == datos[i]) {
                    pos = i;
                    break;
                }
            }
            System.out.println(pos);
        }

}

