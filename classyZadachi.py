def set_battery(self,charge):
        if not self.locked:
            if 0<charge<=100:
                self.battery = charge
            else:
                print('Не балуйся')
        else:
            print('Обратитесь в салон!')

def unlock(self,tries):
        if 0<tries<=self.touchid:
            print('Вы зашли')
        else:
            self.locked = True
            print('Телефон заблокирован!Попробуйте через 30 сек')

iphone = Phone('Iphone','XII PRO MAX','pink',2019,'new')
iphone.price = 1100
iphone.unlock(6)
iphone.set_battery(100)
iphone.description()

