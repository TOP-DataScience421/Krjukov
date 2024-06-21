from decimal import Decimal
from datetime import time, date, datetime
from collections import defaultdict

class PowerMeter:
    
    def __init__(self, tariff1: Decimal = Decimal(0.0), tariff2: Decimal =  Decimal(0.0),
                 tariff2_starts: time = time(0, 0), tariff2_ends: time = time(0, 0)):
        self.tariff1 = Decimal(str(tariff1))
        self.tariff2 = Decimal(str(tariff2))
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = Decimal(0.0)
        self.charges = defaultdict(Decimal)
    
    def __repr__(self):
        return f"PowerMeter(tariff1={self.tariff1}, tariff2={self.tariff2}, tariff2_starts={self.tariff2_starts}, tariff2_ends={self.tariff2_ends})"
    
    def __str__(self):
        return f"Тариф 1: {self.tariff1}\nТариф 2: {self.tariff2}\nВремя начала второго тарифа: {self.tariff2_starts}\nВремя окончания второго тарифа: {self.tariff2_ends}\nСуммарная потребленная мощность: {self.power}\nНачисления за месяцы: {self.charges}"
    
    def meter(self, power: Decimal) -> Decimal:
        current_date = date.today().replace(day=1)
        if self.tariff2_starts  < self.tariff2_ends:
            cost = power * self.tariff2
        else:
            cost = power * self.tariff1
        self.charges[current_date] += cost
        return cost

pm1 = PowerMeter()
print(pm1.meter(2))

###  НЕ ПОНЯД КАК СДЕЛАТЬ((((((((((((((