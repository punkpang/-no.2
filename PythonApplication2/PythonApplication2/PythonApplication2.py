Shopping = list() #จะเเอพเพนเข้าไปในลิสนี้เพื่อเก็บค่าไว้
def Shop():
  AP = 0
  print("\n---------------------------------------------------------------------------------------------")
  print("ลำดับที่      รุ่นรองเท้า        ราคา                   ส่วนลด                     จ่ายจริง")
  print("---------------------------------------------------------------------------------------------")
  count = 0 #นับเพื่อจะใส่ลำดับที่อยู่ข้างหน้า
  for i in Shopping:
      count+=1 #นับจำนวนครั้งที่เราวนลูบ
      print(end="\n") #ขึ้นบรรทัดใหม่ก่อนเค้า
      print(count,end="       ")
      for k in i:
        print(k.ljust(25),end="")  #เอาข้อความไปต่อท้าย ถ้าไม่มีเอนข้อความมันจะขึ้นบรรทัดใหม่
  print()
  for i in range(len(Shopping)): AP = AP  + float(Shopping[i][3]) #range กำหนดช่วง  #len คือจำนวนตัวในชอปปิ้งจำนวนตัวเเปล #ap บวก ap ไปเรื่อยๆ  #ถ้าอยากเพิ่ม int ก็จะเป็นเเค่ตัวเลข
  print("---------------------------------------------------------------------------------------------")
  print("รวมเป็นเงิน                                      %d"%AP) #%d กำหนดให้มันเป็น ข้อความ  #ap ผลรวมค่าราคา
  Store()

def Store():
  print("#---------------------------------------#\n             $AOFSHOESHOP$\n#---------------------------------------#")
  print('[1]NIKE\n[2]ADIDAS\n[3]FILA\n[4]Product list\n[5]no longer accepting products')
  Select = input('\nกรุณาเลือกยี่ห้อ: ')
  if Select == '1': F1()
  elif Select == '2': F2()
  elif Select == '3': F3()
  elif Select == '4': Shop()
  elif Select == '5': exit()
  else: Store()

def F1():
  print("\n--------------\nNIKE\n--------------")
  print('[1]Nike P-6000\n[2]Nike Air Max 200\n[3]Nike in season TR9')
  F1Price = int(input('เลือกรุ่น: '))
  if F1Price == 1:
      print("Nike P-6000  ราคา 3600 บาท  ส่วนลด 10%")
      Shopping.append(['Nike P-6000','3600','10%',str(3600*(90/100))])#เพิ่มค่ามาต่อท้ายกัน
      Store()
  elif F1Price == 2:
      print("Nike Air Max 200  ราคา 2400 บาท  ส่วนลด 10%")
      Shopping.append(['Nike Air Max 200','2400','10%',str(2400*(90/100))])
      Store()
  elif F1Price == 3:
      print("Nike in season TR9  ราคา 2700 บาท  ส่วนลด 10%")
      Shopping.append(['Nike in season TR9','2700','10%',str(2700*(90/100))])
      Store()
  else : print("\nกรุณาเลือกใหม่ค่ะ") ; F1()

def F2():
  print("\n--------------\nADIDAS\n--------------")
  print('[1] Adidas PULSEBOOST HD M\n[2] Adidas ULTRABOOST 19\n[3] Adidas LXCON 94')
  F2Price = int(input('เลือกรุ่น: '))
  if F2Price == 1:
     print("Adidas PULSEBOOST HD M  ราคา 5000 บาท  ส่วนลด 30%")
     Shopping.append(['Adidas PULSEBOOST HD M ','5000','30%',str(5000*(70/100))]) #เพิ่มค่าโดยเอาค่ามาต่อท้าย
     Store()
  elif F2Price == 2:
     print("Adidas ULTRABOOST 19 V1 ราคา 7300 บาท ส่วนลด 30%")
     Shopping.append(['Adidas ULTRABOOST 19','7300','30%',str(7300*(70/100))])
     Store()
  elif F2Price == 3:
     print("Adidas LXCON 94 V1  ราคา 6000 บาท  ส่วนลด 30%")
     Shopping.append(['Adidas LXCON 94','6000','30%',str(6000*(70/100))])
     Store()
  else: print("\nกรุณาเลือกใหม่ค่ะ") ; F2()

def F3():
  print("\n--------------\nFILA\n--------------")
  print('[1]FILA FA181546\n[2]FILA Ray CB Low\n[3]FILA Welly Indoor Court')
  F3Price = int(input('เลือกรุ่น: '))
  if F3Price == 1:
      print("FILA FA181546  ราคา 1290 บาท  ส่วนลด 20%")
      Shopping.append(['FILA FA181546','1290','20%',str(1290*(80/100))])
      Store()
  elif F3Price == 2:
      print("FILA Ray CB Low  ราคา 2691 บาท  ส่วนลด 20%")
      Shopping.append(['FILA Ray CB Low','2691','20%',str(2691*(80/100))])
      Store()
  elif F3Price == 3:
      print("FILA Welly Indoor Court ราคา 1290 บาท  ส่วนลด 20%")
      Shopping.append(['FILA Welly Indoor Court','1290','20%',str(1290*(80/100))])
      Store()
  else: print("\nกรุณาเลือกใหม่ค่ะ") ; F3()

def F1():
    print("\n--------------\nNIKE\n--------------")
    print('[1]Nike P-6000\n[2]Nike Air Max 200\n[3]Nike in season TR9')
    F1Price = int(input('เลือกรุ่น: '))
    if F1Price == 1:
        print("Nike P-6000  ราคา 3600 บาท  ส่วนลด 10%")
        Shopping.append(['Nike P-6000','3600','10%',str(3600*(90/100))])#เพิ่มค่ามาต่อท้ายกัน
        Store()
    elif F1Price == 2:
        print("Nike Air Max 200  ราคา 2400 บาท  ส่วนลด 10%")
        Shopping.append(['Nike Air Max 200','2400','10%',str(2400*(90/100))])
        Store()
    elif F1Price == 3:
        print("Nike in season TR9  ราคา 2700 บาท  ส่วนลด 10%")
        Shopping.append(['Nike in season TR9','2700','10%',str(2700*(90/100))])
        Store()
    else : print("\nกรุณาเลือกใหม่ค่ะ") ; F1()
Store()
