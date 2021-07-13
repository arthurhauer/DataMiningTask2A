import csv
from typing import List

class Instance:
    result:str
    age: int
    sex:str
    steroid:bool
    antivirals:bool
    fatigue:bool
    malaise:bool
    anorexia:bool
    liver_big:bool
    liver_firm:bool
    spleen_paupable:bool
    spiders:bool
    ascites:bool
    varices:bool
    bilirubin:float
    alk_phosphate:int
    sgot:int
    albumin:float
    protime:int
    histology:bool
    
    def __init__(self,row:List[str]):
        self._get_result(row)
        self._get_age(row)
        self._get_sex(row)
        self._get_steroid(row)
        self._get_antivirals(row)
        self._get_fatigue(row)
        self._get_malaise(row)
        self._get_anorexia(row)
        self._get_liver_big(row)
        self._get_liver_firm(row)
        self._get_spleen_palpable(row)
        self._get_spiders(row)
        self._get_ascites(row)
        self._get_varices(row)
        self._get_bilirubin(row)
        self._get_alk_phosphate(row)
        self._get_sgot(row)
        self._get_albumin(row)
        self._get_protime(row)
        self._get_histology(row)

    def _check_unknown(self,value)->bool:
        return value=="?"
    
    def _get_field(self,row:List[str],index:int):
        value=row[index]
        if self._check_unknown(value):
            return "?"
        return value

    def _get_buckets(self,row:List[str],index:int,buckets:List[float]):
        if len(buckets)<1:
            return
        value=row[index]
        if self._check_unknown(value):
            return "?"
        value=float(value)
        for bucket in buckets:
            if value<=bucket:
                return bucket
    
    def _get_category(self,row:List[str],index:int,categories:dict):
        value=self._get_field(row,index)
        if self._check_unknown(value):
            return "?"
        value=int(value)
        if value in categories.keys():
            return categories[value]
        return value

    def _get_yes_no(self,row:List[str],index:int):
        return self._get_category(row,index,{
            1:"No",
            2:"Yes"
        })

    def _get_result(self,row:List[str]):
        self.result=self._get_category(row,0,{
            1:"Die",
            2:"Live"
        })
    
    def _get_age(self,row:List[str]):
        self.age=self._get_buckets(row,1,[10,20,30,40,50,60,70,80])
    
    def _get_sex(self,row:List[str]):
        self.sex=self._get_category(row,2,{
            1:"male",
            2:"female"
        })
    
    def _get_steroid(self,row:List[str]):
        self.steroid=self._get_yes_no(row,3)
    
    def _get_antivirals(self,row:List[str]):
        self.antivirals=self._get_yes_no(row,4)
    
    def _get_fatigue(self,row:List[str]):
        self.fatigue=self._get_yes_no(row,5)
    
    def _get_malaise(self,row:List[str]):
        self.malaise=self._get_yes_no(row,6)
    
    def _get_anorexia(self,row:List[str]):
        self.anorexia=self._get_yes_no(row,7)
    
    def _get_liver_big(self,row:List[str]):
        self.liver_big=self._get_yes_no(row,8)
    
    def _get_liver_firm(self,row:List[str]):
        self.liver_firm=self._get_yes_no(row,9)
    
    def _get_spleen_palpable(self,row:List[str]):
        self.spleen_palpable=self._get_yes_no(row,10)
    
    def _get_spiders(self,row:List[str]):
        self.spiders=self._get_yes_no(row,11)
    
    def _get_ascites(self,row:List[str]):
        self.ascites=self._get_yes_no(row,12)
    
    def _get_varices(self,row:List[str]):
        self.varices=self._get_yes_no(row,13)
    
    def _get_bilirubin(self,row:List[str]):
        self.bilirubin=self._get_buckets(row,14,[0.39, 0.80, 1.20, 2.00, 3.00, 4.00])
    
    def _get_alk_phosphate(self,row:List[str]):
        self.alk_phosphate=self._get_buckets(row,15,[33, 80, 120, 160, 200, 250])
        
    def _get_sgot(self,row:List[str]):
        self.sgot=self._get_buckets(row,16,[13, 100, 200, 300, 400, 500])
        
    def _get_albumin(self,row:List[str]):
        self.albumin=self._get_buckets(row,17,[2.1, 3.0, 3.8, 4.5, 5.0, 6.0])

    def _get_protime(self,row:List[str]):
        self.protime=self._get_buckets(row,18,[10, 20, 30, 40, 50, 60, 70, 80, 90])

    def _get_histology(self,row:List[str]):
        self.histology=self._get_yes_no(row,19)

    @staticmethod
    def get_csv_headers() -> List[str]:
        return [
            'Class', 
            'Age', 
            'Sex', 
            'Steroid', 
            'Antivirals', 
            'Fatigue', 
            'Malaise', 
            'Anorexia', 
            'Liver Big', 
            'Liver Firm', 
            'Spleen Palpable', 
            'Spiders', 
            'Ascites', 
            'Varices', 
            'Bilirubin', 
            'Alk Phosphate', 
            'SGOT', 
            'Albumin', 
            'Protime', 
            'Histology'
            ]

    def to_csv(self) -> List[str]:
        return [
            self.result, 
            self.age, 
            self.sex, 
            self.steroid, 
            self.antivirals,
            self.fatigue,
            self.malaise,
            self.anorexia,
            self.liver_big,
            self.liver_firm,
            self.spleen_palpable,
            self.spiders,
            self.ascites,
            self.varices,
            self.bilirubin,
            self.alk_phosphate,
            self.sgot,
            self.albumin,
            self.protime,
            self.histology
            ]

def process_dados() -> List[str]:
    instances:List[List[str]]=[]
    with open('hepatitis.csv', newline='') as dados:
        reader = csv.reader(dados, delimiter=',', quotechar='\"')
        next(reader, None)
        i = 1
        while True:
            try:
                row = next(reader)
            except StopIteration:
                break
            except Exception as e:
                print("Linha " + str(i) + " >> READ_ERROR >> ", e)
                i += 1
                continue
            new_insance: Instance
            try:
                new_insance = Instance(row)
            except Exception as e:
                print("Linha " + str(i) + " >> CONVERT_ERROR >> ", e)
                raise e
            instances.append(new_insance.to_csv())
        i += 1
        return instances

instances = process_dados()
with open('processed_dados.csv', 'w', newline='', encoding='utf-8') as processed_dados:
    writer = csv.writer(processed_dados)
    writer.writerow(Instance.get_csv_headers())
    writer.writerows(instances)