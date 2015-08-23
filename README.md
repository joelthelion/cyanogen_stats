#Scraper for http://stats.cyanogenmod.com/map/

Install the supporting client socketIO library with ```sudo pip install -r requirements.txt``` (or use a virtualenv).

Running main.py will output new installs in convenient CSV format.

###Sample output:

    carrier_id,country,hash,ip,latitude,longitude,name,version
    40402,in,32CBFE679FDE05B4ABC9F690C4EBC1B0,59.97.95.123,20,77,tomato,11.0-XNPH05Q-tomato
    28601,tr,BC80C0BA7FC2277543689F4D032F61F7,176.43.16.62,41.01859999999999,28.964699999999993,n7000,11-20150524-NIGHTLY-n7000
    26201,de,2984929C6063C3E1BD160E0C3F1DF4A5,89.15.81.174,49.98070000000001,8.431999999999988,jflte,11-20140806-SNAPSHOT-InstallerXNPQ32P-jflte
    40443,in,A47580C5D669C88C355D5FD9B5B7EB1B,1.39.63.209,20,77,bacon,11.0-XNPH05Q-bacon
    60503,tn,A9E6BC683CF534F08269F3B239F89237,197.19.211.18,34,9,galaxysmtd,10.1.0-RC2-galaxysmtd
    29703,me,B8C27D537D4393FFC330E53D700BC11D,78.155.63.205,43.21610000000001,19.005300000000005,i9100,11-20140618-NIGHTLY-i9100
    23430,gb,9EFA1EC7F3F2E32C9D78AF35D387B167,92.26.14.174,51.5,-0.12999999999999545,bacon,11.0-XNF9XBS28K-bacon
    22210,it,D63C03D54E80FE0013AFBDDE3BE00608,151.82.182.233,42.83330000000001,12.833300000000008,galaxysmtd,11-20140104-SNAPSHOT-M2-galaxysmtd
    25002,ru,64A0F8F8CE783E1BED51529223542C43,78.25.123.64,59.89439999999999,30.264199999999988,ancora,10.2-20140913-UNOFFICIAL-ancora
