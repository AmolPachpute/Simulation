# Create your views here.
from django.views.generic import View
from django.shortcuts import render

states_dict = { 'LNS14000024':'UnitedStates',
                'ALURN':'Alabama','AKURN':'Alaska',
                'AZURN':'Arizona','ARURN':'Arkansas','CAURN':'California',
                'COURN':'Colorado','CTURN':'Connecticut','DEURN':'Delaware',
                'FLURN':'Florida','GAURN':'Georgia','HIURN':'Hawaii',
                'IDURN':'Idaho','ILURN':'Illinois','INURN':'Indiana','IAURN':'Iowa',
                'KSURN':'Kansas','KYURN':'Kentucky',
                'LAURN':'Louisiana','MEURN':'Maine',
                'MDURN':'Maryland','MAURN':'Massachusetts',
                'MIURN':'Michigan','MNURN':'Minnesota',
                'MSURN':'Mississippi','MOURN':'Missouri',
                'MTURN':'Montana','NEURN':'Nebraska',
                'NVURN':'Nevada','NHURN':'NewHampshire',
                'NJURN':'NewJersey','NMURN':'NewMexico',
                'NYURN':'NewYork','NCURN':'NorthCarolina',
                'NDURN':'NorthDakota','OHURN':'Ohio',
                'OKURN':'Oklahoma','ORURN':'Oregon',
                'PAURN':'Pennsylvania','RIURN':'RhodeIsland',
                'SCURN':'SouthCarolina','SDURN':'SouthDakota',
                'TNURN':'Tennessee','TXURN':'Texas','UTURN':'Utah',
                'VTURN':'Vermont','VAURN':'Virginia','WAURN':'Washington',
                'WVURN':'WestVirginia','WIURN':'Wisconsin','WYURN':'Wyoming'
               }

#states_list = [{'ALURN':'Alabama'},{'AKURN':'Alaska'},
#                {'AZURN':'Arizona'},{'ARURN':'Arkansas'},{'CAURN':'California'},
#                {'COURN':'Colorado'},{'CTURN':'Connecticut'},{'DEURN':'Delaware'},
#                {'FLURN':'Florida'},{'GAURN':'Georgia'},{'HIURN':'Hawaii'},
#                {'IDURN':'Idaho'},{'ILURN':'Illinois'},{'INURN':'Indiana'},{'IAURN':'Iowa'},
#                {'KSURN':'Kansas'},{'KYURN':'Kentucky'},
#                {'LAURN':'Louisiana'},{'MEURN':'Maine'},
#                {'MDURN':'Maryland'},{'MAURN':'Massachusetts'},
#                {'MIURN':'Michigan'},{'MNURN':'Minnesota'},
#                {'MSURN':'Mississippi'},{'MOURN':'Missouri'},
#                {'MTURN':'Montana'},{'NEURN':'Nebraska'},
#                {'NVURN':'Nevada'},{'NHURN':'New Hampshire'},
#                {'NJURN':'New Jersey'},{'NMURN':'New Mexico'},
#                {'NYURN':'New York'},{'NCURN':'North Carolina'},
#                {'NDURN':'North Dakota'},{'OHURN':'Ohio'},
#                {'OKURN':'Oklahoma'},{'ORURN':'Oregon'},
#                {'PAURN':'Pennsylvania'},{'RIURN':'Rhode Island'},
#                {'SCURN':'South Carolina'},{'SDURN':'South Dakota'},
#                {'TNURN':'Tennessee'},{'TXURN':'Texas'},{'UTURN':'Utah'},
#                {'VTURN':'Vermont'},{'VAURN':'Virginia'},{'WAURN':'Washington'},
#                {'WVURN':'WestVirginia'},{'WIURN':'Wisconsin'},{'WYURN':'Wyoming'}
#               ]

states_list = [ ('ALURN','Alabama'),('AKURN','Alaska'),
                ('AZURN','Arizona'),('ARURN','Arkansas'),('CAURN','California'),
                ('COURN','Colorado'),('CTURN','Connecticut'),('DEURN','Delaware'),
                ('FLURN','Florida'),('GAURN','Georgia'),('HIURN','Hawaii'),
                ('IDURN','Idaho'),('ILURN','Illinois'),('INURN','Indiana'),('IAURN','Iowa'),
                ('KSURN','Kansas'),('KYURN','Kentucky'),
                ('LAURN','Louisiana'),('MEURN','Maine'),
                ('MDURN','Maryland'),('MAURN','Massachusetts'),
                ('MIURN','Michigan'),('MNURN','Minnesota'),
                ('MSURN','Mississippi'),('MOURN','Missouri'),
                ('MTURN','Montana'),('NEURN','Nebraska'),
                ('NVURN','Nevada'),('NHURN','NewHampshire'),
                ('NJURN','NewJersey'),('NMURN','NewMexico'),
                ('NYURN','NewYork'),('NCURN','NorthCarolina'),
                ('NDURN','NorthDakota'),('OHURN','Ohio'),
                ('OKURN','Oklahoma'),('ORURN','Oregon'),
                ('PAURN','Pennsylvania'),('RIURN','RhodeIsland'),
                ('SCURN','SouthCarolina'),('SDURN','SouthDakota'),
                ('TNURN','Tennessee'),('TXURN','Texas'),('UTURN','Utah'),
                ('VTURN','Vermont'),('VAURN','Virginia'),('WAURN','Washington'),
                ('WVURN','WestVirginia'),('WIURN','Wisconsin'),('WYURN','Wyoming')
               ]

dates_list = ["2000-01-01", "2000-02-01", "2000-03-01", "2000-04-01", "2000-05-01", "2000-06-01", "2000-07-01", "2000-08-01",
              "2000-09-01", "2000-10-01", "2000-11-01", "2000-12-01", "2001-01-01", "2001-02-01", "2001-03-01", "2001-04-01",
              "2001-05-01", "2001-06-01", "2001-07-01", "2001-08-01", "2001-09-01", "2001-10-01", "2001-11-01", "2001-12-01",
              "2002-01-01", "2002-02-01", "2002-03-01", "2002-04-01", "2002-05-01", "2002-06-01", "2002-07-01", "2002-08-01",
              "2002-09-01", "2002-10-01", "2002-11-01", "2002-12-01", "2003-01-01", "2003-02-01", "2003-03-01", "2003-04-01",
              "2003-05-01", "2003-06-01", "2003-07-01", "2003-08-01", "2003-09-01", "2003-10-01", "2003-11-01", "2003-12-01",
              "2004-01-01", "2004-02-01", "2004-03-01", "2004-04-01", "2004-05-01", "2004-06-01", "2004-07-01", "2004-08-01",
              "2004-09-01", "2004-10-01", "2004-11-01", "2004-12-01", "2005-01-01", "2005-02-01", "2005-03-01", "2005-04-01",
              "2005-05-01", "2005-06-01", "2005-07-01", "2005-08-01", "2005-09-01", "2005-10-01", "2005-11-01", "2005-12-01",
              "2006-01-01", "2006-02-01", "2006-03-01", "2006-04-01", "2006-05-01", "2006-06-01", "2006-07-01", "2006-08-01",
              "2006-09-01", "2006-10-01", "2006-11-01", "2006-12-01", "2007-01-01", "2007-02-01", "2007-03-01", "2007-04-01",
              "2007-05-01", "2007-06-01", "2007-07-01", "2007-08-01", "2007-09-01", "2007-10-01", "2007-11-01", "2007-12-01",
              "2008-01-01", "2008-02-01", "2008-03-01", "2008-04-01", "2008-05-01", "2008-06-01", "2008-07-01", "2008-08-01",
              "2008-09-01", "2008-10-01", "2008-11-01", "2008-12-01", "2009-01-01", "2009-02-01", "2009-03-01", "2009-04-01",
              "2009-05-01", "2009-06-01", "2009-07-01", "2009-08-01", "2009-09-01", "2009-10-01", "2009-11-01", "2009-12-01",
              "2010-01-01", "2010-02-01", "2010-03-01", "2010-04-01", "2010-05-01", "2010-06-01", "2010-07-01", "2010-08-01",
              "2010-09-01", "2010-10-01", "2010-11-01", "2010-12-01", "2011-01-01", "2011-02-01", "2011-03-01", "2011-04-01",
              "2011-05-01", "2011-06-01", "2011-07-01", "2011-08-01", "2011-09-01", "2011-10-01", "2011-11-01", "2011-12-01",
              "2012-01-01", "2012-02-01", "2012-03-01", "2012-04-01", "2012-05-01", "2012-06-01", "2012-07-01", "2012-08-01",
              "2012-09-01", "2012-10-01", "2012-11-01", "2012-12-01", "2013-01-01", "2013-02-01", "2013-03-01", "2013-04-01",
              "2013-05-01", "2013-06-01", "2013-07-01", "2013-08-01", "2013-09-01", "2013-10-01", "2013-11-01", "2013-12-01",
              "2014-01-01", "2014-02-01", "2014-03-01", "2014-04-01", "2014-05-01", "2014-06-01", "2014-07-01", "2014-08-01"
              ]


class Analyze(View):
    
    template_name = "analyze.html"
    
    def get(self, request):
        #records_tuple = self.get_live_data()
        #records_dict = records_tuple[0]
        #dates_list = records_tuple[1]
        
        
        records_dict = self.get_stored_data()
        #import ipdb;ipdb.set_trace()
        
        
        return render(request, self.template_name, {'states_list':states_list,'records_dict':records_dict,'dates_list':dates_list,'dates_count':len(dates_list)})

    #def get_data():
    #    from cus_fred.fred import Fred
    #    fred_obj = Fred("6507f7fface9ac45d34868f450c1e7e9")
    #    
    #    #get all series for release 116.release 116 contains all list of unemployment in U.S and all local areas
    #    # the below function search_by_release return type is DataFrame(Pandas) so needs conversion
    #    series_dataframe  = fred_obj.search_by_release(112)
    #    series_dict = dict(series_dataframe.T) # contains series id as keys
    #    
    #    states = {}
    #    for i in series_dict.iterkeys():
    #        temp1 = series_dict[i]
    #        temp3 = {}
    #        if temp1['title'].startswith('Unemployment Rate'):
    #            temp3['id'] = temp1['id']
    #            temp3['title'] = temp1['title']
    #            temp3['last_updated'] = str(temp1['last_updated']).split(' ')[0]
    #            states[i] = temp3
    
    
    def get_data_old():
        from urllib2 import urlopen
        url = "http://api.stlouisfed.org/fred/release/series?release_id=112&&api_key=6507f7fface9ac45d34868f450c1e7e9&file_type=json"
        data = urlopen(url)
        data_dict = eval(data.readline())
        records_list =  data_dict.get('seriess')
        
        states_dict = {}
        for item in records_list:
            temp_dict = {}
            if item['title'].startswith('Unemp') or item['title'].startswith(' Unemp') or item['title'].startswith('unemp') :
                temp_dict['title'] = item['title']
                temp_dict['id'] = item['id']
                temp_dict['last_updated'] = item['last_updated']
                states_dict[item['id']] = temp_dict
                
    def get_live_data(self):
        from cus_fred.fred import Fred
        fred_obj = Fred("6507f7fface9ac45d34868f450c1e7e9")
        status = False;
        records_dict = {}
        for st in states_dict.keys():
            data = fred_obj.get_series(st)
            if not status:
                dates_list = []
                data_list = data.T.keys().tolist()
                for i in data_list:
                    dates_list.append(str(i)[0:10])
                status = True
            data_dict = dict(data.T)
            temp_dict = {}
            
            for i in data_dict.keys():
                temp_dict[str(i)[0:10]] = str(data_dict[i])[0:6]
            records_dict[states_dict[st]] = temp_dict
        return (records_dict, dates_list)
    
    def get_stored_data(self):
        from cus_fred.fred import Fred
        fred_obj = Fred("6507f7fface9ac45d34868f450c1e7e9")
        US_dict = {}
        us_data = fred_obj.get_series('LNS14000024')
        us_dict = dict(us_data.T)
        US = {}
        for i in us_dict.keys():
            US[str(i)[0:10]] = str(us_dict[i])[0:6]

        fl = open("/home/amol/data.json", "rb")
        data = fl.read()
        data_dict = eval(eval(data))
        data_dict['UnitedStates'] = US
        
        return data_dict
        

