  
class Temporalizador{
    Constrcutor(){
        '''inicializa el Temporalizador con 0 segundos y pausado'''
		this.tReal = 0
        this.tAct = 0
        this.breaker = False
		}
     setTReal( t){
        this.tReal = t}

     setTAct, t: int){
	 this.tAct = t}

     setBreak( b: bool){
	 this.breaker = b}

     getTReal()int{
	 return this.tReal}

     getTAct(){
	 return this.tAct}

     getBreak(){
	 return this.breaker}

     exportarAct( salida){
        try{
		salida(this.getTAct())
		}
        catch(e){
            salida = this.getTAct()
			}
		}
     resett():
        this.ingresarT(this.tReal)

     ingresarT( t):
        this.setTReal(t)
        this.setTAct(t)

     detener(){
        this.setBreak(False)
	 }
     continuar(){
        this.setBreak(True)
	 }
     iniciar( t, salida = None){
        this.ingresarT(t)
        this.setBreak(True)
        this.contar(salida = salida)
	 }
/*
    def contar(self, salida = None):
        if int(this.getTAct()) > 0 and self.getBreak():
            threading.Timer(1,lambda: [self.setTAct(self.getTAct() - 1), self.exportarAct(salida), self.contar(salida=salida)]).start()
        else:
            self.detener()*/
}