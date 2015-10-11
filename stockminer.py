from yahoo_finance import Share

Aurinia = Share('AUPH')

Groupon = Share('GRPN')

Kratos = Share('KTOS')

Parker = Share('PRKR')

print "Aurinia Pharmaceuticals' stock price is $%s" % Aurinia.get_open()

print "Groupon's stock price is $%s" % Groupon.get_open()

print "Kratos' stock price is $%s" % Kratos.get_open()

print "ParkerVision's stock price is $%s" % Parker.get_open()

