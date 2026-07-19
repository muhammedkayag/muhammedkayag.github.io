import httplib
import sys

# Argumanlari al
if len(sys.argv) < 3:
    print "Kullanim: python dirlite_legacy.py <host> <wordlist>"
    sys.exit(1)

target = sys.argv[1]
wordfile = sys.argv[2]

print "--- Tarama Basliyor ---"

try:
    # Dosyayi en eski yontemle ac
    f = open(wordfile, "r")
    
    # Satir satir oku
    while 1:
        line = f.readline()
        if not line:
            break
            
        path = line.strip()
        if not path:
            continue
            
        if path[0] != '/':
            path = '/' + path

        try:
            # HTTPSConnection parametresiz (en sade hali)
            connection = httplib.HTTPSConnection(target)
            connection.request("GET", path)
            
            # Yaniti al
            response = connection.getresponse()
            
            # Sadece 200 veya Yonlendirmeleri yazdir
            if response.status == 200:
                print "[200 OK] -> " + path
            elif response.status == 301 or response.status == 302:
                print "[302 REDIRECT] -> " + path
                
            connection.close()
        except:
            # Her turlu baglanti hatasini pas gec
            pass
            
    f.close()
except:
    print "Dosya okuma hatasi!"

print "--- Tarama Bitti ---"
