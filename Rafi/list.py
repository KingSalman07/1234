my_list = [1,2,7,9, "Eduwork Videonya yang bener dong biar kelihatan sama saya", [7,10,77]]
rafi_ganteng ={
    "Mobil" : "Stargezer",
    "Type"  : "Hyundai",
}#dictionary

rafi_ganteng2 = {
    "Mad In" : "Indonesia, Korea" ,
    "Macos"  : "Apple", 
}

 

if __name__ == '__main__' :
    print(my_list[4])
    print(my_list[-1])
    my_list.append(890)
    print(my_list)

    rafi_ganteng.update(rafi_ganteng2)
    print(rafi_ganteng)
    # rafi_ganteng["Type"] = "Suzuki"
    # print(rafi_ganteng["Type"])

    
    
