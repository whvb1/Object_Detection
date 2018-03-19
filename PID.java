
// need to initialize as a global variable 
// this is just a basic template, but I can change it once I see where it is needed
/**
 * @author willv
 * FTC VERTIGO 7953
 */
public class PID {
	 String name = "";
	 double Kp = 0.0;
	 double Ki = 0.0;
	 double Kd = 0.0;
	 double Error = 0.0;
	 double LastError = 0.0; 
	 double Setpoint = 0.0;
	 double currentVal = 0.0;
	 double u = 0;
	 double reset = 0; 
	public PID(double Kp,double Ki,double Kd, String name) {
		// TODO Auto-generated constructor stub
		this.Kp = Kp;
		this.Ki = Ki;
		this.Kd = Kd; 
		this.name = name;
		this.Setpoint=0;
	}	
	public void setcurrentVal(double currentVal) {
		this.currentVal=currentVal;
	}
	public void setSetpoint(double Setpoint) {
		this.Setpoint=Setpoint;
	}
	public void setError() {
		this.Error = this.Setpoint - this.currentVal;
	}
	public void setReset() {
		this.reset = this.reset + this.Ki*this.Error;
	}
	public double setuPID() {
		this.u = this.Kp * this.Error +this.Ki*(this.reset)+this.Kd*(this.Error-this.LastError);
		this.LastError=Error;
		return u; 
	}
	public double setuPD() {
		this.u = this.Kp * this.Error+this.Kd*(this.Error-this.LastError);
		this.LastError=Error;
		return u; 
	}
	public double doPID(double Setpoint, double currentVal) {
		setcurrentVal(currentVal);
		setSetpoint(Setpoint);
		setError();
		setReset();
		double output = setuPID();
		return output;
	}
	public double doPD(double Setpoint, double currentVal) {
		setcurrentVal(currentVal);
		setSetpoint(Setpoint);
		setError();
		setReset();
		double output = setuPD();
		return output;
	}
	public String getInfo() {
		String info = "";
		info="Name: "+this.name+"\n"+"Kp: "+this.Kp+"\n"+"Ki: "+
				this.Ki+"\n"+"Kd: "+this.Kd+"\n"+"currentVal: "+this.currentVal+"\n"+
				"Setpoint: "+this.Setpoint+"\n";		
		return info;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// this should be global
		PID drivetrain = new PID (1,0.5,2,"drivetrain");
		System.out.println("PID for drivetrain constructed");
		int valOfRobot = 0; //placeholder for the value that you wuold get from the robot about it's situation
		int Setpoint = 1;
		// this next part is definitely not ready
		drivetrain.doPID(Setpoint, valOfRobot);// returns a the value of the adjustment needed ex. could be the increase in power or something
		System.out.println(drivetrain.getInfo());
		System.out.println("Running Properly");
		
	}

}
