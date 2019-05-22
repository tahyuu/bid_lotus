#!/usr/bin/env python
import os,  subprocess, time, sys
currentDir = os.getcwd()
#import the base py file
sys.path.append(currentDir +"/Common")

if __name__=="__main__":
    while True:
        if True:
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
            
