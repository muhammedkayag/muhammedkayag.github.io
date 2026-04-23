import httplib
import sys
import string

# Python 1'de modern argüman yönetimi kısıtlıdır
if len(sys.argv) < 3:
    print "Kullanim: python dirlite.py <host> <wordlist_dosyasi>"
    print "Ornek: python dirlite.py sekercity.com wordlist.txt"
    sys.exit(1)

target_host = sys.argv[1]
wordlist_file = sys.argv[2]

print "--- Tarama Basladi: ", target_host, " ---"

try:
    # Dosyayı okuma modunda açıyoruz
    f = open(wordlist_file, "r")
    while 1:
        line = f.readline()
        if not line:
            break
        
        # Satır sonundaki boşlukları temizle (Python 1.5 standardı)
        path = string.strip(line)
        if not path:
            continue
            
        if path[0] != '/':
            path = '/' + path

        try:
            # httplib Python 1'in temel HTTP kütüphanesidir
            h = httplib.HTTP(target_host)
            h.putrequest('GET', path)
            h.putheader('Host', target_host)
            h.putheader('User-Agent', 'DirLite/1.0')
            h.endheaders()

            errcode, errmsg, headers = h.getreply()

            # Sadece 200 (OK) veya 301/302 (Redirect) olanları göster
            if errcode == 200:
                print "[200 OK] -> ", path
            elif errcode == 301 or errcode == 302:
                print "[REDIRECT ", errcode, "] -> ", path
                
        except:
            # Bağlantı hatalarını sessizce geç
            pass
            
    f.close()
except IOError:
    print "Hata: Wordlist dosyasi bulunamadi."

print "--- Tarama Tamamlandi ---"
