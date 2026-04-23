import httplib
import sys

# Arguman kontrolü
if len(sys.argv) < 3:
    print "Kullanim: python dirlite2.py <host> <wordlist_dosyasi>"
    print "Ornek: python dirlite2.py sekercity.com wordlist.txt"
    sys.exit(1)

target_host = sys.argv[1]
wordlist_file = sys.argv[2]

print "--- Tarama Basladi: " + target_host + " ---"

try:
    # Wordlist dosyasini aciyoruz
    with open(wordlist_file, "r") as f:
        for line in f:
            path = line.strip()
            if not path:
                continue
            
            # Yolun basinda / oldugundan emin olalim
            if path[0] != '/':
                path = '/' + path

            try:
                # HTTP/HTTPS baglantisini kur (Python 2 standart httplib)
                # Not: Hedef HTTPS ise HTTPSConnection kullanilir
                h = httplib.HTTPSConnection(target_host, timeout=5)
                h.request("GET", path)
                response = h.getresponse()

                # Durum kodlarini kontrol et
                if response.status == 200:
                    print "[200 OK] -> " + path
                elif response.status in [301, 302]:
                    print "[REDIRECT " + str(response.status) + "] -> " + path
                
                h.close()
            except Exception:
                # Baglanti hatalarini atla
                pass

except IOError:
    print "Hata: Wordlist dosyasi bulunamadi."
except Exception as e:
    print "Beklenmedik bir hata olustu: " + str(e)

print "--- Tarama Tamamlandi ---"
