import optparse
parser=optparse.OptionParser("This is a sample for option parser. Do whatever you want.\nUsage: \na = first option \nb = second option \nexample: python test.py -a string -b int")
parser.add_option('-a', dest='a', type='string', help='first option')
parser.add_option('-b', dest='b', type='int', help='second option')
options, args = parser.parse_args()
a=options.a
b=options.b
if a==None or b==None:
    print(parser.usage)
    exit(0)
print("first option: "+a+"\nsecond option: "+str(b))
