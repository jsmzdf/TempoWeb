
import Temporalizador from 'Temporalizador';
class Rutina{
     constructor(nomb, tRutn, foutRut,
        tDesc, foutDesc, tEjer, foutEje){
        this.nomb = nomb;
        this.rutn = Temporalizador();
        this.rutn.ingresarT(tRutn);
        this.foutRutn = foutRut;
        this.ejrc = Temporalizador();
        this.ejrc.ingresarT(tEjer);
        this.foutEjrc = foutEjer;
        this.dscn = Temporalizador();
        this.dscn.ingresarT(tDesc);
        this.foutDscn = foutDesc;
        this.brkr = False;
        this.stat = "Ejercicio";
		}
     detener(){
        this.ejrc.detener();
        this.dscn.detener();
        this.rutn.detener();
        this.brkr = False;
	}
     cambiarStado(){
        if (this.stat == "Ejercicio"){
		this.stat = "Descanso"};
        if (this.stat == "Descanso"){
		this.stat = "Ejercicio"};
	}	
     controladorState(tAct):
        //print("Quedan", tAct, "segundos de ", this.stat)
        if this.stat == "Ejercicio" && this.foutEjrc{
		this.foutEjrc(tAct);
		}

        if this.stat == "Descanso" && this.foutDscn{
			this.foutDscn(tAct);
		}

        if int(tAct) == 0:
            if self.stat == "Ejercicio":
                self.ejrc.detener()
            elif self.stat == "Descanso":
                self.dscn.detener()
            self.cambiarStado()

            if self.brkr == True:
                self.iniciarState()

    def iniciarState(self):
        if self.stat == "Ejercicio":
            self.ejrc.iniciar(self.ejrc.getTReal(), salida=self.controladorState)
        elif self.stat == "Descanso":
            self.dscn.iniciar(self.dscn.getTReal(), salida=self.controladorState)

    def controlarRutina(self, tAct):
        print("Quedan", tAct, "segundos de la rutina total de", self.nomb)
        if self.foutRutn:
            self.foutRutn(tAct)

        if int(tAct) == 0:
            self.detener()
            print("La rutina", self.nomb, "ha finalizado totalmente")

    def iniciar(self):
        self.brkr = True
        self.rutn.iniciar(self.rutn.getTReal(), salida=self.controlarRutina)
        self.iniciarState()

    def getBreak(self):
        return self.brkr
}