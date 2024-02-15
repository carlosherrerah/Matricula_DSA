package pilitas;

public class Nodo {
    String matricula;
    String nombre;
    int cuatrimestre;
    Nodo sig;    // Linea de oro
    
    public Nodo(){
    }

    public Nodo(String matricula, String nombre, int cuatrimestre) {
        this.matricula = matricula;
        this.nombre = nombre;
        this.cuatrimestre = cuatrimestre;
        this.sig = null;
    }

    public Nodo(Nodo reg) {
        this.matricula = reg.matricula;
        this.nombre = reg.nombre;
        this.cuatrimestre = reg.cuatrimestre;
        this.sig = null;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getCuatrimestre() {
        return cuatrimestre;
    }

    public void setCuatrimestre(int cuatrimestre) {
        this.cuatrimestre = cuatrimestre;
    }

    public Nodo getSig() {
        return sig;
    }

    public void setSig(Nodo sig) {
        this.sig = sig;
    }

    @Override
    public String toString() {
        return "Nodo [matricula=" + matricula + ", nombre=" + nombre + ", cuatrimestre=" + cuatrimestre + ", sig=" + sig
                + "]";
    }

    

}
