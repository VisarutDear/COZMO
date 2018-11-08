a = {'owner':'DEAR','relative':'AIM','line':'LINEAIM',
            'med' : [{
                'medname':'para',
                'time':['08:00','12:00','20:30'],
                'quantity':'1',
                    'total':'10'},
                    {'medname':'coke',
                    'time':['12:00','17:00'],
                    'quantity':'1',
                    'total':'10'},
                    {'medname':'pepsi',
                    'time':['08:00','12:00'],
                    'quantity':'2',
                    'total':'10'}
                    ]}
alarm_med = []
    
    # for i in range(len(a['med'])):
    #     for j in range(len(a['med'][i]['time'])):
    #         print(i,a['med'][i]['time'][j])
for i in range(len(a['med'])):
            for j in range(len(a['med'][i]['time'])):
                if "08:00" in a['med'][i]['time'][j]:
                    alarm_med.append({'name':a['med'][i]['medname'],'quantity':a['med'][i]['quantity']})

print((alarm_med))