import httplib
import sys

# Arguman kontrolu
if len(sys.argv) < 3:
    print "Kullanim: python dirlite.py <host> <wordlist>"
    sys.exit(1)

target_host = sys.argv[1]
wordlist_file = sys.argv[2]

print "--- Tarama Basladi: " + target_host + " ---"

try:
    f = open(wordlist_file, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        path = line.strip()
        if not path:
            continue
        
        if path[0] != '/':
            path = '/' + path

        try:
            # En sade baglanti sekli (timeout parametresiz)
            h = httplib.HTTPSConnection(target_host)
            h.request("GET", path)
            response = h.getreply() # bazi eski surumlerde getreply() gerekebilir
            # Eger getreply hata verirse asagidaki satiri kullan:
            # response = h.getresponse()
            
            # Python 2'de status kontrolu
            status = response[0] if isinstance(response, tuple) else response.status
            
            if status == 200:
                print "[200 OK] -> " + path
            elif status in [301, 302]:
                print "[REDIRECT] -> " + path
            
            h.close()
        except:
            pass

except IOError:
    print "Hata: Dosya bulunamadi."
except Exception as e:
    print "Hata: " + str(e)

print "--- Bitti ---"
