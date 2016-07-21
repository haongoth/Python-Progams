/**
 * Created by haong on 6/19/2016.
 */
public class mainApp {
    public static void main(String[] args)
    {
        Factory aFactory = null;

        aFactory = new USCATV();
        aFactory.makeProduct();

        aFactory = new NonUSCATV();
        aFactory.makeProduct();
    }
}
