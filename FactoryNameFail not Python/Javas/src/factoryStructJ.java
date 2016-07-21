/**
 * Created by haong on 6/18/2016.
 */
interface Factory {
    public void makeProduct();
}

class USFactory implements Factory {
    public void makeProduct() {
        System.out.println("These products make in US");
    }
}

class NonUSFactory implements Factory {
    public void makeProduct() {
        System.out.println("These products make in China");
    }
}

class Satcom extends USFactory{
    public void makeProduct() {
        System.out.println("These products make by Satcom department in US");
    }
}

class CATV extends  USFactory{
    public void makeProduct() {
        System.out.println("These products make by CATV department in US");
    }
}

class Gyro extends USFactory{
    public void makeProduct(){
        System.out.println("These products make by Gyro department in US");
    }
}

class Satcom extends NonUSFactory{
    public void makeProduct() {
        System.out.println("These products make by Satcom department in Thailand");
    }
}

class CATV extends  NonUSFactory{
    public void makeProduct() {
        System.out.println("These products make by CATV department in China");
    }
}