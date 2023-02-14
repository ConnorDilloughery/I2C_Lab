import mma845x_shell as mma845



def main():
    Accelerometer= mma845.MMA845x (pyb.I2C (1, pyb.I2C.MASTER, baudrate = 100000), 29)
    Accelerometer.active()
    Hello= Accelerometer.get_accels()
    print(Hello)
    
    
if __main__ == "__name__":
    main()
    
