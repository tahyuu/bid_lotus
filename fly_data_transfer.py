#!/usr/bin/env python
import os,  subprocess, time, sys
currentDir = os.getcwd()
#import the base py file
import re
sys.path.append(currentDir +"/Common")


class TransferFile:
    def __init__(self, fileName=None):
	    self._setting = {} 
	    if fileName == None:
	        return
	    try:
	        self._file = open(fileName, "r")
	    except IOError, exception:
	        print "Can't open the configuratin file: ", exception
	        sys.exit(1)
	    
	#self.Read()
    def Read(self):
        lines = self._file.readlines()
        #print len(lines)
        #cos=''
        i=1
        for line in lines:

            if line.find('//')==0 or line.find('@')==0:
                continue
            if i>10:
                break
            #print line.split()
            if line.split():
                name = line.split()[0]
                Om = line.split()[1]
                data_re = re.compile(r'([1-9]\d*\.?\d*)|(0\.\d*[1-9])')
                data_m = data_re.search(Om)
                Om_data=0
                if data_m:
                    Om_data=data_m.group()
                
                start1 = line.split()[2]
                start2 = line.split()[3]
                r= line.split()[4]
                if r!='R': 
                    x1= line.split()[5]
                    y1= line.split()[6]
                    x2= line.split()[7]
                    y2= line.split()[8]
                    atT = line.split()[9]
                    ten1 = line.split()[10]
                    ten2 = line.split()[11]
                else:
                    x1= line.split()[5]
                    y1= line.split()[6]
                    x2= line.split()[7]
                    y2= line.split()[8]
                    atT = line.split()[9]
                    ten1 = line.split()[10]
                li_cop='WCOP,    %s, %s,  %s,   %s,  %s,--------,--------,N,N,N,0,0,0' %(name,x1,y1,x2,y2)
                li_cos='WCOS,    %s,%s 1-2      ,  , ,00,00,   0,   0,%.3E,%.3E,  0.0 [%%],  0.0 [%%],1,0,0,0,0,0.000,0.000E+000,   0,   0,0,0,0,00,0.000E+000' %(i,name,float(Om_data),float(Om_data))
                print line
                print li_cop
                print li_cos
                i=i+1
                    #ten2 = line.split()[11]
	#while line != '':
	#    print line
	#while line != '':
	#    print line
	#    if line[0][0] != '/' and line != '\n':
	#	line2 = line.split('\t')
	#	line2 = filter(self.IsNotNull, line2)
		#print line2
		#name = line2[0].strip()
		#value = line2[1].strip()
		#comment = line2[2].strip()
		#self._setting[name] = value
	#    line = self._file.readline()


if __name__=="__main__":
    transfer_file ='LSB1GP24D_bot.ca8'
    while True:
        if True:
            if transfer_file:
                break
            #cre=RFWIFIIC(1)
            #cre.ScanData()
            #cre.Wait(cre.wait_time)
            #cre.Wait(4)
            #cre.InitLog()
            #cre.Run()
            #write_str=""
            #write_str="serial_number,amb_0_ic_raw,amb_0_ic_read_temp,amb_0_ic_real_temp,amb_0_differ,amb_1_ic_raw,amb_1_ic_read_temp,amb_1__ic_real_temp,amb_1_differ,amb_4_ic_raw,amb_4_ic_read_temp,amb_4_ic_real_temp,amb_4_differ\n"
            #write_str=write_str+cre.testStartTime+","
            #write_str=write_str+cre.serial_number+","
            transfer_type= raw_input("command list as belows:\n1, transfer CA8 --> COP&COS\n2, transfer CA9 --> COP&COS\n3, transfere TA8 -->COP&COS\nplease input the command index:")
            if transfer_type=='1':
                 transfer_file = raw_input("please input the CA8 file:")
                 if transfer_file.find('.ca8')<0:
                     raw_input("file name error, not a ca8 file, input enter to continue")
                     continue
            if transfer_type=='2':
                 transfer_file = raw_input("please input the CA9 file:")
                 if transfer_file.find('.ca9')<0:
                     raw_input("file name error, not a ca9 file, input enter to coninue")
                     continue
            if transfer_type=="3":
                 transfer_file = raw_input("please input the TA8 file:")
                 if transfer_file.find('.ca9')<0:
                     raw_input("file name error, not a ta8 file, input enter to continue")
                     continue
            if transfer_type=="q":
               break

    tfer = TransferFile(transfer_file)
    tfer.Read()
    try:
         #open the file
         pass
    except:
         pass
            #print "Error"
        #for amb_index in [0,1,4]:
        #    write_str=write_str+str(cre.amb_sensores["amb%s_read_raw_data" %amb_index])+","
        #    write_str=write_str+str(cre.amb_sensores["amb%s_read_temp" %amb_index])+","
        #    write_str=write_str+str(cre.amb_sensores["amb%s_real_temp" %amb_index])+","
        #    write_str=write_str+str(float(cre.amb_sensores["amb%s_real_temp" %amb_index])-float(cre.amb_sensores["amb%s_read_temp" %amb_index]))+","
        #write_str=write_str+(cre.testStatus and "pass" or "fail")
        #log=Log()
        #log.Open3('data.csv')
        #log.PrintNoTime(write_str.strip(","))
            
