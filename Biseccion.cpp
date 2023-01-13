#include <math.h>    // math.h
#include <iomanip>  // setprecision(), setw()
#include <iostream>
using namespace std;

double fnEcuacion(double valor) { return pow(valor, 2) - 2; }

int main(int argc, char const *argv[]) {
    double x1 = 1;
    double x2 = 2;
    double xm;
    double Es = 0.001;          // Error Standard o Absoluto
    double Er = abs(x2-x1);     // Error Relativo
    int i = 1;
    double it = round((log(x2 - x1) - log(Es)) / log(2));
    cout << it << endl;
    /*
    cout << "i" << "\t" << "x1" << "\t" << "x2" <<"\t" << "Er" <<"\t" << "xm"
         << "\t" << "fnEc(x1)" << "\t" << "fnEc(xm)" << endl;
    */     
    printf("i   |     x1    |     x2    |      Er   |     xm    |" \
           "   f(x1)   |   f(xm)   | f(x1) * f(xm) |\n");
    while (Er >= Es) {
        xm = (x1 + x2) / 2;
        /*
        cout << fixed << left << setprecision(4) << i << "\t" << x1 << "\t"
             << x2 << "\t" << Er << "\t" << xm << "\t" << fnEcuacion(x1) << "\t"
             << fnEcuacion(xm) << endl;
        */   
       printf("%3d |%10.4f |%10.4f |%10.4f |%10.4f |%10.4f |%10.4f \n",
               i, x1, x2, Er, xm,  fnEcuacion(x1), fnEcuacion(xm));
        if (fnEcuacion(x1) * fnEcuacion(xm) < 0) {
            x2 = xm;
        } else {
            x1 = xm;
        }
        Er = abs(x2 - x1);
        i = i + 1;
    }
    cout << xm << endl;
    return 0;
}
