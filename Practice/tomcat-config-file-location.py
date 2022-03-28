# LEC 98 : Python script to find all tomcats home and config file locations

#-----------------------------  USING FUNCTIONS  --------------------------------------------------------------------------------------

'''
import os

def get_all_tomcats():
    list_of_config_files=[]
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file=="server.xml":
                list_of_config_files.append(os.path.join(r,each_file))
    return list_of_config_files


def display(home_Conf):
    for x in home_Conf.keys():
        print(f"The tomcat home is: {home_Conf[x][0]}")
        print(f"The config file is: {home_Conf[x][1]}") 
    return None

def main():
    list_of_tomcat=get_all_tomcats()
    #print(list_of_tomcat)
    cnt=1
    home_Conf={}
    for x in list_of_tomcat:
        #print(f"Info for tomcat: {cnt}")
        #print(f"The tomcat home is: {os.path.dirname(os.path.dirname(x))}")
        #print(f"The tomcat config file is: {x}")
        #home_Conf.append(os.path.dirname(os.path.dirname(x)))
        #home_Conf.append(x)
        
        tom_home=os.path.dirname(os.path.dirname(x))
        tom_config=x
        home_Conf['tomcat'+str(cnt)]=[tom_home,tom_config]
        cnt+=1
    display(home_Conf)
    return None

if __name__=="__main__":
    main()
'''