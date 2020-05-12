# Work with Jupyter notebook Twitter_ThaiNLP_v1 and quandl environment
import pandas as pd

class database(object):
    # Visual code  ctrl + ]  to tab multiple lines
    districtName_=[    
                        'เขตพระนคร',
                        'เขตดุสิต',
                        'เขตหนองจอก',
                        'เขตบางรัก',
                        'เขตบางเขน',
                        'เขตบางกะปิ',
                        'เขตปทุมวัน',
                        'เขตป้อมปราบศัตรูพ่าย',
                        'เขตพระโขนง',
                        'เขตมีนบุรี',
                        'เขตลาดกระบัง',
                        'เขตยานนาวา',
                        'เขตสัมพันธวงศ์',
                        'เขตพญาไท',
                        'เขตธนบุรี',
                        'เขตบางกอกใหญ่',
                        'เขตห้วยขวาง',
                        'เขตคลองสาน',
                        'เขตตลิ่งชัน',
                        'เขตบางกอกน้อย',
                        'เขตบางขุนเทียน',
                        'เขตภาษีเจริญ',
                        'เขตหนองแขม',
                        'เขตราษฎร์บูรณะ',
                        'เขตบางพลัด',
                        'เขตดินแดง',
                        'เขตบึงกุ่ม',
                        'เขตสาทร',
                        'เขตบางซื่อ',
                        'เขตจตุจักร',
                        'เขตบางคอแหลม',
                        'เขตประเวศ',
                        'เขตคลองเตย',
                        'เขตสวนหลวง',
                        'เขตจอมทอง',
                        'เขตดอนเมือง',
                        'เขตราชเทวี',
                        'เขตลาดพร้าว',
                        'เขตวัฒนา',
                        'เขตบางแค',
                        'เขตหลักสี่',
                        'เขตสายไหม',
                        'เขตคันนายาว',
                        'เขตสะพานสูง',
                        'เขตวังทองหลาง',
                        'เขตคลองสามวา',
                        'เขตบางนา',
                        'เขตทวีวัฒนา',
                        'เขตทุ่งครุ',
                        'เขตบางบอน',
                        'พระนคร',
                        'ดุสิต',
                        'หนองจอก',
                        'บางรัก',
                        'บางเขน',
                        'บางกะปิ',
                        'ปทุมวัน',
                        'ป้อมปราบศัตรูพ่าย',
                        'พระโขนง',
                        'มีนบุรี',
                        'ลาดกระบัง',
                        'ยานนาวา',
                        'สัมพันธวงศ์',
                        'พญาไท',
                        'ธนบุรี',
                        'บางกอกใหญ่',
                        'ห้วยขวาง',
                        'คลองสาน',
                        'ตลิ่งชัน',
                        'บางกอกน้อย',
                        'บางขุนเทียน',
                        'ภาษีเจริญ',
                        'หนองแขม',
                        'ราษฎร์บูรณะ',
                        'บางพลัด',
                        'ดินแดง',
                        'บึงกุ่ม',
                        'สาทร',
                        'บางซื่อ',
                        'จตุจักร',
                        'บางคอแหลม',
                        'ประเวศ',
                        'คลองเตย',
                        'สวนหลวง',
                        'จอมทอง',
                        'ดอนเมือง',
                        'ราชเทวี',
                        'ลาดพร้าว',
                        'วัฒนา',
                        'บางแค',
                        'หลักสี่',
                        'สายไหม',
                        'คันนายาว',
                        'สะพานสูง',
                        'วังทองหลาง',
                        'คลองสามวา',
                        'บางนา',
                        'ทวีวัฒนา',
                        'ทุ่งครุ',
                        'บางบอน',
                        ]

    def __init__(self):
        self.filepath_1=r'C:/Users/70018928/Quantra_Learning/nlp_road_database.xlsx'
        self.filepath_2=r'nlp_road_database.xlsx'    

    def ReadStreetName(self):
        try:
            streetDf=pd.read_excel(self.filepath_1, sheet_name='street') 
            addressDf=pd.read_excel(self.filepath_1, sheet_name='address') 
        except:
            streetDf=pd.read_excel(self.filepath_2, sheet_name='street') 
            addressDf=pd.read_excel(self.filepath_2, sheet_name='address')         
        
        return streetDf, addressDf
       
    def DataframeToList(self,inDf):
        inCol=inDf.columns
        inList=[]
        for n in inCol:
            inList=inList+inDf[n].values.tolist()
        inList = [x for x in inList if str(x) != 'nan']
        return inList
