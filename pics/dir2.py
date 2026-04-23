import httplib
import sys

# Argumanlar
if len(sys.argv) < 3:
    print "Kullanim: python dirlite.py <host> <wordlist>"
    sys.exit(1)

target = sys.argv[1]
wordfile = sys.argv[2]

print "--- Tarama Basladi (Hedef: " + target + ") ---"

try:
    f = open(wordfile, "r")
    while 1:
        line = f.readline()
        if not line: break
        
        path = line.strip()
        if not path: continue
        if path[0] != '/': path = '/' + path

        # Nereyi denedigini gormek icin bunu ekledim
        sys.stdout.write("\rDeneniyor: " + path + "               ")
        sys.stdout.flush()

        try:
            # Eger HTTPS hata verirse HTTPConnection yap kanki
            conn = httplib.HTTPSConnection(target)
            conn.request("GET", path)
            res = conn.getresponse()
            
            if res.status == 200:
                print "\n[+] BULDUM: " + path + " (200 OK)"
            elif res.status == 301 or res.status == 302:
                print "\n[*] YONLENDIRME: " + path + " (" + str(res.status) + ")"
            
            conn.close()
        except:
            # Baglanti hatasi olursa buraya duser
            pass
            
    f.close()
except:
    print "\nDosya okunamadi!"

print "\n--- Tarama Bitti ---"
